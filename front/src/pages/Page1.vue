<template>
  <div class="command">
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
</template>

<script>
export default {
  data(){
    return{
      movielist:[
        {"img":'https://s2.loli.net/2021/12/11/FiKM5GTe9hXJ1tS.jpg', "title":"The Lion King"},
        {"img":'https://s2.loli.net/2021/12/11/kP2xYZbRUo9aJNm.jpg', "title":"Legend"},
        {"img":'https://s2.loli.net/2021/12/11/gTc6LajV82pEsy3.jpg', "title":"Enemy"},
        {"img":'https://s2.loli.net/2021/12/11/5yLZpcbwrfC8F6U.jpg', "title":"MELEFLOVE"},
        {"img":'https://s2.loli.net/2021/12/11/FiKM5GTe9hXJ1tS.jpg', "title":"The Lion King"},
        {"img":'https://s2.loli.net/2021/12/11/kP2xYZbRUo9aJNm.jpg', "title":"Legend"},
        {"img":'https://s2.loli.net/2021/12/11/gTc6LajV82pEsy3.jpg', "title":"Enemy"},
        {"img":'https://s2.loli.net/2021/12/11/5yLZpcbwrfC8F6U.jpg', "title":"MELEFLOVE"},
        {"img":'https://s2.loli.net/2021/12/11/FiKM5GTe9hXJ1tS.jpg', "title":"The Lion King"},
        {"img":'https://s2.loli.net/2021/12/11/kP2xYZbRUo9aJNm.jpg', "title":"Legend"},
        {"img":'https://s2.loli.net/2021/12/11/gTc6LajV82pEsy3.jpg', "title":"Enemy"},
        {"img":'https://s2.loli.net/2021/12/11/5yLZpcbwrfC8F6U.jpg', "title":"MELEFLOVE"},
        {"img":'https://s2.loli.net/2021/12/11/FiKM5GTe9hXJ1tS.jpg', "title":"The Lion King"},
        {"img":'https://s2.loli.net/2021/12/11/kP2xYZbRUo9aJNm.jpg', "title":"Legend"},
        {"img":'https://s2.loli.net/2021/12/11/gTc6LajV82pEsy3.jpg', "title":"Enemy"},
        {"img":'https://s2.loli.net/2021/12/11/5yLZpcbwrfC8F6U.jpg', "title":"MELEFLOVE"},
        {"img":'https://s2.loli.net/2021/12/11/FiKM5GTe9hXJ1tS.jpg', "title":"The Lion King"},
        {"img":'https://s2.loli.net/2021/12/11/kP2xYZbRUo9aJNm.jpg', "title":"Legend"},
        {"img":'https://s2.loli.net/2021/12/11/gTc6LajV82pEsy3.jpg', "title":"Enemy"},
        {"img":'https://s2.loli.net/2021/12/11/5yLZpcbwrfC8F6U.jpg', "title":"MELEFLOVE"},
        {"img":'https://s2.loli.net/2021/12/11/FiKM5GTe9hXJ1tS.jpg', "title":"The Lion King"},
        {"img":'https://s2.loli.net/2021/12/11/kP2xYZbRUo9aJNm.jpg', "title":"Legend"},
        {"img":'https://s2.loli.net/2021/12/11/gTc6LajV82pEsy3.jpg', "title":"Enemy"},
        {"img":'https://s2.loli.net/2021/12/11/5yLZpcbwrfC8F6U.jpg', "title":"MELEFLOVE"}
      ],
      movietype:'all',  
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
.command{
  margin-left: 90px;
}
</style>