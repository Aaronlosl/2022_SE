<template>
  <div>
    <router-link to='/FirstPage'>
      <img style="margin-left: 0px; margin-top: 200px;" src="@/assets/多选.svg">
    </router-link>
    <router-link to='/PostPage'>
      <img style="margin-left: 90px; margin-top: 200px;" src="@/assets/plus.svg">
    </router-link>
    <router-link to='/InfoList'>
      <img style="margin-left: 90px; margin-top: 200px;" src="@/assets/message-circle.svg">
    </router-link>
  </div>
</template>

<script>
export default {
  name: "NaviBox",
}
</script>
