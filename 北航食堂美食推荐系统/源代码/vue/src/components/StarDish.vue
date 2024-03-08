<template>
  <div class="box">
    <van-button type="primary" @click="back">返回到个人中心</van-button>
    <div>收藏过的菜品</div>
    <van-list
        v-model:loading="loading"
        :finished="finished"
        finished-text="没有更多了"
        @load="onLoad"
    >
      <van-cell v-for="(item, index) in list" :key="item.id">
        <template #title >
          <img :src="`/images/${item.name}.jpg`" :alt="item.name" height="200" width="200"/>
          菜名：{{ item.name }}
          所在食堂：{{ item.hall }}
          所在窗口：{{ item.window }}
          类型： {{ item.type }}
          评分：{{ item.score }}
          <van-button type="primary" @click="cancelStar(item.id, index)">取消收藏</van-button>
          <van-button type="primary" @click="gotoDish(item.id)">查看详情</van-button>
        </template>
      </van-cell>
    </van-list>
  </div>
</template>

<script lang="ts">
import {generatePost} from "@/utils/protocal";
import {ref} from 'vue';

interface Dish {
  id: number,
  name: string,
  hall: string,
  window: string,
  type: string,
  tags: Array<string>,
  purchase: number,
  comment: number,
  collectNum: number,
  score: number
}

export default {
  setup() {
    const list = ref([] as Array<Dish>);
    const loading = ref(false);
    const finished = ref(false);

    return {
      list,
      loading,
      finished,
    };
  },
  methods: {
    onLoad() {
      generatePost("/user/collect", {user_id: this.$cookies.get("user_id")}).then((res) => {
        let dish = res.data.dishes;
        for (let i = 0; i < 10 && this.list.length < dish.length; i++) {
          this.list.push(dish[dish.length - 1 - this.list.length])
        }
        this.loading = false;
        if (this.list.length == dish.length) {
          this.finished = true;
        }
      }, (err) => {
        alert("向后端请求数据时发生错误");
      })
    },
    back() {
      this.$router.back();
    },
    cancelStar(id: number, index: number) {
      generatePost("/user/delete_collect", {user_id: this.$cookies.get("user_id"), dish_id: id}).then((res) => {
        this.list.splice(index, 1);
      }, (err) => {
        alert("删除失败")
      })
    },
    gotoDish(id: number) {
      this.$router.push(`/dish/${id}`);
    }
  }
}
</script>

<style scoped>
.box {
  text-align: center;
  height: 100vh; /* 让容器充满整个屏幕高度 */
  /* 添加背景图片 */
  background-image: url('/ff.jpeg');
  /* 设置背景图片的大小和重复方式 */
  background-size: cover;
  background-repeat: no-repeat;
}
</style>
