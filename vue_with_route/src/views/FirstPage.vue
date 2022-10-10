<template>
  <div class="PP_entry">
    <a href="https://" target="_blank" rel="noopener">
      <img src="@/assets/子页面1按钮.png">
    </a>
    <a href="https://" target="_blank" rel="noopener">
      <img src="@/assets/子页面2按钮.png">
    </a>
    <a href="https://" target="_blank" rel="noopener">
      <img src="@/assets/子页面3按钮.png">
    </a>
    <br>
    <img src="@/assets/分割线.png">
    <br>

    <AbstractDis></AbstractDis>

    <h3>
      <a href="https://" target="_blank" rel="noopener">
        <img src="@/assets/首页icon.png">
      </a>
      <a href="https://" target="_blank" rel="noopener">
        <img src="@/assets/发布icon.png">
      </a>
      <a href="https://" target="_blank" rel="noopener">
        <img src="@/assets/聊天icon.png">
      </a>
    </h3>
  </div>
</template>

<script>
import AbstractDis from '@/components/AbstractDis.vue';
export default {
    name: "FirstPage",
    components: { AbstractDis }
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