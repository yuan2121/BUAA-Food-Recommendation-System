<script lang="ts">
import { defineComponent } from 'vue';
import { ref } from 'vue';

import type { SubCommentData } from '@/utils/dataTypes';
import { useRoute } from 'vue-router';
import { showToast } from 'vant';
import { generatePost } from '@/utils/protocal';


export default defineComponent({
    name: "subComment",

    setup(props){
        const route = useRoute();
        
        const subcommentid = ref(props.item.id);
        const commentedid = ref(props.item.commentedid);
        const commenterid = ref(props.item.commenterid);
        const commentedname = ref();
        const commentername = ref();
        const time = ref(props.item.time);
        const content = ref(props.item.content);
        const support = ref(props.item.support);

        const isClick = ref(false);
        const show = ref(false);
        const subinput = ref("");
        return {
            subcommentid,

            commentedid,
            commenterid,
            commentedname,
            commentername,
            time,
            content,
            support,
            
            isClick,
            show,
            subinput,
        };
    },

    props: {
        item: {
            type: Object as () => SubCommentData,
            required: true,
        },
    },

    methods:{
        getcommentedname(){
            generatePost('/user/get_info',{ user_id: this.commentedid }).then((res) => {
                this.commentedname = res.data.name;
            })
        },
        getcommentername(){ 
            generatePost('/user/get_info',{ user_id: this.commenterid }).then((res) => {
                this.commentername = res.data.name;
            })
        },
        addSupport(){
            this.support = this.support + 1;
            this.isClick = true;
            generatePost('/community/support_reply', {
                id: this.subcommentid
            })
        },
        subSupport(){
            this.support = this.support - 1;
            this.isClick = false;
            generatePost('/community/cancel_support_reply', {
                id: this.subcommentid
            })
        },
        getClick(){
            return this.isClick;
        },
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
        changeCommentBar(){
            if (this.$cookies.get("user_id") != null) {
                this.show = !this.show;
            } else {
                showToast("未登录，不可评论")
            }
        },
        getShow(){
            return this.show;
        },
        onClickButton(){
                generatePost('/community/reply_comment', {
                    "comment_id": this.subcommentid,
                    "receiver_id": this.commentedid,
                    "user_id": this.$cookies.get("user_id"),
                    "time": this.getTime(),
                    "content": this.subinput,
                }).then((res) => {
                    if (res.data.code == 0) {
                        this.changeCommentBar();
                        this.subinput = "";
                        alert("评论成功！");
                    }
                })
        }
    },
    created() {
        this.getcommentedname();
        this.getcommentername();
    },
})
</script>

<template>
    <div style="display:flex; position:relative" class="top">
        <div class="user-name" style="font-size: 15px">{{ commentername }} 回复 {{ commentedname }}</div>
        <div class="support">
            <van-icon v-if="getClick()" name="good-job"  @click="subSupport()">{{ support }}</van-icon>
            <van-icon v-else name="good-job-o" @click="addSupport()">{{ support }}</van-icon>
        </div>
    </div>
    <div class="time" style="font-size: 10px">{{ time }}</div>
    <div class="content">{{ content }}</div>
    <div class="comment-icon" style="text-align: right;">
        <van-icon name="comment-o" @click="changeCommentBar()"></van-icon>
    </div>
    <div class="subcomment-field" v-if="show">
        <van-cell-group inset>
        <!-- 输入任意文本 -->
            <van-field
                v-model="subinput"
                rows="2"
                autosize
                label="评论"
                type="textarea"
                maxlength="50"
                placeholder="请输入您的评论"
                show-word-limit>
            </van-field>
        </van-cell-group>
        <div style="text-align: right;" class="my-button">
            <van-button size="small" type="primary" @click="onClickButton">提交评论</van-button>
        </div>
    </div>
</template>

<style scoped>
    .top{
        margin-left:40px;
        margin-top: 20px;
    }
    .support{
        margin-left:auto;
        margin-right:50px;
    }
    .time{
        position: relative;
        margin-left:50px
    }
    .content{
        position: relative;
        margin-left:50px;
        margin-top :5px;
        width:60%;
        word-break:break-all;
        word-wrap: break-word;
    }
    .comment-icon{
        margin-right:50px;
    }

    .subcomment-field{
        margin-left: 50px;
        margin-right: 70px;
    }

    .my-button{
        margin-right:20px;
    }
</style>