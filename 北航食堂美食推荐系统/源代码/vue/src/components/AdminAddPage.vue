<script lang="ts">
import {defineComponent, ref} from 'vue'
import {generatePost, generatePostJson} from "@/utils/protocal";
import {showNotify} from "vant";

export default defineComponent({
  name: "AdminAddPage",
  setup() {
    const hall = ref('')
    const window = ref('')
    const dish = ref('')
    const dish_type = ref('')
    const price_str = ref(0)
    const tags_str = ref('')

    const tab_active = ref(0)
    const tab2_active = ref(0)

    const new_hall = ref('')
    const new_window = ref('')
    const new_dish = ref('')
    return {
      hall,
      new_hall,
      window,
      new_window,
      dish,
      new_dish,
      dish_type,
      price_str,
      tags_str,
      tab_active,
      tab2_active
    }
  },
  methods: {
    add(type: 'hall' | 'window' | 'dish') {
      if (type == 'hall') {
        generatePost('/admin/add_hall', {hall: this.hall}).then(response => {
          if (response.data?.code !== 0) {
            throw new Error(`Errcode: ${response.data?.code}`)
          } else {
            showNotify({type: 'success', message: "成功"})
          }
        }, err => {
          showNotify(`发生错误：${err}`)
        })
      } else if (type == 'window') {
        generatePost('/admin/add_window', {
          hall: this.hall,
          window: this.window
        }).then(response => {
          if (response.data?.code !== 0) {
            throw new Error(`Errcode: ${response.data?.code}`)
          } else {
            showNotify({type: 'success', message: "成功"})
          }
        }, err => {
          showNotify(`发生错误：${err}`)
        })
      } else if (type == 'dish') {
        generatePostJson('/admin/add_dish', {
          hall: this.hall,
          window: this.window,
          name: this.dish,
          'type': this.dish_type,
          price: this.price,
          tags: this.tags
        }).then(response => {
          if (response.data?.code !== 0) {
            throw new Error(`Errcode: ${response.data?.code}`)
          } else {
            showNotify({type: 'success', message: "成功"})
          }
        }, err => {
          showNotify(`发生错误：${err}`)
        })
      }
    },
    modify(type: 'hall' | 'window' | 'dish') {
      if (type == 'hall') {
        generatePost('/admin/edit_hall', {
          hall: this.hall,
          newName: this.new_hall
        }).then(response => {
          if (response.data?.code !== 0) {
            throw new Error(`Errcode: ${response.data?.code}`)
          } else {
            showNotify({type: 'success', message: "成功"})
          }
        }, err => {
          showNotify(`发生错误：${err}`)
        })
      } else if (type == 'window') {
        generatePost('/admin/edit_window', {
          hall: this.hall,
          window: this.window,
          newName: this.new_window
        }).then(response => {
          if (response.data?.code !== 0) {
            throw new Error(`Errcode: ${response.data?.code}`)
          } else {
            showNotify({type: 'success', message: "成功"})
          }
        }, err => {
          showNotify(`发生错误：${err}`)
        })
      } else if (type == 'dish') {
        generatePost('/admin/edit_dish', {
          hall: this.hall,
          window: this.window,
          dish: this.dish,
          newName: this.new_dish
        }).then(response => {
          if (response.data?.code !== 0) {
            throw new Error(`Errcode: ${response.data?.code}`)
          } else {
            showNotify({type: 'success', message: "成功"})
          }
        }, err => {
          showNotify(`发生错误：${err}`)
        })
      }
    },
    del(type: 'hall' | 'window' | 'dish') {
      if (type == 'hall') {
        generatePost('/admin/delete_hall', {hall: this.hall}).then(response => {
          if (response.data?.code !== 0) {
            throw new Error(`Errcode: ${response.data?.code}`)
          } else {
            showNotify({type: 'success', message: "成功"})
          }
        }, err => {
          showNotify(`发生错误：${err}`)
        })
      } else if (type == 'window') {
        generatePost('/admin/delete_window', {
          hall: this.hall,
          window: this.window
        }).then(response => {
          if (response.data?.code !== 0) {
            throw new Error(`Errcode: ${response.data?.code}`)
          } else {
            showNotify({type: 'success', message: "成功"})
          }
        }, err => {
          showNotify(`发生错误：${err}`)
        })
      } else if (type == 'dish') {
        generatePost('/admin/delete_dish', {
          hall: this.hall,
          window: this.window,
          dish: this.dish
        }).then(response => {
          if (response.data?.code !== 0) {
            throw new Error(`Errcode: ${response.data?.code}`)
          } else {
            showNotify({type: 'success', message: "成功"})
          }
        }, err => {
          showNotify(`发生错误：${err}`)
        })
      }
    }
  },
  computed: {
    tags(): string[] {
      return this.tags_str.split(' ').filter(e => e.length > 0)
    },
    price(): number {
      return Number(this.price_str)
    }
  }
})
</script>

<template>
  <van-nav-bar title="内容管理" left-arrow @click-left="$router.back()"/>
  <van-tabs v-model:active="tab_active">
    <van-tab title="食堂">
      <van-tabs v-model:active="tab2_active" type="card" style="padding-top: 10px">
        <van-tab title="添加">
          <van-cell-group title="要添加的" inset>
            <van-cell>
              <van-field v-model="hall" label="食堂" placeholder="请输入食堂名称" />
            </van-cell>
            <van-cell>
              <van-button @click="add('hall')">添加食堂</van-button>
            </van-cell>
          </van-cell-group>
        </van-tab>
        <van-tab title="修改">
          <van-cell-group title="原信息" inset>
            <van-cell>
              <van-field v-model="hall" label="食堂" placeholder="请输入食堂名称" />
            </van-cell>
          </van-cell-group>
          <van-cell-group title="要修改到的" inset>
            <van-cell>
              <van-field v-model="new_hall" label="食堂" placeholder="请输入食堂名称" />
            </van-cell>
            <van-cell>
              <van-button @click="modify('hall')">修改食堂</van-button>
            </van-cell>
          </van-cell-group>
        </van-tab>
        <van-tab title="删除">
          <van-cell-group title="要删除的" inset>
            <van-cell>
              <van-field v-model="hall" label="食堂" placeholder="请输入食堂名称" />
            </van-cell>
            <van-cell>
              <van-button @click="del('hall')" type="danger">删除食堂</van-button>
            </van-cell>
          </van-cell-group>
        </van-tab>
      </van-tabs>
    </van-tab>

    <van-tab title="窗口">
      <van-tabs v-model:active="tab2_active" type="card" style="padding-top: 10px">
        <van-tab title="添加">
          <van-cell-group title="要添加的" inset>
            <van-cell>
              <van-field v-model="hall" label="食堂" placeholder="请输入食堂名称" />
            </van-cell>
            <van-cell>
              <van-field v-model="window" label="窗口" placeholder="请输入窗口名称" />
            </van-cell>
            <van-cell>
              <van-button @click="add('window')">添加窗口</van-button>
            </van-cell>
          </van-cell-group>
        </van-tab>
        <van-tab title="修改">
          <van-cell-group title="原信息" inset>
            <van-cell>
              <van-field v-model="hall" label="食堂" placeholder="请输入食堂名称" />
            </van-cell>
            <van-cell>
              <van-field v-model="window" label="窗口" placeholder="请输入窗口名称" />
            </van-cell>
          </van-cell-group>
          <van-cell-group title="要修改到的" inset>
            <van-cell>
              <van-field v-model="new_window" label="窗口" placeholder="请输入窗口名称" />
            </van-cell>
            <van-cell>
              <van-button @click="modify('window')">修改窗口</van-button>
            </van-cell>
          </van-cell-group>
        </van-tab>
        <van-tab title="删除">
          <van-cell-group title="要删除的" inset>
            <van-cell>
              <van-field v-model="hall" label="食堂" placeholder="请输入食堂名称" />
            </van-cell>
            <van-cell>
              <van-field v-model="window" label="窗口" placeholder="请输入窗口名称" />
            </van-cell>
            <van-cell>
              <van-button @click="del('window')" type="danger">删除窗口</van-button>
            </van-cell>
          </van-cell-group>
        </van-tab>
      </van-tabs>

    </van-tab>


    <van-tab title="菜品">
      <van-tabs v-model:active="tab2_active" type="card" style="padding-top: 10px">
        <van-tab title="添加">
          <van-cell-group title="要添加的" inset>
            <van-cell>
              <van-field v-model="hall" label="食堂" placeholder="请输入食堂名称" />
            </van-cell>
            <van-cell>
              <van-field v-model="window" label="窗口" placeholder="请输入窗口名称" />
            </van-cell>
            <van-cell>
              <van-field v-model="dish" label="菜品" placeholder="请输入菜品名称" />
            </van-cell>
            <van-cell>
              <van-field v-model="dish_type" label="类型" placeholder="请输入菜品类型" />
            </van-cell>
            <van-cell>
              <van-field v-model="price_str" label="价格" placeholder="请输入菜品类型" />
            </van-cell>
            <van-cell>
              <van-field v-model="tags_str" label="TAG" placeholder="请输入菜品标签，以空格分隔" />
            </van-cell>
            <van-cell>
              <van-button @click="add('dish')">添加菜品</van-button>
            </van-cell>
          </van-cell-group>
        </van-tab>
        <van-tab title="修改">
          <van-cell-group title="原信息" inset>
            <van-cell>
              <van-field v-model="hall" label="食堂" placeholder="请输入食堂名称" />
            </van-cell>
            <van-cell>
              <van-field v-model="window" label="窗口" placeholder="请输入窗口名称" />
            </van-cell>
            <van-cell>
              <van-field v-model="dish" label="菜品" placeholder="请输入菜品名称" />
            </van-cell>
          </van-cell-group>
          <van-cell-group title="要修改到的" inset>
            <van-cell>
              <van-field v-model="new_dish" label="菜品" placeholder="请输入菜品新名称" />
            </van-cell>
            <van-cell>
              <van-button @click="modify('dish')">修改菜品</van-button>
            </van-cell>
          </van-cell-group>
        </van-tab>
        <van-tab title="删除">
          <van-cell-group title="要删除的" inset>
            <van-cell>
              <van-field v-model="hall" label="食堂" placeholder="请输入食堂名称" />
            </van-cell>
            <van-cell>
              <van-field v-model="window" label="窗口" placeholder="请输入窗口名称" />
            </van-cell>
            <van-cell>
              <van-field v-model="dish" label="菜品" placeholder="请输入菜品名称" />
            </van-cell>
            <van-cell>
              <van-button @click="del('dish')" type="danger">删除菜品</van-button>
            </van-cell>
          </van-cell-group>
        </van-tab>
      </van-tabs>
    </van-tab>
  </van-tabs>
</template>

<style scoped>

</style>