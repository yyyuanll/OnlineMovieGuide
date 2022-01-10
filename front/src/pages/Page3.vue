<template>
  <div class="new">
    <div class="new_">
      <div class="nf">Genre</div>
      <el-select v-model="Genre" @change="upload()" placeholder="genre..." class="ns">
        <el-option
          v-for="item in options1"
          :key="item.value"
          :label="item.value"
          :value="item.value">
        </el-option>
      </el-select>
    </div>
    <div class="new_">
      <div class="nf">Country</div>
      <el-select v-model="Country" @change="upload()" placeholder="contry..." class="ns">
        <el-option
          v-for="item in options2"
          :key="item.value"
          :label="item.value"
          :value="item.value">
        </el-option>
      </el-select>
    </div>
    <div class="new_">
      <div class="nf">IMDBRating</div>
      <el-select v-model="IMDBRating" @change="upload()" placeholder="imdbrating..." class="ns">
        <el-option
          v-for="item in options3"
          :key="item.value"
          :label="item.value"
          :value="item.value">
        </el-option>
      </el-select>
    </div>
    <div class="page-info">
      <el-col v-for="data in moviesdata.slice(1)" :key="data.imdbid" :value="data.imdbid" :span="5.5" style="background:none">
        <div class="grid-content bg-purple" />
          <el-card class="box-card" style="margin:10px;padding:0px;background:#ffffff;height:320px">
            <router-link :to="{name:'MovieDetails',query:{imdbid: data.imdbid,username: username}}" class="link">
            <img :src="data.img" class="image" style="height:230px;width:160px">
              <div :id="data.imdbid" class="nt" style="padding: 0px;margin-top:10px;width:160px">
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
import Axios from 'axios';
import { axiosInstance } from 'src/boot/axios';

export default {
  data(){
    return{
      moviesdata:[],
      username: null,
      index: 1,
      pagesize:28,
      all: 20, //总页数
      cur: 1, //当前页码
      Genre:'All',
      Country:'All',
      IMDBRating:'All',
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
        {value: '0.0--1.0'}, {value: '1.0--2.0'}, {value: '2.0--3.0'}, {value: '3.0--4.0'}, {value: '4.0--5.0'},
        {value: '5.0--6.0'}, {value: '6.0--7.0'}, {value: '7.0--8.0'}, {value: '8.0--9.0'}, {value: '9.0--10.0'},
      ],
    }
  },
  mounted () {
    document.querySelector("body").style.backgroundImage =
      "url('https://s2.loli.net/2021/12/17/1atOwnYbEMJGPsc.jpg') ";
      document.querySelector("body").style.backgroundAttachment= 'fixed';
      document.querySelector("body").style.backgroundSize= 'cover';
      document.querySelector("body").style.backgroundPosition= 'center';
      this.moviesdata = this.upload();
      this.username = this.$route.query.username;
  },
  methods:{
    //请求数据
      async upload(){ 
        let data = [];
        console.log(this.cur);
        console.log(this.Genre);
        console.log(this.Country);
        console.log(this.IMDBRating);
       
        await this.$axios.get("http://127.0.0.1:8000/new/",{
          params:{
            index:this.cur,
            Genre:this.Genre,
            Country:this.Country,
            IMDBRating:this.IMDBRating
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
        this.moviesdata = data;
        return this.moviedata;
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

.link{
  text-decoration: none;
  color: #000;
}

.new{
  margin-left: 90px;
  display: table;
  width: 90%;
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

.nf{
  margin-top:60px;
  font-size: 15px;
  float: left;
}

.ns{
  margin-top: 45px;
  margin-left: 20px;
}

.new_{
  margin-left: 90px;
  display: inline-block;
  width: 350px;
}

.nt{
  padding: 0px;
  text-align: center;
  margin-top:10px;
  overflow:hidden;
  white-space: nowrap;
  text-overflow:ellipsis;
  width:150px;
}
</style>