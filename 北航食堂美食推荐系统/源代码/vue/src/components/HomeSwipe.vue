<script lang="ts">
import {defineComponent} from 'vue'

export default defineComponent({
  name: "HomeSwipe"
})
</script>

<template>
  <van-swipe class="my-swipe" :autoplay="3000" indicator-color="white">
  <van-swipe-item v-for="i in 4">
    <div style="height: 350px">
      <img :src="`/banners/banner${i}.jpg`" :alt="`banner${i}`" style="width:100%; height:100%; object-fit: cover"/>
    </div>
  </van-swipe-item>
  </van-swipe>
</template>

<style scoped>
.my-swipe .van-swipe-item {
  color: #fff;
  font-size: 20px;
  line-height: 150px;
  text-align: center;
  background-color: #39a9ed;
}
</style>
