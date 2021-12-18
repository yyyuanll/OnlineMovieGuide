<template>
  <q-layout view="hHh lpR lFf">

    <q-header elevated class="head1" height-hint="98">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="left = !left" />

        <q-toolbar-title>
            <img
              src="https://i.loli.net/2021/12/01/DI1slReF5KzLm7p.png"
              style="width: 130px; height: 100px; margin-left:20px"
            >
            <q-tabs align="center" class="head_voc">
              <q-route-tab to="/page1" label="Command" />
              <q-route-tab to="/page2" label="Hot" />
              <q-route-tab to="/page3" label="New" />
              <q-route-tab to="/page4" label="Oscar" />
              <q-route-tab to="/page5" label="All" />
              <q-route-tab to="/page6" label="Myself"/>
            </q-tabs>
        </q-toolbar-title>
      </q-toolbar>
    </q-header>
    <q-page-container>
      <router-view />
    </q-page-container>

  </q-layout>
</template>

<script>

export default {
 
}
</script>

<style>
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