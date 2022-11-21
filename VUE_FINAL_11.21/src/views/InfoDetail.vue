<!-- 说明：好友信息详情页
内容：
显示后端信息TODO
显示自己信息的页有修改信息功能 -->

<template>
  <div class="InfoDetail">
    <mid>
      <p>{{ username}}</p>
      <InfoCard></InfoCard>
    </mid>
  </div>
  <div>
    <router-link to='/FirstPage'>
      <img style="margin-left: 0px; margin-top: 720px;" src="@/assets/多选.svg">
    </router-link>
    <router-link to='/PostPage'>
      <img style="margin-left: 30px; margin-top: 720px;" src="@/assets/plus.svg">
    </router-link>
    <router-link to='/InfoList'>
      <img style="margin-left: 30px; margin-top: 720px;" src="@/assets/message-circle.svg">
    </router-link>
  </div>
</template>

<script>
import InfoCard from '@/components/InfoCard.vue'
export default {
  name: "InfoDetail",
  components: {
    InfoCard,
  },
  data() {
    return {
      username: '',
    }
  },
  mounted() {
    this.username = this.$route.params.username
  },
}
</script>


<style scoped>
a {
  color: #000000;
  margin: 32px;
}

mid {
  position: absolute;
}
</style>