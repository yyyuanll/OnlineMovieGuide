<template>
<el-container style="">
    <el-main style="">
        <div  id="main1" style="width: 100%;height:100%;" @change="trigger"> </div>
    </el-main>
</el-container>
</template>

<script>
import * as echarts from 'echarts/core';
import { TooltipComponent, LegendComponent } from 'echarts/components';
import { PieChart } from 'echarts/charts';
import { LabelLayout } from 'echarts/features';
import { CanvasRenderer } from 'echarts/renderers';

echarts.use([
  TooltipComponent,
  LegendComponent,
  PieChart,
  CanvasRenderer,
  LabelLayout
]);
  export default {
    data() {
      return {
          chart:[
        { value: 335, name: 'Drama' },
        { value: 310, name: 'Action' },
        { value: 274, name: 'Comedy' },
        { value: 235, name: 'Romance' },
        { value: 400, name: 'Ctime' },
        { value: 350, name: 'Triller' },
        { value: 450, name: 'Adventure' },
        { value: 155, name: 'Horror' },
        { value: 266, name: 'Documentary' },
        { value: 511, name: 'Fantasy' },
        { value: 299, name: 'Biography' },
        { value: 377, name: 'Mystery' },
        { value: 456, name: 'Sci-fi' },
        { value: 199, name: 'Music' },
        { value: 245, name: 'Animation' },
        { value: 345, name: 'History' },
        { value: 321, name: 'Sport' },
        { value: 231, name: 'War' },
        { value: 253, name: 'Others' }
      ],
      username:null
      }
    },
    watch: {
  // 监测路由变化,只要变化了就调用获取路由参数方法将数据存储本组件即可
  '$route': 'uchart'
},
    methods:{
        getUsername:function(){
                var routerUserName = this.$router.query.username
                console.log(routerUserName)
                this.username = routerUserName
            },
        trigger () {
      const bar = this.$refs.bar

      bar.start()

      this.timer = setTimeout(() => {
        if (this.$refs.bar) {
          this.$refs.bar.stop()
        }
      }, Math.random() * 3000 + 1000)},
    
         async uchart(){  {
             this.getUsername();
        let data = [];
        console.log(this.username);
        var chartDom = document.getElementById('main1');
var myChart = echarts.init(chartDom);
var option;


       
        await this.$axios.get("http://127.0.0.1:8000/user/user_genre/",{
          params:{
           username:this.$route.query.username
          }
        })
        .then(function(response){
          data = response.data;
          console.log(data);
        }).catch((error) => {
            console.log(error);
        })
        console.log(data);
        this.chart = data;
        console.log
        console.log(233,this.chart);
        option = {
  tooltip: {
    trigger: 'item'
  },
  legend: {
    bottom: '0%',
    left: 'center',
    type:'scroll'
  },
  series: [
    {
      name: 'Access From',
      type: 'pie',
      radius: ['40%', '70%'],
      avoidLabelOverlap: false,
      itemStyle: {
        borderRadius: 10,
        borderColor: '#fff',
        borderWidth: 2
      },
      label: {
        show: false,
        position: 'center'
      },
      emphasis: {
        label: {
          show: true,
          fontSize: '40',
          fontWeight: 'bold'
        }
      },
      labelLine: {
        show: true
      },
      data: this.chart
    }
  ]
};

option && myChart.setOption(option);
        return this.chart;}
      },
    },
    mounted(){
      this.chart=this.uchart()
      this.username = this.$route.query.username;
      //var echarts = require('echarts')
      //var myChart = echarts.init(document.getElementById('main1'))
      //var option
    // 指定图表的配置项和数据
    // 使用刚指定的配置项和数据显示图表。
    //myChart.setOption(option)
   },
  };
</script>