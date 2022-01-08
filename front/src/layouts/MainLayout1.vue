<template>
  <q-layout view="hHh lpR lFf" >

    <q-header elevated class="head1" height-hint="98">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="left = !left" />

        <q-toolbar-title>
            <img
              src="https://i.loli.net/2021/12/01/DI1slReF5KzLm7p.png"
              style="width: 130px; height: 100px; margin-left:20px"
            >
            <q-tabs align="center" class="head_voc">
              <q-route-tab :to="{path:'/page1',query:{username: this.$route.query.username}}" label="Command" />
              <q-route-tab :to="{path:'/page2',query:{username: this.$route.query.username}}" label="Hot" />
              <q-route-tab :to="{path:'/page3',query:{username: this.$route.query.username}}" label="New" />
              <q-route-tab :to="{path:'/page4',query:{username: this.$route.query.username}}" label="Oscar" />
              <q-route-tab :to="{path:'/page5',query:{username: this.$route.query.username}}" label="All" />
              <q-route-tab :to="{path:'/page6',query:{username: this.$route.query.username}}" label="Myself"/>
              <q-route-tab :to="{path:'/search',query:{username: this.$route.query.username}}" label="Search"/>
            </q-tabs>
        </q-toolbar-title>
      </q-toolbar>
    </q-header>
    <q-page-container >
      <router-view />
    </q-page-container>

  </q-layout>
</template>

<script>

export default {
    mounted(){
        document.querySelector("body").style.backgroundColor =
      "background:rgb(238,241,246)";
      document.querySelector("body").style.backgroundAttachment= 'fixed';
      document.querySelector("body").style.backgroundSize= 'cover';
      document.querySelector("body").style.backgroundPosition= 'center';
    }
 
}
</script>

<style>
.element.style {
    min-height: 1366px;
    background: rgb(238,241,246) !important;
}
.head1{
  background:white;
  height: 61px;
}
.head_voc{
  color:black;
  margin-top:-95px;
}
.fit {
    width: 80% !important;
    height: 100% !important;
    border: none;
}
.omg {
    background: none !important;
    background: none !important;
}
#lead{
  position: absolute;
}
</style>