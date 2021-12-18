<template>
<div class="index">
  <q-layout view="hHh lpR fFf">

    <q-header reveal class="omg">
      <q-toolbar style="background=none">
        <q-btn dense flat round icon="menu" @click="left = !left" />

        <q-toolbar-title>
            <img
              src="https://i.loli.net/2021/12/01/DI1slReF5KzLm7p.png"
              style="width: 130px; height: 100px; margin-top:20px;margin-left:20px"
            >
        </q-toolbar-title>
        <router-link to="register" >
        <q-btn outline rounded color="black" label="Resign in/Register" />
        </router-link>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="left" side="left" overlay style="background=none" class="omg"> 
      <!-- drawer content -->
    
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

  </q-layout>
</div>
</template>

<script>
export default {
  data () {
    return {
      left: true
    }
  }
}
</script>
<style >
.omg {
    background: none !important;
    background: none !important;
}
.index .q-drawer {
    position: absolute;
    top: 0;
    bottom: 0;
    background: none !important;
    z-index: 1000;
}

</style>