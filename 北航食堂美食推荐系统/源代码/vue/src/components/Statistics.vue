<template>
  <div ref="pdfContent">
    <div style="display: flex;">
      <div style="flex: 1;">
        <div style="margin-bottom: 15px;margin-top: 20px;margin-left: 20px; font-weight: bold;font-size: 28px">系统统计图</div>
        <div style="margin-left: 20px;">本系统对北航所有菜品数量分别按类别、所属食堂和价格区间进行统计，方便用户及游客对北航食堂有更充分的认识，有更好的购餐体验。</div>
        <button style="margin-left: 20px;" @click="exportToPdf">导出为PDF</button>
      </div>

      <div style="width: 50px"></div>

      <div style="flex: 1; margin-top: 50px">
        <div ref="bie1" class="chart" style="width: 80%; height: 430px"></div>
      </div>

    </div>
    <div style="display: flex;">

      <div style="width: 50%">
        <div ref="bie2" class="chart" style="width: 80%; height: 430px"></div>
      </div>

      <div style="width: 50%">
        <div ref="bar" class="chart" style="width: 80%; height: 430px"></div>
      </div>

    </div>
  </div>

  <BottomBar active="statistics" />
</template>

<style scoped></style>


<script lang="ts">
import { defineComponent, ref } from 'vue';
import BottomBar from "./BottomBar.vue";
import { showToast } from 'vant';
import { generatePost } from '@/utils/protocal';
import * as echarts from "echarts";
import html2pdf from 'html2pdf.js';

export default defineComponent({
  name: "Statistics",
  components: { BottomBar },
  data() {
    const array = [0, 10, 100, 1000]
    const a = ref()
    return {
      // b2xb: Number,
      // b2hy: Number,
      // b2xe: Number,
      // b2xs: Number,
      // b1zheng: Number,
      // b1zao: Number,
      // b1yin: Number,
      // b31: Number,
      // b32: Number,
      // b33: Number,
      // b34: Number,
      // b35: Number,
      myChart1: null,
      myChart2: null,
      myChart3: null,
      array,
      user_id: "id尚未刷新"
    }
  },


  mounted() {
    this.initBie1();
    this.initBie2();
    this.initBar();
  },


  methods: {
    exportToPdf() {
      const content = this.$refs.pdfContent;
      const options = {
        filename: 'exported.pdf',
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'mm', format: 'a2', orientation: 'portrait' }
      };

      html2pdf().set(options).from(content).save();
    },


    initBie1() {
      // generatePost('/user/collect_demo1', { })
      //   .then(res => {
      //     this.b1zheng=res.data.key1;
      //     this.b1zao=res.data.key2;
      //     this.b1yin=res.data.key3;
      //   })

      // let chartDom = document.getElementById('bie1');
      let chartDom = this.$refs.bie1;
      this.myChart1 = echarts.init(chartDom);
      let option;
      option = {
        title: {
          text: '类型统计（饼图）',
          subtext: '统计维度：菜品数量',
          left: 'center'
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          orient: 'vertical',
          left: 'left'
        },
        series: [
          {
            name: 'Access From',
            type: 'pie',
            radius: '50%',
            data: [
              { value: 69, name: '早餐' },
              { value: 526, name: '正餐' },
              { value: 87, name: '饮料' }
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      };

      option && this.myChart1.setOption(option);

    },

    initBie2() {
      // generatePost('/user/collect_demo2', { })
      //   .then(res => {
      //     this.b2xb=res.data.key1;
      //     this.b2hy=res.data.key2;
      //     this.b2xe=res.data.key3;
      //     this.b2xs=res.data.key4;
      //   })


      // let chartDom = document.getElementById('bie2');
      // let myChart2 = echarts.init(chartDom);
      let chartDom = this.$refs.bie2;
      this.myChart2 = echarts.init(chartDom);
      let option;

      option = {
        title: {
          text: '食堂统计（饼图）',
          subtext: '统计维度：菜品数量',
          left: 'center'
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          orient: 'vertical',
          left: 'left'
        },
        series: [
          {
            name: 'Access From',
            type: 'pie',
            radius: '50%',
            data: [
              { value: 127, name: '合一' },
              { value: 191, name: '学二' },
              { value: 162, name: '学四' },
              { value: 202, name: '新北' }
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      };

      option && this.myChart2.setOption(option);

    },


    initBar() {
      // generatePost('/user/collect_demo3', { })
      //   .then(res => {
      //     this.b31=res.data.key1;
      //     this.b32=res.data.key2;
      //     this.b33=res.data.key3;
      //     this.b34=res.data.key4;
      //     this.b35=res.data.key5;
      //   })


      // let chartDom = document.getElementById('bar');
      // let myChart = echarts.init(chartDom);
      let chartDom = this.$refs.bar;
      this.myChart3 = echarts.init(chartDom);
      let option;

      option = {
        title: {
          text: '价格区间统计',
          subtext: "统计维度：菜品数量",
          // left: 'center'
        },
        xAxis: {
          type: 'category',
          data: ['0-4.9元','5-9.9元', '10-14.9元', '15-19.9元']
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            data: [165, 238, 142, 137],
            type: 'bar'
          }
        ]
      };

      option && this.myChart3.setOption(option);
    }
  }
})


</script>

