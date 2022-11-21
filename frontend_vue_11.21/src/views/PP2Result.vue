<!-- 说明：科研板块结果页
内容：
注意！！没有搜索框
显示热门内容——至多100条
底部功能栏——滑框 -->

<template>
  <div class="PP2">
    <abstract-dis-2></abstract-dis-2><br>
    <abstract-dis-2></abstract-dis-2><br>
    <abstract-dis-2></abstract-dis-2><br>
    <router-view></router-view>
    <navi-box></navi-box>
  </div>
</template>
<script>
import NaviBox from '@/components/NaviBox.vue'
import AbstractDis2 from '@/components/AbstractDis2.vue'
export default {
  components: { NaviBox, AbstractDis2 },
  name: 'PP2',
}
</script>

<style scoped>
h3 {
  margin: 600px 0px 60px;
}

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