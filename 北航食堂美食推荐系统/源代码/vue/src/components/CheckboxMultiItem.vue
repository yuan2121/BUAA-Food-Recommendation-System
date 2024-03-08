<script lang="ts">
import {defineComponent, ref} from 'vue'

export default defineComponent({
  name: "CheckboxMultiItem",
  computed: {
    isChecked() {
      return this.groupCheckedList?.includes(this.value) ?? false
    }
  },
  props: {
    title: String,
    value: String,
    groupCheckedList: Array<string>
  },
  setup() {
    const checkbox = ref()
    const checked = ref(false)
    return {
      checkbox,
      checked
    }
  }
})
</script>

<template>
  <van-cell clickable center :title="title" @click="checkbox.toggle()"
            :style="'color: ' + ((isChecked)?'var(--van-primary-color)':'var(--van-text-color)')">
    <template #right-icon>
      <van-checkbox
          :name="value"
          ref="checkbox"
          @click.stop
      >
        <template #icon="props">
          <van-icon :style="'color: ' + (props.checked?'var(--van-primary-color)':'white')"
                    style="font-size: 14px" name="success"/>
        </template>
      </van-checkbox>
    </template>
  </van-cell>
</template>

<style scoped>

</style>


<style>
:root:root {
  --van-checkbox-border-color: white;
  --van-checkbox-checked-icon-color: transparent;
}
</style>