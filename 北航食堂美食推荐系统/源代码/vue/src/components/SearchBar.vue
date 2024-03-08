<script lang="ts">
import {defineComponent} from 'vue'
import { ref } from 'vue';
import type {PreferenceTag} from "@/utils/dataTypes";


export default defineComponent({
  name: "SearchBar",
  props: {
    modelValue: {
      type: Array<PreferenceTag>,
      default: [] as PreferenceTag[]
    }
  },
  methods: {
    focus() {
      this.search.focus()
    }},
  emits: ['toSearch', 'clickSearch', 'clickDice', 'update:modelValue', 'change'],
  setup(props, { emit }) {
    const value = ref('');
    const search = ref()
    const onSearch = (keyword: string) => emit('toSearch', keyword);
    const addTag = (attitude: boolean) => {
      const tag = { name: value.value, attitude }
      props.modelValue.push(tag)
      value.value = ""
      emit('update:modelValue', props.modelValue)
    }
    const removeTag = (index: number) => {
      props.modelValue.splice(index, 1)
      emit('update:modelValue', props.modelValue)
    }

    return {
      value,
      search,
      onSearch,

      addTag,
      removeTag,
    };
  }
});

</script>

<template>
  <div>
    <form action="/">
      <!--iOS 搜索兼容-->
    <van-search
        v-model="value"
        show-action
        placeholder="请输入菜品关键词"
        @search="onSearch"
        @update:model-value="value => $emit('change', value)"
        shape="round"
        @click-input="$emit('clickSearch', value)"
        ref="search"
        style="padding-right: 5px"
        :clearable="false"
    >
      <template #action>
        <div @click="$emit('clickDice', value)"><van-icon name="/dice.svg" size="20" style="vertical-align: middle"/></div>
      </template>
      <template #right-icon>
        <div style="display: flex" v-if="value.length > 0">
          <van-button size="mini" class="search-tag-button-positive"
                      @click="addTag(true)" round>
            <div class="search-tag-button-text-container">
              <van-icon size="13px" name="plus" />
            </div>
          </van-button>
          <van-button size="mini" class="search-tag-button-negative"
                      @click="addTag(false)" round>
            <div class="search-tag-button-text-container">
              <van-icon size="13px" name="minus" />
            </div>
          </van-button>
        </div>
      </template>
    </van-search>
    </form>

    <div v-if="modelValue.length > 0" class="search-tag-container">
      <van-tag v-for="(tag, index) in modelValue" type="danger" closeable size="large" :plain="tag.attitude"
        class="search-tag-box" @close="removeTag(index)">
        {{(tag.attitude ? '+' : '-') + ' ' + tag.name}}
      </van-tag>
    </div>

  </div>

</template>

<style scoped>

.search-tag-button-positive, .search-tag-button-negative {
  aspect-ratio: 1
}

.search-tag-button-text-container {
  display: flex;
  gap: 2px;
  color: black;
}

.search-tag-container {
  display: flex;
  flex-wrap: wrap;
  padding: 0 13px 5px 13px;
  background-color: white;
}
.search-tag-box {
  margin: 2px 2px
}
</style>