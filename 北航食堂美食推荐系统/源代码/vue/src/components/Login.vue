<style>
	.center {
		width: 1700px;
		height: 900px;
		background-image: url('https://gd-hbimg.huaban.com/9165dc3c0f8279ae5402d1f47212847bff68b49f3cb547-QEli8R');
		background-size: 100% 100%;
		background-repeat: no-repeat;
		display: flex;
		align-items: center;
		justify-content: center;
		flex-direction: column;
	}
 
	h1 {
		font-size: 30px;
		color: black;
	}
 
	.logon {
		background-color: #fff;
		border-radius: 10px;
		box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22);
		/* position: relative;
		overflow: hidden; */
		width: 768px;
		max-width: 100%;
		min-height: 480px;
		margin-top: 20px;
		display: flex;
		background: -webkit-linear-gradient(right, #4284db, #29eac4);
	}
 
	.overlaylong {
		border-radius: 10px 0 0 10px;
		width: 50%;
		height: 100%;
		background-color: #fff;
		display: flex;
		align-items: center;
		justify-content: center;
	}
 
	.overlaylongleft {
		border-radius: 0px 10px 10px 0px;
		width: 50%;
		height: 100%;
		background-color: #fff;
		transform: translateX(100%);
		transition: transform 0.6s ease-in-out;
		display: flex;
		align-items: center;
		justify-content: center;
	}
 
	.overlaylongright {
		border-radius: 10px 0 0 10px;
		width: 50%;
		height: 100%;
		background-color: #fff;
		transform: translateX(0%);
		transition: transform 0.6s ease-in-out;
		display: flex;
		align-items: center;
		justify-content: center;
	}
 
	.overlaytitle {
		border-radius: 0px 10px 10px 0px;
		width: 50%;
		height: 100%;
		background-color: rgba(0, 0, 0, 0);
		display: flex;
		align-items: center;
		justify-content: center;
	}
 
 
	.overlaytitleH2 {
		font-size: 30px;
		color: #fff;
		margin-top: 20px;
	}
 
	.overlaytitleP {
		font-size: 15px;
		color: #fff;
		margin-top: 20px;
	}
 
	.overlaytitleleft {
		border-radius: 0px 10px 10px 0px;
		width: 50%;
		height: 100%;
		background-color: rgba(0, 0, 0, 0);
		display: flex;
		align-items: center;
		justify-content: center;
		transform: translateX(0%);
		transition: transform 0.6s ease-in-out;
	}
 
	.overlaytitleright {
		border-radius: 0px 10px 10px 0px;
		width: 50%;
		height: 100%;
		background-color: rgba(0, 0, 0, 0);
		display: flex;
		align-items: center;
		justify-content: center;
		transform: translateX(-100%);
		transition: transform 0.6s ease-in-out;
	}
 
	.overlaytitle-Signin {
		display: flex;
		align-items: center;
		justify-content: center;
		flex-direction: column;
	}
 
	.overlaytitle-Signup {
		display: flex;
		align-items: center;
		justify-content: center;
		flex-direction: column;
	}
 
	.buttongohs {
		width: 180px;
		height: 40px;
		border-radius: 50px;
		border: 1px solid #fff;
		color: #fff;
		font-size: 15px;
		text-align: center;
		line-height: 40px;
		margin-top: 40px;
	}
 
	.overlaylongH2 {
		font-size: 25px;
		color: black;
		/* width: 250px; */
	}
 
	.overlaylong-Signin {
		display: flex;
		align-items: center;
		justify-content: center;
		flex-direction: column;
	}
 
	.overlaylong-Signup {
		display: flex;
		align-items: center;
		justify-content: center;
		flex-direction: column;
	}
 
	input {
		background-color: #eee;
		border: none;
		padding: 12px 15px;
		margin: 10px 0;
		width: 240px;
	}
	h3{
		font-size: 10px;
		margin-top: 10px;
		cursor: pointer;
	}
	.inupbutton{
		background-color: #29eac4;
		border: none;
		width: 180px;
		height: 40px;
		border-radius: 50px;
		font-size: 15px;
		color: #fff;	
		text-align: center;
		line-height: 40px;
		margin-top: 30px;
	}
</style>
 
<template>
	<div class="center">
		<h1>北航食堂菜品推荐系统</h1>
		<div class="logon">
			<div :class="overlaylong">
				<div class="overlaylong-Signin" v-if="disfiex == 0">
					<h2 class="overlaylongH2">Sign in</h2>
					<input type="text" v-model="user_info.user_id" placeholder="user">
					<input type="text" v-model="user_info.password" placeholder="password">
					<h3>Forgot your password?</h3>
					<button class="inupbutton" @click="login">Sign in</button>
				</div>
				<div class="overlaylong-Signup" v-if="disfiex == 1">
					<h2 class="overlaylongH2">Register Your Account</h2>
					<van-cell-group class="box" inset>
          <van-field v-model="user_regisInfo.user_id" label="用户id" placeholder="长度为1-12的字符串" required />
          <van-field v-model="user_regisInfo.password" label="密码" placeholder="长度为6-9的字符串" type="password" required />
          <van-field v-model="passwordAgain" label="再次确认密码" placeholder="再次确认密码" type="password" required />
          <van-field v-model="user_regisInfo.name" label="姓名" required />
          <van-field v-model="user_regisInfo.college" label="学院" required />
          <van-field v-model="user_regisInfo.stuId" label="学号" placeholder="八位数字" required />
          </van-cell-group>
					<button class="inupbutton" @click="regis">Sign up</button>
				</div>
 
			</div>
			<div :class="overlaytitle">
				<div class="overlaytitle-Signin" v-if="disfiex == 0">
					<h2 class="overlaytitleH2">Hello,Friend!</h2>
					<p class="overlaytitleP">
						Enter your personal details and start journey with us
					</p>
					<div class="buttongohs" @click="Signin">Sign up</div>
				</div>
				<div class="overlaytitle-Signup" v-if="disfiex == 1">
					<h2 class="overlaytitleH2">Welcome Back!</h2>
					<p class="overlaytitleP"> 注册您的账户以此来体验北航菜品推荐系统~</p>
					<div class="buttongohs" @click="Signup">返回到登陆界面</div>
				</div>
			</div>
		</div>
 
	</div>
</template>



<script>
import {generatePost} from "@/utils/protocal";
	export default {
		data() {
			return {
        user_info: {
          user_id: '',
          password: ''
        },
        user_regisInfo: {
          user_id: "",
          password: "",
          name: "",
          college: "",
          stuId: ""
        },
        passwordAgain: "",
				overlaylong: 'overlaylong',
				overlaytitle: 'overlaytitle',
				disfiex: 0
			}
		},
		methods: {
			Signin() {
				this.overlaylong = "overlaylongleft"
				this.overlaytitle = "overlaytitleright"
				setTimeout(() => {
					this.disfiex = 1
				}, 200)
			},
			Signup() {
				this.overlaylong = "overlaylongright"
				this.overlaytitle = "overlaytitleleft"
 
				setTimeout(() => {
					this.disfiex = 0
				}, 200)
			},
      login() {
        generatePost("/user/login", this.user_info).then(res => {
          if (res.data.code == 0) {
            this.$cookies.set("user_id", this.user_info.user_id);
            this.$router.push('/home');
          } else if (res.data.code == 1) {
            alert("用户名不存在，请检查输入是否正确")
          } else {
            alert("密码输入错误，请重新检查")
          }
        }, err => {
          alert("请求后端数据失败")
        })
      },
      regis() {
        if (this.isLegal()) {
          generatePost("/user/register", this.user_regisInfo).then(res => {
            if (res.data.code == 0) {
              this.$cookies.set("user_id", this.user_regisInfo.user_id);
              alert("注册成功，跳转到主页");
              this.$router.push("/home");
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
        return this.user_regisInfo.password == this.passwordAgain &&
            this.user_regisInfo.user_id.length >= 1 && this.user_regisInfo.user_id.length <= 12 &&
            this.user_regisInfo.password.length >= 6 && this.user_regisInfo.password.length <= 9 &&
            this.user_regisInfo.stuId.length == 8;
      }
		}
	}
</script>