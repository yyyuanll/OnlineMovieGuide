
<template>
  <div class="oscar">
      <q-ajax-bar
      ref="bar"
      position="bottom"
      color="cyan-2"
      size="10px"
     
    />
    <div class="of" style="float:left">Select the year</div>
    <el-form>
        <el-select v-model="value" @change="upload()" placeholder="2020..." class="os">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.value"
            :value="item.value">
          </el-option>
        </el-select>
    </el-form>
    <div v-if="this.length >= 1" style="background-color:white;width:95%;height:280px;margin-top:30px;display:inline-block">
      <div style="float:left;margin-left:10px;margin-top:20px;padding:0 30px">
        <img :src="tabledata[0].url" style="height:240px">
      </div>
      <div>
        <div><font size="6"><strong>{{tabledata[0].award}}</strong></font></div>
        <div style="margin-top:6px"><font size="4"><strong>Name</strong>: {{tabledata[0].name}}</font></div>
        <div style="margin-top:6px"><font size="4"><strong>Movie name</strong>: {{tabledata[0].movie_name}}</font></div>
        <div style="margin-top:6px"><font size="4"><strong>Character name</strong>: {{tabledata[0].character_name}}</font></div>
        <div style="margin-top:6px"><font size="4"><strong>Representitive</strong>: {{tabledata[0].representitive}}</font></div>
        <div style="margin-top:6px; width:95%"><font size="4"><strong>Introduction</strong>: {{tabledata[0].introduction}}</font></div>
      </div>
    </div>
    <div v-if="this.length >= 2" style="background-color:white;width:95%;height:280px;margin-top:30px;display:inline-block">
      <div style="float:left;margin-left:10px;margin-top:20px;padding:0 30px">
        <img :src="tabledata[1].url" style="height:240px">
      </div>
      <div>
        <div><font size="6"><strong>{{tabledata[1].award}}</strong></font></div>
        <div style="margin-top:6px"><font size="4"><strong>Name</strong>: {{tabledata[1].name}}</font></div>
        <div style="margin-top:6px"><font size="4"><strong>Movie name</strong>: {{tabledata[1].movie_name}}</font></div>
        <div style="margin-top:6px"><font size="4"><strong>Character name</strong>: {{tabledata[1].character_name}}</font></div>
        <div style="margin-top:6px"><font size="4"><strong>Representitive</strong>: {{tabledata[1].representitive}}</font></div>
        <div style="margin-top:6px; width:95%"><font size="4"><strong>Introduction</strong>: {{tabledata[1].introduction}}</font></div>
      </div>
    </div>
    <div v-if="this.length >= 3" style="background-color:white;width:95%;height:280px;margin-top:30px;display:inline-block">
      <div style="float:left;margin-left:10px;margin-top:20px;padding:0 30px">
        <img :src="tabledata[2].url" style="height:240px">
      </div>
      <div>
        <div><font size="6"><strong>{{tabledata[2].award}}</strong></font></div>
        <div style="margin-top:6px"><font size="4"><strong>Name</strong>: {{tabledata[2].name}}</font></div>
        <div style="margin-top:6px"><font size="4"><strong>Movie name</strong>: {{tabledata[2].movie_name}}</font></div>
        <div style="margin-top:6px"><font size="4"><strong>Character name</strong>: {{tabledata[2].character_name}}</font></div>
        <div style="margin-top:6px"><font size="4"><strong>Representitive</strong>: {{tabledata[2].representitive}}</font></div>
        <div style="margin-top:6px; width:95%"><font size="4"><strong>Introduction</strong>: {{tabledata[2].introduction}}</font></div>
      </div>
    </div>
    <div v-if="this.length >= 4" style="background-color:white;width:95%;height:280px;margin-top:30px;display:inline-block">
      <div style="float:left;margin-left:10px;margin-top:20px;padding:0 30px">
        <img :src="tabledata[3].url" style="height:240px">
      </div>
      <div>
        <div><font size="6"><strong>{{tabledata[3].award}}</strong></font></div>
        <div style="margin-top:6px"><font size="4"><strong>Name</strong>: {{tabledata[3].name}}</font></div>
        <div style="margin-top:6px"><font size="4"><strong>Movie name</strong>: {{tabledata[3].movie_name}}</font></div>
        <div style="margin-top:6px"><font size="4"><strong>Character name</strong>: {{tabledata[3].character_name}}</font></div>
        <div style="margin-top:6px"><font size="4"><strong>Representitive</strong>: {{tabledata[3].representitive}}</font></div>
        <div style="margin-top:6px; width:95%"><font size="4"><strong>Introduction</strong>: {{tabledata[3].introduction}}</font></div>
      </div>
    </div>
    <div v-if="this.length >= 5" style="background-color:white;width:95%;height:280px;margin-top:30px;display:inline-block">
      <div style="float:left;margin-left:10px;margin-top:20px;padding:0 30px">
        <img :src="tabledata[4].url" style="height:240px">
      </div>
      <div>
        <div><font size="6"><strong>{{tabledata[4].award}}</strong></font></div>
        <div style="margin-top:6px"><font size="4"><strong>Title</strong>: {{tabledata[4].title}}</font></div>
        <div style="margin-top:6px"><font size="4"><strong>Director</strong>: {{tabledata[4].director}}</font></div>
        <div style="margin-top:6px"><font size="4"><strong>Actors</strong>: {{tabledata[4].actors}}</font></div>
        <div style="margin-top:6px"><font size="4"><strong>Genre</strong>: {{tabledata[4].genre}}</font></div>
        <div style="margin-top:6px; width:95%"><font size="4"><strong>Introduction</strong>: {{tabledata[4].introduction}}</font></div>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from 'axios';
import { axiosInstance } from 'src/boot/axios';

export default {
   data() {
      return {
        username: null,
        options: [{value: '2021'},
          {value: '2020'}, {value: '2019'}, {value: '2018'}, {value: '2017'}, {value: '2016'},{value: '2015'}, 
          {value: '2014'}, {value: '2013'}, {value: '2012'}, {value: '2011'}, {value: '2010'},{value: '2009'},
          {value: '2008'}, {value: '2007'}, {value: '2006'}, {value: '2005'}, {value: '2004'},{value: '2003'}, 
          {value: '2002'}, {value: '2001'}, {value: '2000'}, {value: '1999'}, {value: '1998'},{value: '1997'},
          {value: '1996'}, {value: '1995'}, {value: '1994'}, {value: '1993'}, {value: '1992'},{value: '1991'}, 
          {value: '1990'}, {value: '1989'}, {value: '1988'}, {value: '1987'}, {value: '1986'},{value: '1985'},
          {value: '1984'}, {value: '1983'}, {value: '1982'}, {value: '1981'}, {value: '1980'},{value: '1979'}, 
          {value: '1978'}, {value: '1977'}, {value: '1976'}, {value: '1975'}, {value: '1974'},{value: '1973'},
          {value: '1972'}, {value: '1971'}, {value: '1970'}, {value: '1969'}, {value: '1968'},{value: '1967'}, 
          {value: '1966'}, {value: '1965'}, {value: '1964'}, {value: '1963'}, {value: '1962'},{value: '1961'},
          {value: '1960'}, {value: '1959'}, {value: '1958'}, {value: '1957'}, {value: '1956'},{value: '1955'}, 
          {value: '1954'}, {value: '1953'}, {value: '1952'}, {value: '1951'}, {value: '1950'},{value: '1949'},
          {value: '1948'}, {value: '1947'}, {value: '1946'}, {value: '1945'}, {value: '1944'},{value: '1943'}, 
          {value: '1942'}, {value: '1941'}, {value: '1940'}, {value: '1939'}, {value: '1938'},{value: '1937'},
          {value: '1936'}, {value: '1935'}, {value: '1934'}, {value: '1933'}, {value: '1932'},{value: '1931'}, 
          {value: '1930'}, {value: '1929'},
          ],
        value: '2021',
        tabledata:[],
        length:0
      }
    },
    methods:{
         async upload(){
          console.log(this.value);
          let data = [];
        const bar = this.$refs.bar;
        bar.start();


          await this.$axios.get("http://127.0.0.1:8000/oscar/",{
            params:{
              year:this.value,
            }
          })
          .then(function(response){
            console.log(response.data)
            data = response.data;
          }).catch((error) => {
              console.log(error)
          })
          this.tabledata = data;
          this.length = this.tabledata.length;
          console.log(this.length);
          console.log(this.tabledata)
          this.bar.stop();
          return this.tabledata
        }
    },
    mounted () {
    document.querySelector("body").style.backgroundImage =
      "url('https://s2.loli.net/2021/12/17/1atOwnYbEMJGPsc.jpg') ";
      document.querySelector("body").style.backgroundAttachment= 'fixed';
      document.querySelector("body").style.backgroundSize= 'cover';
      document.querySelector("body").style.backgroundPosition= 'center';
      this.tabledata = this.upload(this.value)
      this.username = this.$route.query.username;
  },
}
</script>

<style>
.of{
  margin-top:50px;
  font-size: 20px;
}
.os{
  margin-top: 45px;
  margin-left: 20px;
}
.oscar{
  margin-left: 90px;
}
.osbutton{
  margin-left: 40px;
  border-radius: 6px;
}

.ot{
  overflow : hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
}
</style>
