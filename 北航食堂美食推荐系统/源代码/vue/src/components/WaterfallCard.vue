<script lang="ts">
import {defineComponent, ref} from 'vue'
import type {SummaryData} from '@/utils/dataTypes'
import {showToast} from "vant";

export default defineComponent({
  name: "WaterfallCard",
  methods: {showToast},
  props: {
    item: {
      type: Object as () => SummaryData,
      required: true
    },
    boxWidth: Number,
    community: {
      type: Boolean,
      default: false
    },
    heart_clicked: {
      type: Boolean,
      default: false
    }
  },
  emits: ['cardClick', 'heartClick', 'update:heart_clicked'],
})
</script>

<template>
  <div class="data-item"
       @click="$emit('cardClick')" :style="{width: boxWidth + 'px'}">
    <img class="data-cover" :src="item.cover" :style="{width: '100%', height: item.imgHeight + 'px'}"
         :alt="item.sign"/>
    <div class="data-title">{{item.sign}}</div>
    <div class="data-subtitle">
      {{ item.sub_title1 }}
      <van-divider vertical :hairline="false" />
      {{ item.sub_title2 }}
      <van-icon v-if="community" :name="heart_clicked ? 'like' : 'like-o'"
                :color="heart_clicked ? 'red' : undefined"
                size="18px" style="right: 10px; position: absolute"
        @click="event => {
          event.stopPropagation()
          $emit('update:heart_clicked', true)
          $emit('heartClick')
        }"/>
    </div>
    <div class="data-tags">
      <div class="data-single-tag" v-for="tag in item.tags">
        <van-tag :type="['甜','辣','酸', '面食'].includes(tag) ? 'warning' : ['素食','清淡'].includes(tag)? 'success' :'primary'"
                 :plain="['清淡', '开胃', '面食', '小吃', '素食'].includes(tag)">{{ tag }}</van-tag>
      </div>
    </div>

  </div>
</template>

<style scoped>

@keyframes data-item-ani{
  0% { transform: scale(0.5); }
  100% { transform: scale(1); }
}
.data-item {
  height: auto;
  position: absolute; background-color: #ffffff; left: -1000px;
  animation: data-item-ani 0.4s;
  transition: left 0.6s, top 0.6s;
  transition-delay: 0.1s;
  border-radius: 5px;
}
.data-item .data-cover { display: block; }
.data-cover {border-radius: 5px 5px 0 0;}
.data-item:active {filter: brightness(90%)}
.data-title { font-size: 16px; padding: 5px 10px; text-align: left; }
.data-subtitle { font-size: 12px; padding: 0 10px 5px 10px; text-align: left; color: #888 }
.data-tags {padding: 5px 10px;}
.data-single-tag {padding: 0 5px 0 0; display: inline}
</style>

<style>

:root:root {
  --van-divider-vertical-margin: 0 3px;
}
</style>