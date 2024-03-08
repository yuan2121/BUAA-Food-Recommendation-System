<template>
  <div class="regis">
    <van-cell-group class="box" inset>
      <div>北航食堂菜品推荐系统注册页面</div>
      <van-field v-model="user_info.user_id" label="用户id" placeholder="长度为6-9的字符串" required/>
      <van-field v-model="user_info.password" label="密码" placeholder="长度为6-9的字符串" type="password" required/>
      <van-field v-model="passwordAgain" label="确认密码" placeholder="确认密码" type="password" required/>
      <van-field v-model="user_info.name" label="姓名" required/>
      <van-field v-model="user_info.college" label="学院" required/>
      <van-field v-model="user_info.stuId" label="学号" placeholder="八位数字" required/>
      <van-button type="primary" @click="tryToRegis">确认注册</van-button>
    </van-cell-group>
  </div>
</template>

<script lang="ts">
import {generatePost} from "@/utils/protocal";

export default {
  data() {
    return {
      user_info: {
        user_id: "",
        password: "",
        name: "",
        college: "",
        stuId: ""
      },
      passwordAgain: ""
    }
  },
  methods: {
    tryToRegis() {
      if (this.isLegal()) {
        generatePost("/user/register", this.user_info).then(res => {
          if (res.data.code == 0) {
            alert("注册成功，跳转到登陆页面");
            this.$router.push("/login");
          } else {
            alert("注册失败，user_id已被使用");
          }
        }, err => {
          alert("向后端请求时失败");
        })
      } else {
        alert("请检查输入是否符合要求");
      }
    },
    isLegal() {
      return this.user_info.password == this.passwordAgain &&
          this.user_info.user_id.length >= 6 && this.user_info.user_id.length <= 9 &&
          this.user_info.password.length >= 6 && this.user_info.password.length <= 9 &&
          this.user_info.stuId.length == 8;
    }
  }
}
</script>
<style scoped>
.box {
  text-align: center;
  border: 1px solid black;
  border-radius: 3px;
  box-shadow: 0px 0px 7px #cdcdcd;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.regis {
  width: 100%;
  min-height: 100vh;
  background-color: #f7f7f9;
  background-repeat: no-repeat;
  background-size: cover;
  background-attachment: fixed;
  background-image: url("/hengping.jpg");
}

@media only screen and (orientation: portrait) {

  .regis {
    background-repeat: no-repeat;
    background-size: cover;
    background-attachment: fixed;
    background-image: url("/shuping.jpg");
  }

}
</style>