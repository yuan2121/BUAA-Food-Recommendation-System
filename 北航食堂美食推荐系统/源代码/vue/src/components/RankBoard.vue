<script lang="ts">
import {defineComponent} from 'vue'
import type {RankItem} from "@/utils/dataTypes";
import RankCircle from "@/components/RankCircle.vue";
import type {ConfigProviderThemeVars} from "vant";

export default defineComponent({
  name: "RankBoard",
  components: {RankCircle},
  computed: {
    RankItem() {
      return Object as () => RankItem
    }
  },
  props: {
    title: String,
    lines: Array<RankItem>,
    colors: {
      type: Array<string>,
      default: [
        '#fb400d',
        '#fd6f01',
        '#fcb40a']
    },
    cover: String
  },
  setup() {
    const themeVars: ConfigProviderThemeVars = {
      cellGroupInsetPadding: '0px'
    }

    return {
      themeVars
    }
  }
})
</script>

<template>
  <van-config-provider :theme-vars="themeVars">
    <div>
      <div style="background-color: #f4f4f4">
        <van-cell-group inset>
          <van-cell :title="title" style="font-weight: bold">
          </van-cell>
          <van-cell v-for="(item, index) in lines as RankItem[]" :title="item.name" :url="item.link" clickable>
            <template #icon>
              <RankCircle :color="colors[index] ?? 'transparent'"
                          :text-color="colors[index]?undefined:'#222'"
                          :num="index + 1" :size="20" />
            </template>
          </van-cell>
          <div v-if="cover" style="display:flex; justify-content: center">
            {{cover}}
          </div>
        </van-cell-group>
      </div>
    </div>
  </van-config-provider>
</template>

<style scoped>

</style>

