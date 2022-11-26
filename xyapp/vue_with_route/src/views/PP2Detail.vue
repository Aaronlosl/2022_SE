<!-- 说明：科研板块中的一条搜索结果的详情
内容：
全部信息的显示 -->

<template>
  <div class="PP2">
    <h3>This is PP2 Detail Page</h3>
    information, information...
    <navi-box></navi-box>
  </div>
</template>
<script>
import NaviBox from '@/components/NaviBox.vue'
export default {
  components: { NaviBox },
  name: 'PP2',
}
</script>

<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}

a {
  color: #000000;
  margin: 32px;
}

b {
  color: #000000;
  margin: 8px;
}
</style>

