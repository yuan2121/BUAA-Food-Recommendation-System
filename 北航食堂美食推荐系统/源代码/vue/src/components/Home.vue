<script lang="ts">
import {defineComponent, ref} from 'vue'
import BottomBar from "./BottomBar.vue";
import HomeSwipe from "./HomeSwipe.vue";
import SearchBar from "@/components/SearchBar.vue";
import Waterfall from "@/components/Waterfall.vue";
import RankBoard from "@/components/RankBoard.vue";
import type {DishSummary, RankItem} from "@/utils/dataTypes";
import {generatePost, isMorning} from "@/utils/protocal";
import {showNotify} from "vant";


export default defineComponent({
  name: "Home",
  components: {RankBoard, Waterfall, SearchBar, HomeSwipe, BottomBar},
  setup() {
    const recommendation = ref<Array<RankItem>>([])
    const rank = ref<Array<RankItem>>([])
    return {
      recommendation,
      rank
    }
  },
  methods: {
    searchRedirect() {
      this.$router.push('/search')
    }
  },
  created() {
    if (!this.$isGuest()) {
      generatePost('/search/recommendation', {
        user_id: this.$getUser(),
        is_morning: isMorning(),
        n: 3
      }).then(response => {
        this.recommendation = (response.data?.dishes as DishSummary[] ?? []).map(e => ({
          name: e.name, link: `/dish/${e.id}`
        }))
      }, err => {
        showNotify(`发生错误：${err}`)
      })
    }

    generatePost('/search/rank', {
      order: 'sales',
      n: 3
    }).then(response => {
      this.rank = (response.data?.dishes as DishSummary[] ?? []).map(e => ({
        name: e.name, link: `/dish/${e.id}`
      }))
    }, err => {
      showNotify(`发生错误：${err}`)
    })
  }
})
</script>

<template>
  <!--<van-nav-bar title="标题" />-->

  <SearchBar @click-dice="searchRedirect" @click-search="searchRedirect" @to-search="searchRedirect"/>
  <HomeSwipe />
  <van-row>
    <van-col span="12">
      <RankBoard title="今日推荐" :lines="recommendation" :cover="$isGuest()?'要查看推荐，请登录':undefined"/>
    </van-col>
    <van-col span="12">
      <RankBoard title="销量最高" :lines="rank"/>
    </van-col>
  </van-row>

  <!--<van-button type="primary">主要按钮</van-button>-->
  <Waterfall />
  <BottomBar active="home"/>
</template>

<style scoped>

</style>