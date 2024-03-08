<script lang="ts">
import {defineComponent, ref} from 'vue'
import SearchBar from "@/components/SearchBar.vue";
import BottomBar from "@/components/BottomBar.vue";
import CheckboxMultiItem from "@/components/CheckboxMultiItem.vue";

type SearchStatus = 'empty' | 'searching' | 'returned'
import type {DishSummary, OrderMethod, ParamSearch, PreferenceTag, ResultSearch} from "@/utils/dataTypes";
import SearchResultItem from "@/components/SearchResultItem.vue";
import {showNotify, showToast} from "vant";
import {preferenceTagOnSearch} from "@/utils/dataTypes";
import {generatePost, generatePostJson, isMorning} from "@/utils/protocal";
import EatDialog from "@/components/EatDialog.vue";

export default defineComponent({
  name: "SearchPage",
  components: {EatDialog, SearchResultItem, CheckboxMultiItem, BottomBar, SearchBar},
  setup() {
    const searchBar = ref()
    const dropdownHall = ref()

    const collected_dish_id = ref([] as number[])

    const selected_tags = ref<Array<PreferenceTag>>([])

    const value_order = ref<OrderMethod>('score')
    const value_type = ref(isMorning() ? '早餐' : '正餐')

    const checked_hall = ref<Array<string>>([])

    const options_hall = ref([
      { text: '学一食堂', value: '学一食堂' },
      { text: '学四食堂', value: '学四食堂' },
      { text: '学二食堂', value: '学二食堂' },
      { text: '学三食堂', value: '学三食堂' },
      { text: '学五食堂', value: '学五食堂' },
      { text: '学六食堂', value: '学六食堂' },
    ])
    const options_order = [
      { text: '默认排序', value: 'score' },
      { text: '收藏排序', value: 'collect' },
      { text: '销量排序', value: 'sales' },
    ]
    const options_type = [
      { text: '早餐', value: '早餐' },
      { text: '正餐', value: '正餐' },
      { text: '饮料', value: '饮料' },
    ]

    const keyword_changed = ref(true)

    const search_status = ref<SearchStatus>('empty');
    const search_result_list = ref<Array<DishSummary>>([])
    const eatDialog = ref<InstanceType<typeof EatDialog>>()
    const rate_of_dialog = ref(0)

    return {
      searchBar, dropdownHall,
      value_order,
      options_hall,
      options_order,
      checked_hall,
      options_type,
      value_type,
      search_status,
      search_result_list,
      selected_tags,
      rate_of_dialog,
      eatDialog,
      keyword_changed,
      collected_dish_id
    }
  },
  mounted() {
    this.searchBar.focus()
  },
  created() {
    generatePost('/search/get_hall').then(response => {
      if (response.data?.code !== 0) {
        throw new Error(`ErrCode: ${response.data?.code}`)
      }
      const hall_list = response.data.halls as string[]
      this.options_hall = hall_list.map(e => ({text: e, value: e}))
    }, err => {
      showNotify(`发生错误：${err}`)
    })
    if (!this.$isGuest()) {
      this.refreshCollectList()
    }
  },
  computed: {
    multiCheckHallTitle() {
      if (this.checked_hall.length === 0) {
        return '全部食堂'
      } else {
        return this.checked_hall.join(',')
      }
    }
  },
  methods: {
    showToast,
    async search(keyword: string) {
      this.search_result_list = []
      this.search_status = 'searching';
      this.keyword_changed = false

      const param: ParamSearch = {
        keyword,
        hall: this.checked_hall,
        order: this.value_order,
        filters: preferenceTagOnSearch(this.selected_tags),
        'type': this.value_type,
      }
      await generatePostJson('/search/search', param).then(response => {
        if (!(response.data)) throw new Error('Unavailable Result')
        const result: ResultSearch = response.data
        if (result.code !== 0) throw new Error(`Request Failed with ErrCode: ${result.code}`)

        this.search_result_list = result.dishes
        this.search_status = result.dishes.length > 0 ? 'returned' : 'empty'
      }, err => {
        showNotify({message: `遇到错误：${err}`})
        this.search_status = "empty"
      })
    },
    async dice(keyword: string) {
      if (this.keyword_changed) {
        await this.search(keyword)
      }
      const res_id = Math.round(Math.random()*this.search_result_list.length)
      showToast({
        message: `今天去吃\n${this.search_result_list[res_id].name}\n吧！`,
        icon: ('/images/' + this.search_result_list[res_id].name + '.jpg') ?? undefined
      })
    },
    showEatDialog(dish_id: number) {
      this.eatDialog?.show(dish_id)
    },
    eat(dish_id: number) {
      generatePost('/dish/purchase', {
        dish_id,
        user_id: this.$cookies.get('user_id')
      }).then(response => {
        if (response.data?.code !== 0) {
          throw new Error(`Errcode: ${response.data?.code}`)
        }
        this.updateDish(dish_id)
      }, err => {
        showNotify({message: `发生错误：${err}`})
      })
      this.showEatDialog(dish_id)
    },
    updateDish(dish_id: number) {
      generatePost('/dish/get_detail', {
        dish_id
      }).then(response => {
        if (response.data?.code !== 0) {
          throw new Error(`Errcode: ${response.data?.code}`)
        }
        const summary: DishSummary = response.data.summary
        for (let i = 0; i < this.search_result_list.length; i++) {
          if (this.search_result_list[i].id === dish_id) {
            this.search_result_list[i] = summary
          }
        }
      }, err => {
        showNotify({message: `发生错误：${err}`})
      })
    },
    bookmark(dish_id: number) {
      if (this.$isGuest()) {
        this.$router.push('/')
        showNotify({ type: 'warning', message: '请登录' })
        return
      }

      if (this.collected_dish_id.includes(dish_id)) {
        generatePost('/user/delete_collect', {
          dish_id,
          user_id: this.$cookies.get('user_id')
        }).then(response => {
          if (response.data?.code !== 0) {
            throw new Error(`Errcode: ${response.data?.code}`)
          }
          showToast('取消收藏')
          this.refreshCollectList()
          this.updateDish(dish_id)
        }, err => {
          showNotify({message: `发生错误：${err}`})
        })
      } else {
        generatePost('/user/save_collect', {
          dish_id,
          user_id: this.$cookies.get('user_id')
        }).then(response => {
          if (response.data?.code !== 0) {
            throw new Error(`Errcode: ${response.data?.code}`)
          }
          showToast('收藏成功！')
          this.refreshCollectList()
          this.updateDish(dish_id)
        }, err => {
          showNotify({message: `发生错误：${err}`})
        })
      }


    },
    refreshCollectList() {
      generatePost('/user/collect', {
        user_id: this.$getUser()
      }).then(response => {
        if (response.data?.code !== 0) {
          throw new Error(`ErrCode: ${response.data?.code}`)
        }
        const dishes: DishSummary[] = response.data?.dishes ?? []
        this.collected_dish_id = dishes.map( e => e.id )
      }, err => {
        showNotify(`发生错误：${err}`)
      })
    }
  }
})
</script>

<template>
  <SearchBar ref="searchBar" @to-search="search" @click-dice="dice" @change="keyword_changed = true"
             v-model="selected_tags" style="position: relative; z-index: 2000" />
  <van-sticky>
  <van-dropdown-menu>
    <van-dropdown-item :title="multiCheckHallTitle" ref="dropdownHall">
      <van-checkbox-group v-model="checked_hall">
        <CheckboxMultiItem v-for='item in options_hall'
                           :title="item.text" :value="item.value" :group-checked-list="checked_hall" />
      </van-checkbox-group>

      <van-grid clickable :column-num="2">
        <van-grid-item text="清空" @click="checked_hall=[]; dropdownHall.toggle()"/>
        <van-grid-item text="确定" @click="dropdownHall.toggle()"/>
      </van-grid>
    </van-dropdown-item>

    <van-dropdown-item v-model="value_type" :options="options_type"/>
    <van-dropdown-item v-model="value_order" :options="options_order"/>
  </van-dropdown-menu>
  </van-sticky>
  <!--
  <div style="position: absolute; margin-top: 100px; z-index: 100">
    <van-button @click="search_status = 'empty'; search_result_list = []"/>
    <van-button @click="search_status = 'searching'" />
    <van-button @click="search_status = 'returned'; search_result_list.push(demo_dish)" />
  </div>
  -->
  <van-empty v-if="search_status == 'empty'" description="这里空空如也"/>
  <van-list v-else :loading="search_status == 'searching'">
    <SearchResultItem v-for="(dish, index) in search_result_list" :key="index" :item="dish" :required-tags="selected_tags"
      @click-eat="eat(dish.id)" @card-click="$router.push(`/dish/${dish.id}`)"
      @bookmark="bookmark(dish.id)" :collected="collected_dish_id.includes(dish.id)"/>
  </van-list>
  <EatDialog v-model:rate="rate_of_dialog" ref="eatDialog" @close="updateDish" />
  <BottomBar />
</template>

<style scoped>

</style>
