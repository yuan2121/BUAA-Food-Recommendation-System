<script lang="ts">
import {defineComponent, ref} from 'vue'
export default defineComponent({
  name: "BottomBar",
  props: {
    active: String
  },
  setup(props) {
    const active = ref(props.active)
    return { active }
  }
})
</script>

<template>
  <van-tabbar v-model="active">
    <van-tabbar-item name="home" icon="home-o" to="/home">主页</van-tabbar-item>
    <van-tabbar-item name="rank" icon="medal-o" to="/rank">排行</van-tabbar-item>
    <van-tabbar-item name="community" icon="fire-o" to="/community">社区</van-tabbar-item>
    <van-tabbar-item name="statistics" icon="home-o" to="/statistics">统计</van-tabbar-item>
    <van-tabbar-item name="my" icon="user-o" to="/mine">我的</van-tabbar-item>
  </van-tabbar>
</template>

<style scoped>

</style>