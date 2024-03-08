<script lang="ts">
import { defineComponent } from 'vue';
import subComment from './subComment.vue';
import { ref } from 'vue';

import type { CommentData } from '@/utils/dataTypes';
import { useRoute } from 'vue-router';
import { showToast } from 'vant';
import { generatePost } from '@/utils/protocal';

export default defineComponent({
    name: "Comment",
    components: { subComment },

    setup(props){
        const route = useRoute()

        const commentid = ref(props.item.id);
        const name = ref();
        const commentname = ref(props.item.commentname);
        const time = ref(props.item.time);
        const rate = ref(props.item.rate);
        const support = ref(props.item.support);
        const subcomments = ref(props.item.subcomments);
        const content = ref(props.item.content);
        
        const isClick = ref(false);
        const show = ref(false);
        const subinput = ref("")
        
        return {
            commentid,
            name,

            commentname,
            time,
            content,
            rate,
            support,
            subcomments,
            
            isClick,
            show,
            subinput,
        };
    },

    props: {
        item: {
            type: Object as () => CommentData,
            required: true
        },
    },

    methods:{
        getname(){
            generatePost('/user/get_info',{ user_id: this.commentname }).then((res) => {
                this.name = res.data.name;
            })
        },
        addSupport(){
            this.support = this.support + 1;
            this.isClick = true;
            generatePost('/community/support', {
                id: this.commentid,
            })
        },
        subSupport(){
            this.support = this.support - 1;
            this.isClick = false;
            generatePost('/community/cancel_support', {
                id: this.commentid,
            })
        },
        getClick(){
            return this.isClick;
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
                generatePost('/community/reply_comment', {
                    "comment_id": this.commentid,
                    "receiver_id": this.commentname,
                    "user_id": this.$cookies.get("user_id"),
                    "time": this.getTime(),
                    "content": this.subinput,
                }).then((res) => {
                    if (res.data.code == 0){
                        this.changeCommentBar();
                        this.subinput = "";
                        alert("评论成功！");
                    }
                })
        }
    },
    created() {
        this.getname();
    },
})
</script>

<template>
    <div style="display:flex; position:relative" class="top">
        <div class="user-name" style="font-size: 20px">{{ name }}</div>
        <div class="rate"><van-rate v-model="rate" readonly></van-rate></div>
        <div class="support">
            <van-icon v-if="getClick()" name="good-job"  @click="subSupport()">{{ support }}</van-icon>
            <van-icon v-else name="good-job-o" @click="addSupport()">{{ support }}</van-icon>
        </div>
    </div>
    <div class="time" style="font-size: 10px">{{ time }}</div>
    <div class="content">{{ content }}</div>
    <div class="commenticon" style="text-align: right;">
        <van-icon name="comment-o" @click="changeCommentBar()"></van-icon>
    </div>
    <div v-if="show" class="textarea">
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
            <van-button size="small" type="primary" @click="onClickButton()">提交评论</van-button>
        </div>
    </div>
    <div>
        <subComment v-for="(item, index) in subcomments" :item="item" :key="index"></subComment>
    </div>
</template>

<style scoped>
    .top{
        margin-left:20px;
        margin-top: 20px;
    }
    .rate{
        margin-left:10px;
    }
    .support{
        margin-left:auto;
        margin-right:30px;
    }
    .time{
        position: relative;
        margin-left:40px
    }
    .content{
        position: relative;
        margin-left:40px;
        margin-top :5px;
        width:75%;
        word-break:break-all;
        word-wrap: break-word;
    }
    .commenticon{
        margin-right:30px;
    }

    .textarea{
        margin-left: 30px;
        margin-right: 50px;
    }

    .my-button{
        margin-right:30px;
    }
</style>