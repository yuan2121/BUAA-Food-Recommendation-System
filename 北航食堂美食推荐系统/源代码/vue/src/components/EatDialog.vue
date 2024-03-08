<script lang="ts">
import {defineComponent, ref} from 'vue'
import type {ParamPostComment} from "@/utils/dataTypes";
import {generatePost, getTime} from "@/utils/protocal";
import {showNotify} from "vant";

export default defineComponent({
  name: "EatDialog",
  props: {
    rate: {
      type: Number,
      default: 0
    }
  },
  emits: ['update:rate', 'close'],
  setup() {
    const show_of_dialog = ref(false)

    const status = ref<'unrated'|'rated'>('unrated')

    const dish_id = ref(0)

    return {
      show_of_dialog,
      status,
      dish_id
    }
  },
  methods: {
    show(dish_id: number) {
      this.$emit('update:rate', 0)
      this.status = 'unrated'
      this.dish_id = dish_id

      this.show_of_dialog = true
    },
    closeMe() {
      this.show_of_dialog = false
      this.$emit('close', this.dish_id)
    },
    postScore() {
      const param: ParamPostComment = {
        user_id: this.$getUser(),
        content: '',
        dish_id: this.dish_id,
        score: this.rate,
        time: getTime()
      }
      console.log(param)
      generatePost('/community/post_comment', param).then(response => {
        let err = response.data?.code
        if (err !== 0) {
          throw new Error(`ErrCode: ${err}`)
        }
      }, err => {
        showNotify({message: `遇到错误：${err}`})
      }).finally(() => {
        this.closeMe()
      })
    }
  }
})
</script>

<template>
    <van-dialog title="吃得怎么样呢？" v-model:show="show_of_dialog" close-on-click-overlay>
      <template #default>
        <div style="width: 100%; padding: 24px 0; display: flex; align-items: center; flex-direction: column">
          <van-rate color="orange" :modelValue="rate" @update:modelValue="value => {
            if (value > 0) {
              status = 'rated'
            }
            $emit('update:rate', value)
          }"
            size="25px" />
          <div v-if="status == 'rated'" style="padding: 8px 0 5px 0">
            <span style="font-size: 60px; color: orange">{{rate}}</span>分
          </div>
        </div>
      </template>
      <template #footer>
        <van-button v-if="status == 'unrated'" style="width: 100%; height: 48px; font-size: 16px;
         color: #1989fa"
          @click="closeMe()">不好评价</van-button>
        <div v-else>
          <van-button style="width: 100%; height: 48px; font-size: 16px;
         color: #1989fa" :url="`/commentfordishes/${dish_id}/${rate}`">写点评论</van-button>
          <van-button style="width: 100%; height: 48px; font-size: 16px;"
            @click="postScore()">就这样吧</van-button>
        </div>
      </template>
    </van-dialog>
</template>

<style scoped>

</style>