<template>
  <div class="oscar">
    <div class="of" style="float:left">Select the year</div>
    <el-form>
        <el-select v-model="value" @change="upload(value)" placeholder="2020..." class="os">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.value"
            :value="item.value">
          </el-option>
        </el-select>
    </el-form>
    <div class="of">
      <div style="font-weight:bold; font-size:30px">Actor</div>
      <table class="el-table el-table--fit el-table--border table-detail" style="width:90%">
        <thead>
          <tr>
            <td>award</td>
            <td>name</td>
            <td>image</td>
            <td>introduction</td>
            <td>representitive</td>
            <td>movie_name</td>
            <td>character_name</td>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(data) in tabledata" :key="data.label" :value="data.value">
            <div v-if="data.type !== 'BestPicture'">
              <td>{{data.award}}</td>
              <td>{{data.name}}</td>
              <td>
                <img :src="data.url">
              </td>
              <td>{{data.introduction}}</td>
              <td>{{data.representitive}}</td>
              <td>{{data.movie_name}}</td>
              <td>{{data.character_name}}</td>
              </div>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="of">
      <div style="font-weight:bold; font-size:30px">Movie</div>
      <table class="el-table el-table--fit el-table--border table-detail" style="width:90%">
        <thead>
          <tr>
            <td>award</td>
            <td>name</td>
            <td>image</td>
            <td>introduction</td>
            <td>director</td>
            <td>actors</td>
            <td>genre</td>
          </tr>
        </thead>
        <tbody>
          <tr v-for="data in tabledata" :key="data.label" :value="data.value">
            <div v-if="data.type == 'BestPicture'">
              <td>{{data.award}}</td>
              <td>{{data.title}}</td>
              <td>
                <img :src="data.url">
              </td>
              <td>{{data.introduction}}</td>
              <td>{{data.director}}</td>
              <td>{{data.actors}}</td>
              <td>{{data.genre}}</td>
              </div>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
   data() {
      return {
        username: this.$route.query.username,
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
      }
    },
    methods:{
         async upload(value){
          let formData = new FormData();
          formData["year"] = this.value;
          console.log(this.value);
          console.log(formData);
          let data = [];

          await this.$axios.post("http://127.0.0.1:8000/oscar/",formDatas)
          .then(function(response){
            console.log(response);
            console.log(response.data)
            data = response.data;
            this.$refs.upload.clearFiles();
          }).catch((erroe) => {
              console.log(error)
          })
          this.tabledata = data;
          console.log(this.tabledata)
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
</style>