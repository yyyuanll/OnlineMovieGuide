<template>
  <div>
      <q-ajax-bar
      ref="bar"
      position="bottom"
      color="cyan-2"
      size="10px"
     
    />
    <div class="search_" style="position:relative;right:-2.5%;margin-bottom:16px">
      <input v-model="search_text" class="input_" type="text" placeholder="Please input movie name" style="padding-left:12px;font-size:16px"/>
      <button class="button_" @click="upload()" style="margin-left:16px">search</button>
    </div>
    <div class="movie_">
      <el-col v-for="(data) in movielist.slice(1)" :key="data.label" :value="data.value" :span="5.5" style="background:none">
      <div class="grid-content bg-purple" />
      <el-card class="box-card" style="margin:10px;padding:0px;background:#ffffff;height:320px">
      <router-link :to="{name:'MovieDetails',query:{imdbid: data.imdbid,username: username}}" class="link">
      <img :src="data.img" class="image" style="height:230px;width:160px">
        <div :id="data.id" class="ht" style="padding: 0px;margin-top:10px;width:160px">
          {{data.title}}
        </div>
      </router-link>
      </el-card>
      </el-col>
    </div>
  </div>
</template>

<script>
export default {
  data(){
    return{
      search_text:'',
      username: null,
      movielist:[],
    }
  },
  mounted () {
    document.querySelector("body").style.backgroundImage =
      "url('https://s2.loli.net/2021/12/17/1atOwnYbEMJGPsc.jpg') ";
      document.querySelector("body").style.backgroundAttachment= 'fixed';
      document.querySelector("body").style.backgroundSize= 'cover';
      document.querySelector("body").style.backgroundPosition= 'center';
      this.username = this.$route.query.username;
  },
  methods:{
    async upload(){ 
        let data = [];
        console.log(this.search_text);
       
        await this.$axios.get("http://127.0.0.1:8000/movies/search/",{
          params:{
            search:this.search_text
          }
        })
        .then(function(response){
          data = response.data;
          console.log(data);
        }).catch((error) => {
            console.log(error);
        })
        console.log(data);
        this.movielist = data;
        return this.movielist;
      },
  }  
}
</script>

<style>
.el-card__body {
  padding: 15px;
}

.el-card{
  background-color: transparent;
}

.sf{
  margin-top:60px;
  font-size: 15px;
  float: left;
}

.search{
  margin-left: 90px;
  display: inline-block;
  width: 350px;
}

.link{
  text-decoration: none;
  color: #000;
}

.SEARCH{
  white-space: nowrap;
  margin-left: 90px;
  display: table;
  width: 90%;
  margin-top:-20px;
}

.ss{
  margin-top: 45px;
  margin-left: 20px;
}

.movie_{
  margin-left: 90px;
}

.st{
  padding: 0px;
  text-align: center;
  margin-top:10px;
  overflow:hidden;
  white-space: nowrap;
  text-overflow:ellipsis;
  width:150px;
}

.search_{
  margin-top: 30px;
  margin-left: 300px;
  width: 90%;
}

.input_{
  margin: 0 auto;
  border-radius:6px;
  border-color:  #eee;
  width:500px;
  height:35px;
}

.button_{
  border-radius: 10px;
  height: 30px;
  width: 65px;
  margin-right: -50px;
  background-color: transparent;
  text-align: center;
}

.button_:hover{
  background-color:#A9A9A9;
}
</style>