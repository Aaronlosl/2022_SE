<!-- 说明：自己的个人信息更改界面
内容：
更改内容到后端——对接 -->

<template>
  <div class="home">
    <h1>
      <img src="@/assets/logo.svg">
    </h1>
    <h1>Update Infomation</h1>
    <h2>
      <p>
        <t style="margin-right: 200px">Name</t><br>
        <textarea maxlength="25" placeholder="less than 25 characters" cols="32" style="resize:none;"></textarea><br>
      </p>
      <p>
        <t style="margin-right: 190px">Identity</t><br>
        <textarea maxlength="25" placeholder="less than 25 characters" cols="32" style="resize:none;"></textarea><br>
      </p>
      <p>
        <t style="margin-right: 215px">Info</t><br>
        <textarea maxlength="50" placeholder="less than 50 characters" cols="32" rows="4"
          style="resize:none;"></textarea><br>
      </p>
      <p>
        <t style="margin-right: 125px">Optional Contact</t><br>
        <textarea maxlength="25" placeholder="less than 25 characters" cols="32" style="resize:none;"></textarea><br>
      </p>
    </h2>

    <router-link to='/PostPage'>
      <img src="@/assets/send.svg" style="margin-left:200px">
    </router-link>
    <router-view></router-view>

    <div class="scroll" :class="{ 'is-fixed': isFixed }">
      <navi-box></navi-box>
    </div>

  </div>
</template>

<script>
import NaviBox from '@/components/NaviBox.vue';
export default {
  components: { NaviBox },
  name: 'UpdateInfo',
  data() {
    return {
      isFixed: false,
    }
  },
}
</script>

<style scoped>
h2 {
  font: 1em sans-serif;
  margin: 0px 0px 60px;
}

a {
  color: #000000;
  margin: 32px;
}

h3 {
  margin: 0px 0px 60px;
}

.is-fixed {
  position: fixed;
  top: 2000;
  z-index: 999;
}
</style>
