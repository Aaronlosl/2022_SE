<!-- 说明：个人发展板块搜索结果页
内容：
搜索框——吸顶
显示热门内容——至多100条
底部功能栏——滑框 -->

<template>
  <div class="PP3">
    <br>
    <abstract-dis-3></abstract-dis-3><br>
    <abstract-dis-3></abstract-dis-3><br>
    <abstract-dis-3></abstract-dis-3><br>
    <router-view></router-view>

    <navi-box></navi-box>
  </div>
</template>

<script>
import NaviBox from '@/components/NaviBox.vue'
import AbstractDis3 from '@/components/AbstractDis3.vue'
export default {
  components: { NaviBox, AbstractDis3 },
  name: 'PP3',
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
