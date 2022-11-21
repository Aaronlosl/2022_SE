<!-- 说明：登录页（已完成） -->

<template>
  <div class="home">
    <img alt="XY logo" src="../assets/Vector.svg">
    <HelloWorld msg="Sign in | up to XY" />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'SignIn',
  components: {
    HelloWorld
  }
}
</script>
