<template>
<div class = "out">
  <div class="box" v-if="sta == 0">
    <ul style="text-align: left; position: absolute; left: 0%; top: 0%">
      <van-button type="primary" @click="back">返回到个人中心</van-button>
      <br>
      <br>
      <div>个人详细信息</div>
      <br>
      <li>user_id&#8194&#8194&#8194&#8194&#8194&#8197 {{ user_id }}</li>
      <li>college&#8194&#8194&#8194&#8194&#8194&#8197 {{ college }}</li>
      <li>stuId&#8194&#8194&#8194&#8194&#8194&#8194&#8194&#8197 {{ stuId }}</li>
      <li>name&#8194&#8194&#8194&#8194&#8194&#8194&#8194 {{ name }}</li>
      <li>已发表评论数 {{ comments }}</li>
      <li>吃过的菜品数 {{ purchase }}</li>
      <br>
      <van-button type="primary" @click="modify">修改个人信息</van-button>
      <van-button type="primary" @click="modifyPassword">修改密码</van-button>
    </ul>
  </div>

  <div v-else-if="sta == 1" class="box2">
    <van-cell-group class="mod" inset>
      <van-field v-model="tname" label="新姓名" required/>
      <van-field v-model="tcollege" label="新学院" required/>
      <van-field v-model="tstuId" label="新学号" placeholder="八位数字" required/>
      <van-button type="primary" @click="backFrom1to0">返回到个人信息页面</van-button>
      <van-button type="primary" @click="finishModify">确认修改</van-button>
    </van-cell-group>
  </div>

  <div v-else class="box2">
    <van-cell-group class="mod" inset>
      <van-field v-model="password" label="密码" placeholder="长度为6-9的字符串" type="password" required/>
      <van-field v-model="passwordAgain" label="再次确认密码" placeholder="再次确认密码" type="password" required/>
      <van-button type="primary" @click="backFrom2to0">返回到个人信息页面</van-button>
      <van-button type="primary" @click="finishModifyPassword">确认修改</van-button>
    </van-cell-group>
  </div>
</div>
</template>

<script lang="ts">
import {generatePost} from "@/utils/protocal";

export default {
  data() {
    return {
      user_id: "",
      college: "",
      stuId: "",
      name: "",
      comments: 0,
      purchase: 0,
      sta: 0, //0默认 1修改信息 2修改密码
      password: "",
      passwordAgain:"",
      tcollege: "",
      tstuId: "",
      tname: "",
    }
  },
  mounted() {
    this.user_id = this.$cookies.get("user_id");
    generatePost("/user/get_info", {user_id: this.user_id}).then((res) => {
      this.college = res.data.college;
      this.tcollege = this.college;
      this.stuId = res.data.stuId;
      this.tstuId = this.stuId;
      this.name = res.data.name;
      this.tname = this.name;
      this.comments = res.data.comments;
      this.purchase = res.data.purchase;
    }, (err) => {
      alert("向后端请求数据时失败");
    })
  },
  methods: {
    back() {
      this.$router.push("/mine");
    },
    modify() {
      this.sta = 1
    },
    finishModify() {
      generatePost("/user/edit_info", {user_id: this.user_id, college: this.tcollege, stuId: this.tstuId, name: this.tname}).then((res) => {
        if (res.data.code == 0) {
          this.college = this.tcollege;
          this.name = this.tname;
          this.stuId = this.tstuId;
          this.sta = 0;
        } else {
          alert('修改失败');
        }
      }, (err) => {
        alert("后端异常")
      })
    },
    modifyPassword() {
      this.sta = 2;
    },
    finishModifyPassword() {
      if (this.password == this.passwordAgain && this.password.length >= 6 && this.password.length <= 9) {
        generatePost("/user/edit_password", {user_id: this.user_id, password: this.password}).then((res) => {
          if (res.data.code == 0) {
            this.password = "";
            this.passwordAgain = "";
            this.sta = 0;
          } else {
            alert('修改失败');
          }
        }, (err) => {
          alert("后端异常")
        })
      } else {
        alert("新密码长度不符合要求或者两次输入密码不一致")
      }
    },
    backFrom1to0() {
      this.tcollege = this.college;
      this.tstuId = this.stuId;
      this.tname = this.name;
      this.sta = 0;
    },
    backFrom2to0() {
      this.password = "";
      this.passwordAgain = "";
      this.sta = 0;
    }
  }
}
</script>

<style scoped>

.out {
  height: 100vh; /* 让容器充满整个屏幕高度 */
  /* 添加背景图片 */
  background-image: url('/ff.jpeg');
  /* 设置背景图片的大小和重复方式 */
  background-size: cover;
  background-repeat: no-repeat;
}

.box {
  text-align: center;
  position: absolute;
  left: 45%;
  top: 40%;
  background-color: white;
  padding: 102px; /* 调整内边距以增加信息的可读性 */
  width: 0px; /* 调整宽度 */
  height: 70px;
}
/*    <ul style="text-align: left; position: absolute; left: 45%; top: 40%">
*/
.box2 {
  text-align: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);

 
}
</style>