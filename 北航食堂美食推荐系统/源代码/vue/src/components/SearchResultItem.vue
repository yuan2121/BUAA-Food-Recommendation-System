<script lang="ts">
import {defineComponent, ref} from 'vue'
import type {DishSummary, PreferenceTag} from "@/utils/dataTypes";
import {showToast} from "vant";

export default defineComponent({
  name: "SearchResultItem",
  methods: {showToast},
  props: {
    item: {
      type: Object as () => DishSummary,
      required: true
    },
    requiredTags: {
      type: Array<PreferenceTag>,
      required: true
    },
    collected: {
      type: Boolean,
      default: false
    }
  },
  emits: ['clickEat', 'cardClick', 'bookmark'],
  setup: function (props) {

  },
  computed: {
    score() {
      return this.item.score / 5
    }
  }
})
</script>

<template>
  <van-cell clickable>
  <div class="data-item"
       @click="$emit('cardClick')">
    <div class="data-item-row-1">
      <div style="display: flex; justify-items: center; width: 30%; flex-direction: column">
        <img class="data-cover" :src="`/images/${item.name}.jpg`" :style="{width: '100%', height: '64px', objectFit: 'cover'}"
             :alt="item.name"/>
      </div>
      <div style="width: 35%">
        <div class="data-title">{{item.name}}</div>
        <div class="data-subtitle">
          {{item.hall}}
          <van-divider vertical :hairline="false" />
          {{ item.window }}
        </div>
      </div>

      <div style="margin-left: auto; margin-right: 10px">
        <div style="display: flex; align-items: baseline">
          <van-rate v-model="score" readonly allow-half :count="1"/>
          <span class="data-score-text">{{item.score.toFixed(2)}}</span>
          <span class="data-score-text-sub">/ {{item.comment}} 人评分</span>
        </div>
      </div>
    </div>

    <div class="data-item-row-2">
      <van-row class="data-description-under-cover">
        <van-col :span="10" class="data-description-under-cover-unit" @click="event => {
          event.stopPropagation()
          $emit('bookmark')
        }">
          <van-icon :name="collected ? 'star' : 'star-o'" />
          <span style="margin-left: 2px;">{{item.collectNum}}</span>
        </van-col>
        <van-col :span="10" class="data-description-under-cover-unit">
          <van-icon name="shopping-cart-o" />
          <span style="margin-left: 2px;">{{item.purchase}}</span>
        </van-col>
      </van-row>

      <div class="data-tags-container">
      <div class="data-tags">
        <div class="data-single-tag" v-for="tag in item.tags">
          <van-tag type="primary" :plain="requiredTags.some(el=>el.attitude && el.name == tag)">
            {{ tag }}
          </van-tag>
        </div>
      </div>
      </div>
    </div>

    <van-button style="position: absolute; right: 10px; bottom: 3px" v-if="!$isGuest()"
                @click="event => {event.stopPropagation(); $emit('clickEat')}">
      吃
    </van-button>
  </div>
  </van-cell>
</template>

<style scoped>

.data-item {
  height: auto;
  position: relative;
  display: flex;
  flex-direction: column;
  line-height: normal;
}
.data-item-row-1 {
  height: auto;
  position: relative;
  display: flex;
  line-height: normal;
}
.data-item-row-2 {
  position: relative;
  display: flex;
  align-items: baseline;
  overflow: hidden;
}
.data-item .data-cover { display: block; }
.data-cover {border-radius: 5px 5px 0 0}
.data-title { font-size: 16px; padding: 5px 10px; text-align: left; color: black}
.data-subtitle { font-size: 12px; padding: 0 10px 5px 10px; text-align: left; color: #888 }
.data-tags-container {
  padding: 5px 10px; width: 40%;overflow: hidden; height: 17px
}
.data-tags { display: flex; width: max-content }
.data-single-tag {padding: 0 5px 0 0; display: inline}
.data-description-under-cover {
  text-align: center;
  width: 30%;
  display: flex;
  justify-content: center;
}
.data-description-under-cover-unit {
  text-align: center;
}
.data-score-text {
  margin-left: 5px;
  color: red;
  font-weight: bold;
  font-size: 18px;
}
.data-score-text-sub {
  margin-left: 3px;
  font-weight: normal;
  font-size: 8px;
}
</style>