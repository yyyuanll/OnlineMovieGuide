<template>
<el-container style="">
    <el-main style="">
        <div  id="main1" style="width: 100%;height:100%;"> </div>
    </el-main>
</el-container>
</template>

<script>
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
      username:"Lucas Kim"
      }
    },
    methods:{
       async uchart(){ 
        let data = [];
        console.log(this.username);
       
        await this.$axios.get("http://127.0.0.1:8000/user/user_genre/",{
          params:{
           username:this.username
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
        console.log(this.chart);
        return this.chart;
      },
    },
    mounted(){
      this.chart=this.uchart()
      var echarts = require('echarts')
      var myChart = echarts.init(document.getElementById('main1'))
    // 指定图表的配置项和数据
      var option = {
            //backgroundColor: 'rgb(238,241,246)',
  title: {
    text: 'Favorite Type',
    left: 'center',
    top: 20,
    textStyle: {
      color: '#ccc'
    }
  },
  tooltip: {
    trigger: 'item'
  },
  visualMap: {
    show: false,
    min: 80,
    max: 600,
    inRange: {
      colorLightness: [0, 1]
    }
  },
  series: [
    {
      name: 'Film Type',
      type: 'pie',
      radius: '55%',
      center: ['50%', '50%'],
      data:this.uchart().sort(function (a, b) {
        return a.value - b.value;
      }),
      roseType: 'radius',
      label: {
        color: 'rgba(255, 255, 255, 1)'
      },
      labelLine: {
        lineStyle: {
          color: 'rgba(255, 255, 255, 0.3)'
        },
        smooth: 0.2,
        length: 10,
        length2: 20
      },
      itemStyle: {
        color: '#c23531',
        shadowBlur: 200,
        shadowColor: 'rgba(0, 0, 0, 0.5)'
      },
      animationType: 'scale',
      animationEasing: 'elasticOut',
      animationDelay: function (idx) {
        return Math.random() * 200;
      }
    }
  ]
        };
    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option)
   },
  };
</script>