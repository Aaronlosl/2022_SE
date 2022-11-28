<template>
  <div className="nav">
    <router-link to='/FirstPage' className="nav-item">
      <img style="margin-left: 0px; margin-top: 200px;" src="@/assets/多选.svg">
    </router-link>
    <router-link to='/PostPage' className="nav-item">
      <img style="margin-left: 90px; margin-top: 200px;" src="@/assets/plus.svg">
    </router-link>
    <router-link to='/InfoList' className="nav-item">
      <img style="margin-left: 90px; margin-top: 200px;" src="@/assets/message-circle.svg">
    </router-link>
  </div>
</template>

<script>
export default {
  name: "NaviBox",
}
</script>
<style scoped>
.nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: space-between;
  width: 328px;
  height: 50px;
  overflow: hidden;
  margin: 0 auto;
  background: #FFFFFF;
}

.nav-item {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 50px;
  height: 50px;
  overflow: hidden;
  margin: 0 32px;
}

.nav-item img {
  width: 32px;
  height: 32px;
  margin: 0 !important;
  padding: 0 !important;
}

</style>
