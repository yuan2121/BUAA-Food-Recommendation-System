<script lang="ts">
import {defineComponent} from 'vue'
import BottomBar from "./BottomBar.vue";

export default defineComponent({
  name: "Home",
  components: {BottomBar},
  data() {
    return {
      user_id: "id尚未刷新"
    }
  },
  mounted() {
    this.user_id = this.$cookies.get("user_id") == undefined ||
    this.$cookies.get("user_id") == "" ? "游客" : this.$cookies.get("user_id");
  },
  methods: {
    toUserInfo() {
      if (this.$cookies.get("user_id") == undefined || this.$cookies.get("user_id") == "") {
        alert("游客状态下无法查看个人信息");
      } else {
        this.$router.push("/mine/userInfo");
      }
    },
    toStarDish() {
      if (this.$cookies.get("user_id") == undefined || this.$cookies.get("user_id") == "") {
        alert("游客状态下无法查看收藏菜品");
      } else {
        this.$router.push("/mine/starDish");
      }
    },
    toEatenDish() {
      if (this.$cookies.get("user_id") == undefined || this.$cookies.get("user_id") == "") {
        alert("游客状态下无法查看吃过的菜品");
      } else {
        this.$router.push("/mine/eatenDish");
      }
    },
    toAdmin() {
      this.$router.push("/admin_add");
    },
    quit() {
      this.$cookies.set("user_id", "");
      this.$router.push("/login");
    }
  }
})
</script>

<template>
  <div id="box">
    <div id="title">个人中心</div>
    <br>
    <div id = "myuser"> user_id : {{ user_id }}</div>
    <br>
    <van-divider/>
    <van-space>
      <van-icon name="user-o" @click="toUserInfo">个人信息</van-icon>
      <van-icon name="todo-list-o" @click="toEatenDish">吃过的菜</van-icon>
      <van-icon name="star-o" @click="toStarDish">收藏菜品</van-icon>
      <van-icon v-if="$isAdmin()" name="manager-o" @click="toAdmin">内容管理</van-icon>
    </van-space>
    <br>
    <br>
    <van-divider/>
    <van-button type="primary" @click="quit">退出登录</van-button>
  </div>
  <BottomBar active="my"/>
</template>

<style scoped>

#box {
  text-align: center;
  height: 100vh; /* 让容器充满整个屏幕高度 */
  /* 添加背景图片 */
  background-image: url('/ff.jpeg');
  /* 设置背景图片的大小和重复方式 */
  background-size: cover;
  background-repeat: no-repeat;
}

#title {
  text-align: center;
  font-size: 30px; 
}

#myuser {
  text-align: center;
  font-size: 20px; 
}

.van-icon {
  font-size: 30px; /* 调整图标按钮的大小 */
  margin-right: 50px;
  /* 可以针对特定图标进行样式调整 */
  /* 例如，个人信息、吃过的菜、收藏菜品的图标 */
}

.van-button {
  padding: 15px 20px; /* 调整按钮的内边距 */
  font-size: 18px; /* 调整按钮文字大小 */
}

.van-icon {
  font-size: 24px; /* 调整图标按钮的大小 */
}

</style>