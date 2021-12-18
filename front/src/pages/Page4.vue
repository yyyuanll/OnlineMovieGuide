<template>
  <div class="oscar">
    <div class="of" style="float:left">Select the year</div>
    <el-select v-model="value" placeholder="2020..." class="os">
      <el-option
        v-for="item in options"
        :key="item.value"
        :label="item.value"
        :value="item.value">
      </el-option>
    </el-select>
    <div class="of">The Best Actor</div>
    <el-table
      :data="tableData1"
      style="width: 90%">
      <el-table-column
        prop="year"
        label="Year"
        width="80">
      </el-table-column>
      <el-table-column
        prop="name"
        label="Name"
        width="80">
      </el-table-column>
      <el-table-column
        prop="img_actor"
        label="Img_actor"
        width="150">
      </el-table-column>
      <el-table-column
        prop="introduction"
        label="Introduction"
        width="500">
      </el-table-column>
      <el-table-column
        prop="representitive"
        label="Representitive"
        width="200">
      </el-table-column>
      <el-table-column
        prop="movie_name"
        label="Movie_name"
        width="120">
      </el-table-column>
      <el-table-column
        prop="character_name"
        label="Character_name"
        width="150">
      </el-table-column>
    </el-table>
    <div class="of">The Best Actress</div>
    <el-table
      :data="tableData2"
      style="width: 90%">
      <el-table-column
        prop="year"
        label="Year"
        width="80">
      </el-table-column>
      <el-table-column
        prop="name"
        label="Name"
        width="80">
      </el-table-column>
      <el-table-column
        prop="img_actor"
        label="Img_actor"
        width="150">
      </el-table-column>
      <el-table-column
        prop="introduction"
        label="Introduction"
        width="500">
      </el-table-column>
      <el-table-column
        prop="representitive"
        label="Representitive"
        width="200">
      </el-table-column>
      <el-table-column
        prop="movie_name"
        label="Movie_name"
        width="120">
      </el-table-column>
      <el-table-column
        prop="character_name"
        label="Character_name"
        width="150">
      </el-table-column>
    </el-table>
    <div class="of">The Best Supporting Actor</div>
    <el-table
      :data="tableData3"
      style="width: 90%">
      <el-table-column
        prop="year"
        label="Year"
        width="80">
      </el-table-column>
      <el-table-column
        prop="name"
        label="Name"
        width="80">
      </el-table-column>
      <el-table-column
        prop="img_actor"
        label="Img_actor"
        width="150">
      </el-table-column>
      <el-table-column
        prop="introduction"
        label="Introduction"
        width="500">
      </el-table-column>
      <el-table-column
        prop="representitive"
        label="Representitive"
        width="200">
      </el-table-column>
      <el-table-column
        prop="movie_name"
        label="Movie_name"
        width="120">
      </el-table-column>
      <el-table-column
        prop="character_name"
        label="Character_name"
        width="150">
      </el-table-column>
    </el-table>
    <div class="of">The Best Supporting Actress</div>
    <el-table
      :data="tableData4"
      style="width: 90%">
      <el-table-column
        prop="year"
        label="Year"
        width="80">
      </el-table-column>
      <el-table-column
        prop="name"
        label="Name"
        width="80">
      </el-table-column>
      <el-table-column
        prop="img_actor"
        label="Img_actor"
        width="150">
      </el-table-column>
      <el-table-column
        prop="introduction"
        label="Introduction"
        width="500">
      </el-table-column>
      <el-table-column
        prop="representitive"
        label="Representitive"
        width="200">
      </el-table-column>
      <el-table-column
        prop="movie_name"
        label="Movie_name"
        width="120">
      </el-table-column>
      <el-table-column
        prop="character_name"
        label="Character_name"
        width="150">
      </el-table-column>
    </el-table>
    <div class="of">The Best Picture</div>
    <el-table
      :data="tableData5"
      style="width: 90%">
      <el-table-column
        prop="year"
        label="Year"
        width="80">
      </el-table-column>
      <el-table-column
        prop="title"
        label="Title"
        width="80">
      </el-table-column>
      <el-table-column
        prop="img_movie"
        label="Img_movie"
        width="150">
      </el-table-column>
      <el-table-column
        prop="introduction"
        label="Introduction"
        width="500">
      </el-table-column>
      <el-table-column
        prop="director"
        label="Director"
        width="150">
      </el-table-column>
      <el-table-column
        prop="actors"
        label="Actors"
        width="150">
      </el-table-column>
      <el-table-column
        prop="genre"
        label="Genre"
        width="150">
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
   data() {
      return {
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
        tableData1: [{
            year: '2021',
            name: 'Anthony Hopkins',
            img_actor: '',
            introduction: 'Anthony Hopkins was born on December 31, 1937, in Margam, Wales, to Muriel Anne (Yeats) and Richard Arthur Hopkins, a baker. His parents were both of half Welsh and half English descent. Influenced by Richard Burton, he decided to study at College of Music and Drama and graduated in 1957. In 1965, ...',
            representitive: 'The Silence of the Lambs',
            movie_name: 'The Father',
            character_name: 'Anthony'
          }],
          tableData2: [{
            year: '2021',
            name: 'Anthony Hopkins',
            img_actor: '',
            introduction: 'Anthony Hopkins was born on December 31, 1937, in Margam, Wales, to Muriel Anne (Yeats) and Richard Arthur Hopkins, a baker. His parents were both of half Welsh and half English descent. Influenced by Richard Burton, he decided to study at College of Music and Drama and graduated in 1957. In 1965, ...',
            representitive: 'The Silence of the Lambs',
            movie_name: 'The Father',
            character_name: 'Anthony'
          }],
          tableData3: [{
            year: '2021',
            name: 'Anthony Hopkins',
            img_actor: '',
            introduction: 'Anthony Hopkins was born on December 31, 1937, in Margam, Wales, to Muriel Anne (Yeats) and Richard Arthur Hopkins, a baker. His parents were both of half Welsh and half English descent. Influenced by Richard Burton, he decided to study at College of Music and Drama and graduated in 1957. In 1965, ...',
            representitive: 'The Silence of the Lambs',
            movie_name: 'The Father',
            character_name: 'Anthony'
          }],
          tableData4: [{
            year: '2021',
            name: 'Anthony Hopkins',
            img_actor: '',
            introduction: 'Anthony Hopkins was born on December 31, 1937, in Margam, Wales, to Muriel Anne (Yeats) and Richard Arthur Hopkins, a baker. His parents were both of half Welsh and half English descent. Influenced by Richard Burton, he decided to study at College of Music and Drama and graduated in 1957. In 1965, ...',
            representitive: 'The Silence of the Lambs',
            movie_name: 'The Father',
            character_name: 'Anthony'
          }],
          tableData5: [{
            year: '2021',
            title: 'Nomadland',
            img_movie: '',
            introduction: 'A woman in her sixties, after losing everything in the Great Recession, embarks on a journey through the American West, living as a van-dwelling modern-day nomad.',
            director: 'director',
            actors: 'Frances McDormand,David Strathairn,Linda May,Gay DeForest',
            genre: 'Drama'
          }]
      }
    }
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
</style>