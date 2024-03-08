import { createApp } from 'vue'
import App from './App.vue'

import {
    Button,
    Tabbar,
    TabbarItem,
    Swipe,
    SwipeItem,
    NavBar,
    PullRefresh,
    List,
    Search,
    Icon,
    Tag,
    Divider,
    Col, Row,
    Cell, CellGroup,
    Empty,
    DropdownMenu, DropdownItem,
    Checkbox, CheckboxGroup,
    Grid, GridItem,
    Loading,
    Sticky,
    Rate,
    Field,
    Notify, Dialog, Tab, Tabs, ConfigProvider,
    Space
} from "vant";
import 'vant/lib/index.css';
import router from "@/router";
import VueCookies from "vue-cookies";

const app = createApp(App)
app.use(Button).use(Tabbar).use(TabbarItem)
   .use(Swipe).use(SwipeItem).use(NavBar).use(PullRefresh)
   .use(List).use(Search).use(Icon).use(Tag).use(Divider)
   .use(Col).use(Row).use(Cell).use(CellGroup)
   .use(Empty).use(DropdownMenu).use(DropdownItem)
   .use(Checkbox).use(CheckboxGroup).use(Grid).use(GridItem)
   .use(Loading).use(Sticky).use(Rate).use(Field)
   .use(Notify).use(Dialog).use(Tab).use(Tabs)
app.use(ConfigProvider).use(Space)
app.use(router)
app.use(VueCookies)

// 自定义全局函数
declare module '@vue/runtime-core' {
    interface ComponentCustomProperties {
        $getUser: () => string,
        $isAdmin: () => boolean,
        $isGuest: () => boolean
    }
}
app.config.globalProperties.$getUser = () => { return app.config.globalProperties.$cookies.get('user_id') ?? '' }
app.config.globalProperties.$isAdmin = () => ( app.config.globalProperties.$getUser() == 'admin' )
app.config.globalProperties.$isGuest = () => ( app.config.globalProperties.$getUser() == '' )

app.mount('#app')
