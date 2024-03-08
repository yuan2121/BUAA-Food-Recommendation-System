<script lang="ts">
import { ref } from 'vue';
import axios from 'axios';
import {defineComponent} from 'vue'
import { showToast } from 'vant';
import { generatePost } from '@/utils/protocal';
import {useRoute} from "vue-router";

export default defineComponent({
  name: "CommentForDishes",

  setup() {
    const route = useRoute()

    const content = ref("");
    const rate = ref(route.params.fromSearch ?? 0);
    const time = ref("");
    const name = ref();

    return {
        content,
        rate,
        time,
        name,
      }
  },
  
  methods:{
    getTime(){
      const val = new Date();
      const year = val.getFullYear()
      const month = (val.getMonth() + 1).toString().padStart(2, '0')
      const day = val.getDate().toString().padStart(2, '0')
      const hour = val.getHours().toString().padStart(2, '0')
      const mm = val.getMinutes().toString().padStart(2, '0')
      const ss = val.getSeconds().toString().padStart(2, '0')
      return year + "-" + month + "-" + day + " " + hour + ":" + mm + ":" + ss
    },
    onClickButton(){
        generatePost('/community/post_comment', {
            user_id: this.$cookies.get("user_id"),
            dish_id: this.$route.params.id,
            time: this.getTime(),
            score: this.rate,
            content: this.content,
        }).then((res) => {
          if (res.data.code == 0) {
            alert("评论成功！")
            if (this.$route.params.fromSearch) {
              this.$router.replace('/dish/' + this.$route.params.id)
            } else {
              this.$router.back()
            }
          } else {  
            console.log(res.data.code)
            showToast("评论失败")
          }
        })
    }
  },
});

</script>

<template>
    <van-nav-bar title="发表评论" left-arrow @click-left="$router.back()"/>
    <div style="display:flex; position:relative" class="top">
        <div class="title">评分</div>
        <div class="rate"><van-rate v-model="rate"/></div>
    </div>
    <div class="textarea">
      <van-cell-group inset>
          <!-- 输入任意文本 -->
          <van-field
              v-model="content"
              rows="2"
              autosize
              label="评论"
              type="textarea"
              maxlength="50"
              placeholder="请输入您对这道菜品的评价"
              show-word-limit>
          </van-field>
      </van-cell-group>
    </div>  
    <div style="text-align: right;" class="my-button">
        <van-button size="small" type="primary" @click="onClickButton()">提交评论</van-button>
    </div>
</template>

<style scoped>

    .top{
      margin-top: 20px;
      margin-left: 15px;
    }

    .title{
      margin-left: 30px;
    }
    .rate{
      margin-left: 70px;
    }

    .my-button{
        position: relative;
        margin-right: 30px
    }

    .textarea{
        margin-left: 15px;
        margin-right: 30px;
    }
</style>