<script lang="ts">
import { ref } from 'vue';

import { defineComponent } from 'vue';
import Comment from './Comment.vue';

import type { CommentData } from '@/utils/dataTypes';
import { useRoute } from 'vue-router';
import { showToast } from 'vant';
import { generatePost } from '@/utils/protocal';
import type { SubCommentData } from '@/utils/dataTypes';
import type { HallAndWindow } from '@/utils/dataTypes';

export default defineComponent ({
    name: "dish",
    components: { Comment },

    setup(){
        const route = useRoute();

        const id = route.params.id as string;
        const name = ref("");
        const image = ref();
        const hall = ref("");
        const tags = ref([] as String[]);
        const purchase = ref();
        const comment = ref();
        const likes = ref();
        const score = ref();
        const comments = ref([] as CommentData[]);
        const window = ref();
        const type = ref();

        const isClick = ref(false);
        const isClickForHall = ref(false);
        const isClickForWindow = ref(false);
        const likeslist = ref([] as number[]);
        const halllist = ref([] as string[]);
        const windowlist = ref([] as HallAndWindow[]);

        const price = ref(0)

        return {
            id,
            name,
            image,
            hall,
            tags,
            price,
            purchase,
            comment,
            likes,
            score,
            comments,
            window,
            type,
            isClick,
            isClickForHall,
            isClickForWindow,
            likeslist,
            halllist,
            windowlist
        }
    },

    methods: {
        init() {
            generatePost("/dish/get_detail", { dish_id: this.id }).then(async (res) => {
                this.name = res.data.summary.name;
                this.hall = res.data.summary.hall;
                this.purchase = res.data.summary.purchase;
                this.price = res.data.summary.price;
                const temp = res.data.comments.map(i => {
                    return generatePost('/community/get_detail', { id: i }).then((res) => {
                        return {
                            id: i,
                            commentname: res.data.summary.user_id,
                            rate: res.data.summary.score,
                            time: res.data.time,
                            support: res.data.summary.likes,
                            content: res.data.full_text,
                            subcomments: res.data.comments.map(e => {
                                return {
                                    id: e.id,
                                    commentedid: e.receiver_id,
                                    commenterid: e.user_id,
                                    time: e.time,
                                    support: e.likes,
                                    content: e.full_text,
                                } as SubCommentData
                            }),
                        } as CommentData
                    })
                })
                this.comments = await Promise.all(temp)
                this.comment = res.data.summary.comment;
                this.tags = res.data.summary.tags;
                this.likes = res.data.summary.collectNum;
                this.score = res.data.summary.score;
                this.window = res.data.summary.window;
                this.type = res.data.summary.type;
            }) 
            generatePost('/user/collect', { user_id: this.$cookies.get("user_id"), }).then(async (res) => {
                this.likeslist = res.data.dishes.map(u => {
                    return u.id;
                })
            })
            generatePost('/user/collect_hall', { user_id: this.$cookies.get("user_id"), }).then(async (res) => {
                this.halllist = res.data.halls;
            })
            generatePost('/user/collect_window', { user_id: this.$cookies.get("user_id"), }).then(async (res) => {
                this.windowlist = res.data.windows.map(u => {
                    return {
                        hall: u.hall,
                        window: u.window
                    } as HallAndWindow
                });
            })
        },
        addComment(){
            if (this.$cookies.get("user_id") != null) {
                this.$router.push('/commentfordishes/' + this.id);
            } else {
                showToast("未登录，不可评论")
            }
        },
        addlikes(){
            if (this.$cookies.get("user_id") != null) {
                this.likes = this.likes + 1;
                this.isClick = !this.isClick;
                generatePost('/user/save_collect', {
                    user_id: this.$cookies.get("user_id"),
                    dish_id: this.id,
                }).then((res) => {
                    generatePost('/user/collect', { user_id: this.$cookies.get("user_id"), }).then(async (result) => {
                        this.likeslist = result.data.dishes.map(u => {
                            return u.id;
                        })
                    })
                })
            } else {
                showToast("未登录，不可收藏")
            }
        },
        sublikes(){
            if (this.$cookies.get("user_id") != null) {
                this.likes = this.likes - 1;
                this.isClick = !this.isClick;
                generatePost('/user/delete_collect', {
                    user_id: this.$cookies.get("user_id"),
                    dish_id: this.id,
                }).then((res) => {
                    generatePost('/user/collect', { user_id: this.$cookies.get("user_id"), }).then(async (result) => {
                        this.likeslist = result.data.dishes.map(u => {
                            return u.id;
                        })
                    })
                })
            } else {
                showToast("未登录，不可取消收藏")
            }
        },
        addlikehall() {
            if (this.$cookies.get("user_id") != null) {
                generatePost('/user/save_collect_hall', {
                    user_id: this.$cookies.get("user_id"),
                    hall: this.hall,
                }).then((res) => {
                    generatePost('/user/collect_hall', { user_id: this.$cookies.get("user_id"), }).then(async (result) => {
                        this.halllist = result.data.halls;
                    })
                })
            } else {
                showToast("未登录，不可收藏")
            }
        },
        sublikehall() {
            if (this.$cookies.get("user_id") != null) {
                generatePost('/user/delete_collect_hall', {
                    user_id: this.$cookies.get("user_id"),
                    hall: this.hall,
                }).then((res) => {
                    generatePost('/user/collect_hall', { user_id: this.$cookies.get("user_id"), }).then(async (result) => {
                        this.halllist = result.data.halls;
                    })
                })
            } else {
                showToast("未登录，不可取消收藏")
            }
        },
        addlikewindow() {
            if (this.$cookies.get("user_id") != null) {
                generatePost('/user/save_collect_window', {
                    user_id: this.$cookies.get("user_id"),
                    hall: this.hall,
                    window: this.window,
                }).then((res) => {
                    generatePost('/user/collect_window', { user_id: this.$cookies.get("user_id"), }).then(async (result) => {
                        this.windowlist = result.data.windows.map(u => {
                            return {
                                hall: u.hall,
                                window: u.window
                            } as HallAndWindow
                        });
                    })
                })
            } else {
                showToast("未登录，不可收藏")
            }
        },
        sublikewindow() {
            if (this.$cookies.get("user_id") != null) {
                generatePost('/user/delete_collect_window', {
                    user_id: this.$cookies.get("user_id"),
                    hall: this.hall,
                    window: this.window,
                }).then((res) => {
                    generatePost('/user/collect_window', { user_id: this.$cookies.get("user_id"), }).then(async (result) => {
                        this.windowlist = result.data.windows.map(u => {
                            return {
                                hall: u.hall,
                                window: u.window
                            } as HallAndWindow
                        });
                    })
                })
            } else {
                showToast("未登录，不可取消收藏")
            }
        },
    },

    created() {
        this.init()
    },

    computed: {
        judge() {
            return this.likeslist.includes(parseInt(this.id));
        },
        judgeforhall() {
            return !this.halllist.includes(this.hall);
        },
        judgeforwindow() {
            return !this.windowlist.some(e => {
                return e.hall == this.hall && e.window == this.window;
            });
        },
        scoreDiv5() {
            return this.score / 5
        }
    }
})
</script>
<template>
    <van-nav-bar title="菜品详情" left-arrow @click-left="$router.back()"/>
    <img :src="`/images/${ name }.jpg`" :style="{width: 'auto', height: '250px'}" class="image"/>
    <div class="description">
        <h2 class="name">{{ name }}</h2>
        <div class="score">
          <span class="data-score-text">{{this.price}} 元</span>
        </div>
        <div class="score">
          <van-rate v-model="scoreDiv5" :count="1" readonly allow-half />
          <span class="data-score-text">{{score.toFixed(2)}}</span>
        </div>
        <div class="purchase">总购买{{ purchase }}次</div>
    </div>
    <div class="box">
        <div>
            <van-tag v-if="judgeforhall" type="primary" @click="addlikehall()">{{ hall }}</van-tag>
            <van-tag v-else type="success" @click="sublikehall()">{{ hall }}</van-tag>
        </div>
        <div>
            <van-tag v-if="judgeforwindow" type="primary" @click="addlikewindow()">{{ window }}</van-tag>
            <van-tag v-else type="success" @click="sublikewindow()">{{ window }}</van-tag>
        </div>
        <div v-if="window != type">
            <van-tag type="primary">{{ type }}</van-tag>
        </div>
        <div v-for="item in tags">
            <van-tag type="primary">{{ item }}</van-tag>
        </div>
        <div class="likes">
            <van-icon v-if="judge" name="star" @click="sublikes()">收藏({{ likes }})</van-icon>
            <van-icon v-else name="star-o" @click="addlikes()">收藏({{ likes }})</van-icon>
        </div>
    </div>
    <div style="display:flex; position:relative" class="commentsection">
        <div><h2 class="title">评论区({{ comment }})</h2></div>
        <div class="comment">
            <van-button size="small" type="primary" @click="addComment">发表评论</van-button>
        </div>
        
    </div>
    <div><Comment v-for="item in comments" :item="item"/></div>
</template>

<style scoped>
    .image{
        display: block; 
        margin: 0 auto;
    }
    .box {
        display: flex;
        justify-content: center;
    }
    .title{
        margin-left:20px
    }
    .description{
        display: flex;
        align-items: center;
        justify-content: center;
        margin-left: 20px;
        margin-top: 10px;
    }
    .purchase{
        margin-left: 20px;
        margin-top: 5px;
    }
    .likes{
        margin-left:60px;
    }
    .score{
        margin-left: 20px;
        margin-top: 5px;
    }
    .comment{
        margin-left:auto;
        margin-right:30px;
        margin-top:20px;
    }

</style>