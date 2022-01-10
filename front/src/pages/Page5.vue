
<template>
  <div>
    <div class="ALL">
        <q-ajax-bar
      ref="bar"
      position="bottom"
      color="cyan-2"
      size="10px"
      
    />
    <div class="all">
      <div class="af">Genre</div>
      <el-select v-model="Genre" @change="upload()" placeholder="genre..." class="as">
        <el-option
          v-for="item in options1"
          :key="item.value"
          :label="item.value"
          :value="item.value">
        </el-option>
      </el-select>
    </div>
    <div class="all">
      <div class="af">Country</div>
      <el-select v-model="Country" @change="upload()" placeholder="contry..." class="as">
        <el-option
          v-for="item in options2"
          :key="item.value"
          :label="item.value"
          :value="item.value">
        </el-option>
      </el-select>
    </div>
    <div class="all">
      <div class="af">Language</div>
      <el-select v-model="Language" @change="upload()" placeholder="language..." class="as">
        <el-option
          v-for="item in options3"
          :key="item.value"
          :label="item.value"
          :value="item.value">
        </el-option>
      </el-select>
    </div>
    </div>
    <div class="ALL">
    <div class="all">
      <div class="af">IMDBRating</div>
      <el-select v-model="IMDBRating" @change="upload()" placeholder="imdbrating..." class="as">
        <el-option
          v-for="item in options4"
          :key="item.value"
          :label="item.value"
          :value="item.value">
        </el-option>
      </el-select>
    </div>
    <div class="all">
      <div class="af">Released</div>
      <el-select v-model="Released" @change="upload()" placeholder="released..." class="as">
        <el-option
          v-for="item in options5"
          :key="item.value"
          :label="item.value"
          :value="item.value">
        </el-option>
      </el-select>
    </div>
    <div class="all">
      <div class="af">Rated</div>
      <el-select v-model="Rated" @change="upload()" placeholder="rated..." class="as">
        <el-option
          v-for="item in options6"
          :key="item.value"
          :label="item.value"
          :value="item.value">
        </el-option>
      </el-select>
    </div>
    </div>
    <div class="movie">
      <el-col v-for="(data) in movielist.slice(1)" :key="data.label" :value="data.value" :span="5.5" style="background:none">
        <div class="grid-content bg-purple" />
        <el-card class="box-card" style="margin:10px;padding:0px;background:#ffffff;height:320px">
          <img :src="data.img" class="image" style="height:230px;width:160px">
          <router-link :to="{name:'MovieDetails',query:{imdbid: data.imdbid,username: username}}" class="link">
            <div :id="data.id" class="at" style="padding: 0px;margin-top:10px;width:160px">  
              {{data.title}}
            </div>
          </router-link>
        </el-card>
      </el-col>
    </div>
    <div class="page-bar">
      <ul>
        <li v-if="cur>1"><a v-on:click="cur--,pageClick()">previous page</a></li>
        <li v-if="cur==1"><a class="banclick">previous page</a></li>
        <li v-for="index in indexs"  :key="index" v-bind:class="{ 'active': cur == index}">
            <a v-on:click="btnClick(index)">{{ index }}</a>
        </li>
        <li v-if="cur<all"><a v-on:click="cur++,pageClick()">next page</a></li>
        <li v-if="cur == all"><a class="banclick">next page</a></li>
        <li><a>total<i>{{all}}</i>pages</a></li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data(){
    return{
      username: null,
      options1:[
        {value: 'All'},
        {value: 'Drama'}, {value: 'Comedy'}, {value: 'Action'}, {value: 'Romance'}, {value: 'Crime'},
        {value: 'Thiller'},{value: 'Adventure'}, {value: 'Documentary'}, {value: 'Horror'}, {value: 'Fantasy'},
        {value: 'Biography'},{value: 'Mystery'}, {value: 'Family'}, {value: 'Sci-Fi'}, {value: 'Music'},
        {value: 'Animation'},{value: 'History'}, {value: 'Sport'}, {value: 'War'}, {value: 'Others'}, 
      ],
      options2:[
        {value: 'All'},
        {value: 'China'}, {value: 'USA'}, {value: 'UK'}, {value: 'Hong Kong'}, {value: 'France'},{value: 'Germany'},
        {value: 'Japan'},{value: 'South Korea'}, {value: 'Italy'}, {value: 'Australia'}, {value: 'Russia'},
        {value: 'Spain'},{value: 'India'}, {value: 'Canada'}, {value: 'South Africa'}, {value: 'Mexico'},
        {value: 'Others'}
      ],
      options3:[
        {value: 'All'},
        {value: 'English'}, {value: 'Spanish'}, {value: 'French'}, {value: 'Hindi'}, {value: 'German'},
        {value: 'Italian'}, {value: 'Russian'}, {value: 'Japanese'}, {value: 'Mandarin'}, {value: 'Arabic'},
        {value: 'Portuguese'}, {value: 'Cantonese'}, {value: 'Korean'}, {value: 'Latin'}, {value: 'Hebrew'},
        {value: 'Urdu'}, {value: 'Greek'}, {value: 'Chinese'}, {value: 'Others'}
      ],
      options4:[
        {value: 'All'},
        {value: '0.0--1.0'}, {value: '1.0--2.0'}, {value: '2.0--3.0'}, {value: '3.0--4.0'}, {value: '4.0--5.0'},
        {value: '5.0--6.0'}, {value: '6.0--7.0'}, {value: '7.0--8.0'}, {value: '8.0--9.0'}, {value: '9.0--10.0'},
      ],
      options5:[
        {value: 'All'},
        {value: '2010--2020'}, {value: '2000--2010'}, {value: '1990--2000'}, {value: '1980--1990'}
      ],
      options6:[
        {value: "All"},
        {value: 'R'}, {value: 'PG-13'}, {value: 'PG'}, {value: 'G'}, {value: 'NC-17'},{value: 'UR/NR'},
        {value: 'Others'}
      ],
      Genre:'All',
      Country:'All',
      Language:'All',
      IMDBRating:'All',
      Released:'All',
      Rated:'All',
      index:1,
      pagesize:28,
      all:20,
      cur:1,
      movielist:[]
    }
  },
  mounted () {
    document.querySelector("body").style.backgroundImage =
      "url('https://s2.loli.net/2021/12/17/1atOwnYbEMJGPsc.jpg') ";
      document.querySelector("body").style.backgroundAttachment= 'fixed';
      document.querySelector("body").style.backgroundSize= 'cover';
      document.querySelector("body").style.backgroundPosition= 'center';
      this.movielist = this.upload();
      this.username = this.$route.query.username;
  },
  methods:{
    async upload(){ 
        let data = [];
        console.log(this.cur);
        console.log(this.Genre);
        console.log(this.Country);
        console.log(this.Language);
        console.log(this.IMDBRating);
        console.log(this.Released);
        console.log(this.Rated);
        const bar = this.$refs.bar;
        this.bar.start();
       
        await this.$axios.get("http://127.0.0.1:8000/movies/",{
          params:{
            index:this.cur,
            Genre:this.Genre,
            Country:this.Country,
            Language:this.Language,
            IMDBRating:this.IMDBRating,
            Released:this.Released,
            Rated:this.Rated,
          }
        })
        .then(function(response){
          data = response.data;
          console.log(data);
        }).catch((error) => {
            console.log(error);
        })
        console.log(data);
        this.all = data[0].page_number;
        console.log(this.all);
        this.movielist = data;
        this.bar.stop();
        return this.movielist;
      },

    //分页
    btnClick: function(data){//页码点击事件
      if(data != this.cur){
        this.cur = data
      }
      //根据点击页数请求数据
      this.upload();
    },

    pageClick: function(){ //根据点击页数请求数据
      this.upload();
    }
  },

  computed: { //分页
    indexs: function(){
      var left = 1;
      var right = this.all;
      var ar = [];
      if(this.all>= 5){
        if(this.cur > 3 && this.cur < this.all-2){
          left = this.cur - 2
          right = this.cur + 2
        }else{
          if(this.cur<=3){
            left = 1
            right = 5
          }else{
            right = this.all
            left = this.all -4
          }
        }
      }
      while (left <= right){
        ar.push(left)
        left ++
      }
      return ar
    }
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

.af{
  margin-top:60px;
  font-size: 15px;
  float: left;
}

.all{
  margin-left: 90px;
  display: inline-block;
  width: 350px;
}

.link{
  text-decoration: none;
  color: #000;
}

.ALL{
  white-space: nowrap;
  margin-left: 90px;
  display: table;
  width: 90%;
}

.as{
  margin-top: 45px;
  margin-left: 20px;
}

.movie{
  margin-left: 90px;
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

.at{
  padding: 0px;
  text-align: center;
  margin-top:10px;
  overflow:hidden;
  white-space: nowrap;
  text-overflow:ellipsis;
  width:150px;
}

</style>