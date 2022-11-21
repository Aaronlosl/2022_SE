<!-- 说明：同学互助板块中的一条搜索结果的详情
内容：
全部信息的显示 -->

<template>
  <div class="PP1Result">
    <router-view></router-view>
    <abstract-dis-1></abstract-dis-1><br>
    <abstract-dis-1></abstract-dis-1><br>
    <abstract-dis-1></abstract-dis-1><br>
    <navi-box></navi-box>
  </div>
</template>
<script>
import NaviBox from '@/components/NaviBox.vue';
import AbstractDis1 from '@/components/AbstractDis1.vue';

export default {
  name: "PP1",
  components: { NaviBox, AbstractDis1, }
}
</script>

<style scoped>
h3 {
  margin: 450px 0px 60px;
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


