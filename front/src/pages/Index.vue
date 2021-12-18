<template>
  <q-page class="flex flex-center"> 
    <div class="cs">
      <div style="font-size:30px;color:black;font-weight:bolder"> Your Online Movie Guide</div>
      <div class="cs1" style="color:black;font-size:20px;font-weight:bolder">Start your movie journal with us</div>
      <div class="q-pa-md q-gutter-sm">
          <router-link to="page1" >
            <q-btn  rounded color="white" text-color="black" style="font-size:15px">
              <div>
                Start
              </div>
            </q-btn>
          </router-link>
      </div>
    </div>
  </q-page>
</template>

<script>

export default {
  name: 'Index',
   mounted () {
    document.querySelector("body").style.backgroundImage =
      "url('https://s2.loli.net/2021/12/06/7mWKoz54HunOMJY.gif') ";
      document.querySelector("body").style.backgroundAttachment= 'fixed';
      document.querySelector("body").style.backgroundSize= 'cover';
      document.querySelector("body").style.backgroundPosition= 'center';
  },
}
</script>

<style>
a {
  text-decoration: none;
}
 
.router-link-active {
  text-decoration: none;
}
.cs {
  margin:0 auto;
  margin-top:-100px;
}
.cs1{
  margin:0 auto;
  text-align: center;
}
.q-pa-md {
    padding: 16px 116px;
}
</style>

