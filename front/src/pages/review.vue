<template>
<el-container style="">
    <el-main style="background:none">
    <div class="page-info">
        
      <el-col v-for="(data) in reviewlist" :key="data.movie" :value="data.review" :span="5.6" style="background:none;">
      <div class="grid-content bg-purple" />
         <router-link :to="{name:'MovieDetails',query:{imdbid: data.movie,username:username}}" class="link">
      <el-card class="box-card" style="margin:10px;padding:16px;background:#ffffff;height:auto;width:320px;border-radius:16px">
        <div :id="data.id" style="font-weight:bold;margin-bottom:10px">
          {{data.title}}
        </div>
    <div v-if="data.star != 0">
        <el-rate
  v-model="data.star"
  disabled
  show-score
  text-color="#ff9900"
  style="margin-bottom:10px"
  >
</el-rate>
</div>
    <div v-if="data.review != null" style="margin-bottom:10px">
          {{data.review}}
    </div>
        
      </el-card>
         </router-link>
      </el-col>
    </div>
    </el-main>
</el-container>
</template>

<script>
  export default {
    data() {
      return {
       username:null,
        reviewlist:[
        {"movie":'', title:'',"star":"","review":""},
        
      ],
       
      }
    },

    mounted () {
    document.querySelector("body").style.backgroundImage =
      "url('https://s2.loli.net/2021/12/17/1atOwnYbEMJGPsc.jpg') ";
      document.querySelector("body").style.backgroundAttachment= 'fixed';
      document.querySelector("body").style.backgroundSize= 'cover';
      document.querySelector("body").style.backgroundPosition= 'center';
      this.reviewlist = this.review();
      this.username = this.$route.query.username;
  },
  watch: {
  // 监测路由变化,只要变化了就调用获取路由参数方法将数据存储本组件即可
  '$route': 'history'
},
   methods: {
       async review(){ 
           this.getUsername();
        let data = [];
        console.log(this.username);
       
        await this.$axios.get("http://127.0.0.1:8000/user/review/",{
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
        this.reviewlist = data;
        //console.log(this.useravatar);
        return this.reviewlist;
      },
            getUsername:function(){
                var routerUserName = this.$route.query.username
                this.username = routerUserName
            },}
  };
</script>
<style >
.el-card__body {
    padding: 15px;
}

.el-card{
  background-color: transparent;
}

.link{
  text-decoration: none;
  color: #000;
}
.page-info{
  vertical-align:middle;
}

.page-bar{
  margin-top: 1300px;
  margin-left: 50px;
  vertical-align:middle;
}

ul,li{
  margin: 0px;
  padding: 0px;
}

li{
  list-style: none
}
.page-bar li:first-child>a {
  margin-left: 0px
}

.page-bar a{
  border: 1px solid #ddd;
  text-decoration: none;
  position: relative;
  float: left;
  padding: 6px 12px;
  margin-left: -1px;
  line-height: 1.42857143;
  color: #5D6062;
  cursor: pointer;
  margin-right: 20px;
}

.page-bar a:hover{
  background-color: #eee;
}

.page-bar a.banclick{
  cursor:not-allowed;
}

.page-bar .active a{
  color: #fff;
  cursor: default;
  background-color: #E96463;
  border-color: #E96463;
}

.page-bar i{
  font-style:normal;
  color: #d44950;
  margin: 0px 4px;
  font-size: 12px;
}
</style>