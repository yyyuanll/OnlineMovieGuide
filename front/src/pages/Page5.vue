<template>
  <div>
    <div class="ALL">
    <div class="all">
      <div class="af">Genre</div>
      <el-select v-model="value1" placeholder="genre..." class="as">
        <el-option
          v-for="item in options1"
          :key="item.value"
          :label="item.value"
          :value="item.value">
        </el-option>
      </el-select>
    </div>
    <div class="all">
      <div class="af">Contry</div>
      <el-select v-model="value2" placeholder="contry..." class="as">
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
      <el-select v-model="value3" placeholder="language..." class="as">
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
      <el-select v-model="value4" placeholder="imdbrating..." class="as">
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
      <el-select v-model="value5" placeholder="released..." class="as">
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
      <el-select v-model="value6" placeholder="rated..." class="as">
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
      <el-col v-for="(data) in movielist" :key="data.label" :value="data.value" :span="5.5" style="background:none">
        <div class="grid-content bg-purple" />
        <el-card class="box-card" style="margin-top:20px;padding:0px">
          <img :src="data.img" class="image" style="height:230px;width:160px">
          <div style="padding: 0px;text-align: center;margin-top:10px">
            <router-link to="page-detail" class="link">
              {{data.title}}
            </router-link>
          </div>
        </el-card>
      </el-col>
    </div>
  </div>
</template>

<script>
export default {
  data(){
    return{
      options1:[
        {value: 'All'},
        {value: 'Drama'}, {value: 'Comedy'}, {value: 'Action'}, {value: 'Romance'}, {value: 'Ctime'},
        {value: 'Triller'},{value: 'Adventure'}, {value: 'Documentary'}, {value: 'Horror'}, {value: 'Fantasy'},
        {value: 'Biography'},{value: 'Mystery'}, {value: 'Family'}, {value: 'Sci-Fi'}, {value: 'Music'},
        {value: 'Animation'},{value: 'History'}, {value: 'Sport'}, {value: 'War'}, {value: 'Others'}, 
      ],
      value1:'',
      options2:[
        {value: 'All'},
        {value: 'China'}, {value: 'USA'}, {value: 'UK'}, {value: 'Hong Kong'}, {value: 'France'},{value: 'Germany'},
        {value: 'Janpa'},{value: 'South Korea'}, {value: 'Italy'}, {value: 'Australia'}, {value: 'Russian'},
        {value: 'Spain'},{value: 'India'}, {value: 'Canada'}, {value: 'South African'}, {value: 'Mexico'},
        {value: 'Others'}
      ],
      value2:'',
      options3:[
        {value: 'All'},
        {value: 'English'}, {value: 'Spanish'}, {value: 'French'}, {value: 'Hindi'}, {value: 'German'},
        {value: 'Italian'}, {value: 'Russian'}, {value: 'Japanese'}, {value: 'Mandarin'}, {value: 'Arabic'},
        {value: 'Portuguese'}, {value: 'Cantonese'}, {value: 'Korean'}, {value: 'Latin'}, {value: 'Hebrew'},
        {value: 'Urdu'}, {value: 'Greek'}, {value: 'Chinese'}, {value: 'Others'}
      ],
      value3:'',
      options4:[
        {value: 'All'},
        {value: '0.0--1.0'}, {value: '1.0--2.0'}, {value: '2.0--3.0'}, {value: '3.0--4.0'}, {value: '4.0--5.0'},
        {value: '5.0--6.0'}, {value: '6.0--7.0'}, {value: '7.0--8.0'}, {value: '8.0--9.0'}, {value: '9.0--10.0'},
      ],
      value4:'',
      options5:[
        {value: 'All'},
        {value: '2010--2020'}, {value: '2000--2010'}, {value: '1990--2000'}, {value: '1980-1990'}
      ],
      value5:'',
      options6:[
        {value: "All"},
        {value: 'R'}, {value: 'PG-13'}, {value: 'PG'}, {value: 'G'}, {value: 'NC-17'},{value: 'UR/NR'},
        {value: 'Others'}
      ],
      value6:'',
      movielist:[
        {"img":'https://s2.loli.net/2021/12/11/FiKM5GTe9hXJ1tS.jpg', "title":"The Lion King"},
        {"img":'https://s2.loli.net/2021/12/11/kP2xYZbRUo9aJNm.jpg', "title":"Legend"},
        {"img":'https://s2.loli.net/2021/12/11/gTc6LajV82pEsy3.jpg', "title":"Enemy"},
        {"img":'https://s2.loli.net/2021/12/11/5yLZpcbwrfC8F6U.jpg', "title":"MELEFLOVE"},
        {"img":'https://s2.loli.net/2021/12/11/FiKM5GTe9hXJ1tS.jpg', "title":"The Lion King"},
        {"img":'https://s2.loli.net/2021/12/11/kP2xYZbRUo9aJNm.jpg', "title":"Legend"},
        {"img":'https://s2.loli.net/2021/12/11/FiKM5GTe9hXJ1tS.jpg', "title":"The Lion King"},
        {"img":'https://s2.loli.net/2021/12/11/kP2xYZbRUo9aJNm.jpg', "title":"Legend"},
        {"img":'https://s2.loli.net/2021/12/11/gTc6LajV82pEsy3.jpg', "title":"Enemy"},
        {"img":'https://s2.loli.net/2021/12/11/5yLZpcbwrfC8F6U.jpg', "title":"MELEFLOVE"},
        {"img":'https://s2.loli.net/2021/12/11/FiKM5GTe9hXJ1tS.jpg', "title":"The Lion King"}
      ]
    }
  }
}
</script>

<style>
.af{
  margin-top:50px;
  font-size: 15px;
  float: left;
}

.all{
  margin-left: 90px;
  display: inline-block;
  width: 350px;
}

.ALL{
  white-space: nowrap;
}

.as{
  margin-top: 45px;
  margin-left: 20px;
}

.movie{
  margin-left: 90px;
}
</style>