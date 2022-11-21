<!-- 说明：底端发布功能点开显示的介绍页
内容：
点击每个功能进入对应的post页——目前只实现了一个post页 -->

<template>
  <div class="PostPage">

    <mid>
      <post-intro></post-intro>
    </mid>
    <div>
      <router-link to='/FirstPage'>
        <img style="margin-left: 0px; margin-top: 720px;" src="@/assets/多选.svg">
      </router-link>
      <router-link to='/PostPage'>
        <img style="margin-left: 90px; margin-top: 720px;" src="@/assets/plus.svg">
      </router-link>
      <router-link to='/InfoList'>
        <img style="margin-left: 90px; margin-top: 720px;" src="@/assets/message-circle.svg">
      </router-link>
    </div>
  </div>

</template>
<script>
import PostIntro from '@/components/PostIntro.vue'
export default {
  name: 'PostPage',
  components: { PostIntro, },
  data() {
    return {
      type: ""
    }
  }
}
</script>
  
<style scoped>
mid {
  position: absolute;
}
</style>