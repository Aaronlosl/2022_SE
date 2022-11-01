<template>
  <div class="home">
    <img alt="XY logo" src="../assets/logo.png">
    <HelloWorld msg="Sign in | up to XY"/>
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
