import { createRouter, createWebHistory } from "vue-router";
import Home from "@/components/Home.vue";
import Login from "@/components/Login.vue";
import Regis from "@/components/Regis.vue";
import SearchPage from "@/components/SearchPage.vue";
import Comment from "@/components/Comment.vue";
import Dish from "@/components/Dish.vue";
import SubComment from "@/components/subComment.vue";
import CommentForDishes from "@/components/CommentForDishes.vue";
import AdminAddPage from "@/components/AdminAddPage.vue";
import Community from "@/components/Community.vue";
import RankPage from "@/components/RankPage.vue";
import Mine from "@/components/Mine.vue";
import UserInfo from "@/components/UserInfo.vue";
import StarDish from "@/components/StarDish.vue";
import EatenDish from "@/components/EatenDish.vue";
import Statistics from "@/components/Statistics.vue";

const routes = [
    { path: '/dish/:id', component: Dish },
    { path: '/comment/:commentid', component: Comment },
    { path: '/subcomment/:subcommentid', component: SubComment },
    { path: '/commentfordishes/:id', component: CommentForDishes },
    { path: '/commentfordishes/:id/:fromSearch', component: CommentForDishes },
    { path: "/", redirect:"/login" },
    { path: '/search', component: SearchPage},
    { path: '/home', component: Home },
    { path: "/mine", component: Mine },
    { path: '/login', component: Login },
    { path: "/regis", component: Regis },
    { path: '/admin_add', component: AdminAddPage },
    { path: '/community', component: Community },
    { path: '/rank', component: RankPage },
    { path: "/mine/userInfo", component: UserInfo },
    { path: "/mine/starDish", component: StarDish },
    { path: "/mine/eatenDish", component: EatenDish },
    { path: "/statistics", component: Statistics }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
