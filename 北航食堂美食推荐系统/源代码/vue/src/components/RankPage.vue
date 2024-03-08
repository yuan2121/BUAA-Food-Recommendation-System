<script lang="ts">
import {defineComponent, ref} from 'vue'
import BottomBar from "@/components/BottomBar.vue";
import RankBoard from "@/components/RankBoard.vue";
import HomeSwipe from "@/components/HomeSwipe.vue";
import {DishSummary, RankItem} from "@/utils/dataTypes";
import {generatePost, isMorning} from "@/utils/protocal";
import {showNotify} from "vant";

export default defineComponent({
  name: "RankPage",
  components: {HomeSwipe, RankBoard, BottomBar},
  setup() {
    const recommendation = ref<Array<RankItem>>([])
    const sales = ref<Array<RankItem>>([])
    const score = ref<Array<RankItem>>([])
    const collect = ref<Array<RankItem>>([])
    return {
      recommendation,
      sales,
      score,
      collect
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
        n: 10
      }).then(response => {
        this.recommendation = (response.data?.dishes as DishSummary[] ?? []).map(e => ({
          name: e.name, link: `/dish/${e.id}`
        }))
      }, err => {
        showNotify(`发生错误：${err}`)
      })
    }

    for (let rank_type of ['sales', 'collect', 'score']) {
      generatePost('/search/rank', {
        order: rank_type,
        n: 10
      }).then(response => {
        this[rank_type] = (response.data?.dishes as DishSummary[] ?? []).map(e => ({
          name: e.name, link: `/dish/${e.id}`
        }))
      }, err => {
        showNotify(`发生错误：${err}`)
      })
    }
  }
})
</script>

<template>

  <van-row>
    <van-col span="12">
      <RankBoard title="今日推荐" :lines="recommendation" :cover="$isGuest()?'要查看推荐，请登录':undefined"/>
    </van-col>
    <van-col span="12">
      <RankBoard title="销量最高" :lines="sales"/>
    </van-col>
  </van-row>
  <van-row>
    <van-col span="12">
      <RankBoard title="评分最高" :lines="score"/>
    </van-col>
    <van-col span="12">
      <RankBoard title="收藏最多" :lines="collect"/>
    </van-col>
  </van-row>
  <BottomBar active="rank" />
</template>

<style scoped>

</style>