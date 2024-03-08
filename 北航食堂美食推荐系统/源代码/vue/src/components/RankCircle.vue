<script lang="ts">
import {defineComponent} from 'vue'

export default defineComponent({
  name: "RankCircle",
  props: {
    size: Number,
    num: Number,
    color: String,
    textColor: {
      type: String,
      default: 'white'
    }
  }
})
</script>

<template>
  <div class="shell">
    <div class="box">
      <span class="num-text">
        {{num}}
      </span>
    </div>
  </div>
</template>

<style scoped>
.shell {
  align-self: center;
  margin-right: var(--van-padding-base);
}
.box {
  width: v-bind(size + 'px');
  height: v-bind(size + 'px');
  background-color: v-bind(color);
  border-radius: 5px;
  text-align: center;
  vertical-align: middle;
  color: v-bind(textColor);
  font-weight: bold;
  display: flex;
  align-items: center;
}
.num-text {
  width: 100%;
}
</style>