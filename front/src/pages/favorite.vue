<template>
<el-container style="">
    <el-main style="background:none">
    <div class="page-info">
      <el-col v-for="(data) in movielist" :key="data.label" :value="data.value" :span="5.5" style="background:none">
      <div class="grid-content bg-purple" />
      <el-card class="box-card" style="margin:10px;padding:0px;background:#ffffff;height:320px">
    <router-link :to="{name:'MovieDetails',query:{imdbid: data.imdbid,username:username}}" class="link">
        <img :src="data.image" class="image" style="height:230px;width:160px">
        <div :id="data.id" style="padding: 0px;margin-top:10px;width:160px">
          {{data.title}}
        </div>
      </router-link>
      </el-card>
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
        movielist:[
        {"img":'', "title":""},
        
      ],
       
      }
    },

watch: {
  // 监测路由变化,只要变化了就调用获取路由参数方法将数据存储本组件即可
  '$route': 'getUsername'
},
    mounted () {
    document.querySelector("body").style.backgroundImage =
      "url('https://s2.loli.net/2021/12/17/1atOwnYbEMJGPsc.jpg') ";
      document.querySelector("body").style.backgroundAttachment= 'fixed';
      document.querySelector("body").style.backgroundSize= 'cover';
      document.querySelector("body").style.backgroundPosition= 'center';
      this.movielist = this.favorite();
      this.username = this.$route.query.username;
  },
   methods: {
       async favorite(){ 
        let data = [];
        console.log(this.username);
       
        await this.$axios.get("http://127.0.0.1:8000/user/favorite/",{
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
        this.movielist = data;
        //console.log(this.useravatar);
        return this.movielist;
      },
            getUsername:function(){
                var routerUserName = this.$router.query.username
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