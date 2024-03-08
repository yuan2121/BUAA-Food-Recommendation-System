<!--
参考：https://github.com/xiaotanit/tan_vue.git
-->
<script lang="ts">
import type {ComponentPublicInstance} from 'vue';
import {defineComponent} from "vue";
import WaterfallCard from "@/components/WaterfallCard.vue";

import type {CommentSummary, DishSummary, SummaryData} from "@/utils/dataTypes";
import {generatePost} from "@/utils/protocal";
import {showNotify, showToast} from "vant";

export default defineComponent({
  name: 'Waterfall',
  components: {WaterfallCard},
  props: {
    'type': {
      type: String as () => 'home' | 'community',
      default: 'home'
    }
  },
  data() {
    return {

      dataList: [] as SummaryData[], //列表数据
      haveData: 0, //是否有数据，1=无，2=有，0=页面还未初始化
      pageIndex: 1, //页码
      pageSize: 8, //每页加载数据数量
      pullLoading: false,  //下拉刷新进行中，请求开始true, 请求完成false，用于下拉刷新组件van-pull-refresh
      bottomLoading: false,  //上拉加载更多中，上拉触底时自动变成true, 请求完成设置为false, 用于列表组件van-list
      finished: false, //上拉加载是否加载完最后一页数，用于组件van-list
      itemCount: 0, //上一次加载完成后的瀑布流item个数
      lastRowHeights: [0, 0] as [number, number], //最后一行标签的顶部间距+高度，2列

      boxMargin: 7, //每个item之间的边距
      boxSidePadding: 10,  // 屏幕两侧空白
      boxWidth: 165, //每个item宽度
    }
  },
  created() {
    //当前瀑布流设置为两列，计算瀑布流每个item和图片的宽度
    let screenWidth = document.body.offsetWidth; //屏幕宽度
    this.boxWidth = (screenWidth - this.boxMargin - this.boxSidePadding*2)/2; //每个item的宽度
    this.onRefresh(); //刷新数据
  },
  methods:{
    showToast,
    like(comment_id: number, index: number) {
      generatePost('/community/support', {
        id: comment_id
      }).then(response => {
        if (response.data?.code !== 0) {
          throw new Error(`Errcode: ${response.data?.code}`)
        }
      }, err => {
        showNotify({message: `发生错误：${err}`})
      })
    },
    onRefresh(){ //下拉刷新
      // if (this.isLoading) return; //还在请求中，返回
      this.pageIndex = 1; //重置第一页
      this.pullLoading = true; //开始加载
      this.finished = false; //上拉加载"所有数据已经完成"标识 重置为false

      //接口请求
      this.getDataList();
    },
    onBottomLoad(){ //上拉加载更多
      if (this.finished) return; //说明所有数据已经加载完毕，返回
      // console.log("刷新一次")
      this.getDataList(); //下一页数据请求中
    },
    //数据请求
    getDataList() {
      const promise = (() => {
        if (this.type == 'community') {
          const param = {
            n: 10
          }
          return generatePost('/community/random', param)
        } else {
          const param = {
            n: 10
          }
          return generatePost('/dish/random', param)
        }
      }) ()

      promise.then(async (res)=>{
        return (() => {
          if (this.type == 'community') {
            let response_list: CommentSummary[] = res.data?.comments ?? []

            return Promise.all(response_list.map(async e => {
              const dish_summary = await generatePost('/dish/get_detail', {dish_id: e.dish_id}).then(response => {
                return response.data?.summary as DishSummary
              })
              return {
                id: dish_summary.id,
                comment_id: e.id,
                cover: `/images/${dish_summary.name}.jpg`,
                sign: e.summary,
                sub_title1: e.user_id,
                sub_title2: (() => {
                  switch (Math.floor(Math.random()*4)) {
                    case 0:
                      return `${e.likes} 人喜欢`
                    case 1:
                      return `评分 ${e.score} 分`
                    case 2:
                      return `${e.comments} 条评论`
                    case 3:
                      return dish_summary.window
                    default:
                      return dish_summary.window
                  }
                })(),
                tags: []
              } as SummaryData
            }))
          } else {
            let response_list: DishSummary[] = res.data?.dishes ?? []
            return Promise.resolve(
                response_list.map(e => ({
              id: e.id,
              cover: `/images/${e.name}.jpg`,
              sign: e.name,
              sub_title1: e.hall,
              sub_title2: (() => {
                switch (Math.floor(Math.random()*4)) {
                  case 0:
                    return `${e.collectNum} 人喜欢`
                  case 1:
                    return `${e.score * 20}%好评`
                  case 2:
                    return `${e.comment} 次评论`
                  case 3:
                    return `售出 ${e.comment} 份`
                  default:
                    return e.window
                }
              })(),
              tags: e.tags
            } as SummaryData)))
          }
        }) ()
      }).then (list => {
        list = list.filter(e => e.sign != '')
        if (list.length > 0){
          //从list中取pageSize条数据出来
          let tempList = [];
          for (let i = 0; i < this.pageSize; i++){
            if (list.length > 0){
              let tempIndex = parseInt(String(Math.random() * 1000)) % list.length;
              tempList.push(list[tempIndex]);
              list.splice(tempIndex, 1);
            }
          }
          this.loadImagesHeight(tempList); //模拟预加载图片，获取图片高度
        }
        else {
          this.loadImagesHeight(list); //处理数据
        }
      }).catch((res)=>{
        console.log("..fail: ", res);
        this.pullLoading = false; //下拉刷新请求完成
        this.bottomLoading = false; //上拉加载更多请求完成
      })
    },
    loadImagesHeight(list: SummaryData[]){
      let count = 0; //用来计数，表示是否所有图片高度已经获取
      list.forEach((item, index)=>{
        //创建图片对象，加载图片，计算图片高度
        const img = new Image();
        img.src = item.cover;
        img.onload = img.onerror = (e)=>{
          count++;
          if (e instanceof Event && e.type == 'load'){ //图片加载成功
            //计算图片缩放后的高度：图片原高度/原宽度 = 缩放后高度/缩放后宽度
            list[index].imgHeight = Math.round(img.height * this.boxWidth / img.width);
            // console.log('index: ', index, ', load suc, imgHeiht: ', list[index].imgHeight);
          }
          else{ //图片加载失败，给一个默认高度50
            list[index].imgHeight = 50;
            console.log("index： ", index, "， 加载报错：", e);
          }
          list[index].heart_clicked = false

          //加载完成最后一个图片高度，开始下一步数据处理
          if (count == list.length){
            this.resolveDataList(list);
          }
        }
      })
    },
    resolveDataList(list: SummaryData[]){ //处理数据
      //下拉刷新，清空原数据
      if (this.pageIndex <= 1){
        this.itemCount = 0;
        this.dataList = [];
        this.lastRowHeights = [0, 0]; //存储每列的最后一行高度清0
      }
/*
      if (list.length >= this.pageSize){
        this.pageIndex++;  //还有下一页
      }
      else{
        this.finished = true; //当前tab类型下所有数据已经加载完成
      }
*/
      this.pageIndex++;

      //合并新老两个数组数据
      this.dataList = [...this.dataList, ...list];
      //判断页面是否有数据
      this.haveData = this.dataList.length > 0 ? 2 : 1;
      this.pullLoading = false; //下拉刷新请求完成
      this.bottomLoading = false; //上拉加载更多请求完成

      // console.log("...datalist: ", this.dataList);
      // console.log("...this.isLoading: ", this.isLoading)

      this.$nextTick(()=>{
        //渲染完成，计算每个item宽高，设置标签坐标定位
        this.setItemElementPosition();
        this.pullLoading = false; //下拉刷新请求完成
        this.bottomLoading = false; //上拉加载更多请求完成
        /*setTimeout(()=>{
        }, 1000)*/
      });
    },
    //获取每个item标签高度，设置item的定位
    setItemElementPosition(){
      let parentEle = document.getElementById('data-list-box');
      let cards = this.$refs.cards as ComponentPublicInstance[];
      // console.log(cards)
      for (let i = this.itemCount; i < cards.length; i++){
        //上一个标签最小高度的列索引
        let curColIndex = this.getMinHeightIndex(this.lastRowHeights);
        let boxTop = this.lastRowHeights[curColIndex] + this.boxMargin;
        let boxLeft = curColIndex * (this.boxWidth + this.boxMargin) + this.boxSidePadding;

        let tempEle: HTMLElement = cards[i]!.$el;
        // console.log(tempEle)
        tempEle.style.left = boxLeft + 'px';
        tempEle.style.top = boxTop + 'px';


        this.lastRowHeights[curColIndex] = boxTop + tempEle.offsetHeight;

        // console.log('i = ', i, ', boxTop: ', boxTop, ', eleHeight: ', tempEle.offsetHeight);
      }

      this.itemCount = cards.length;

      //修改父级标签的高度
      let maxHeight = Math.max(...this.lastRowHeights);
      parentEle!.style.height = maxHeight + 'px';

      // console.log("...boxEles: ", boxEles.length, ", maxH: ", maxHeight);
    },
    //获取数组中最小值的索引
    getMinHeightIndex(arr: [number, number]): number {
      return arr[0] > arr[1] ? 1 : 0;
    }
  }
})
</script>

<!-- web瀑布流(网络图片) -->
<template>
  <div class="flow-box">

    <!-- 列表 -->
    <van-pull-refresh v-model="pullLoading" @refresh="onRefresh" style="min-height: 100vh;"
                      success-text="加载成功" loading-text="加载中...">
      <van-list v-if="haveData==2" v-model="bottomLoading" :finished="finished"
                finished-text="没有更多了" @load="onBottomLoad" :offset="150" :immediate-check="false">
        <div class="data-list-box" id="data-list-box">
          <WaterfallCard v-for="(item, index) in dataList" :item="item" :box-width="boxWidth" :key="index"
          ref="cards" :community="type == 'community'" @card-click="
            $router.push(`/dish/${item.id}`)
          " @heart-click="() => {
              if (item.comment_id)
                like(item.comment_id, index)
            }
          " v-model:heart_clicked="item.heart_clicked"/>
        </div>
      </van-list>
    </van-pull-refresh>
  </div>
</template>

<style scoped>
.flow-box{
  background-color: #ffffff; width: 100vw; height: 100vh;
}
/* 列表数据样式 */
.flow-box {background-color: #f4f4f4}
.flow-box .data-list-box { position: relative; }
.data-list-box {
  height: auto;
  position: absolute; background-color: #f4f4f4;
  border-radius: 5px;
}

</style>