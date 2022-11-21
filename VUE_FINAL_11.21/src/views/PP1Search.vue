<!-- 说明：同学互助板块搜索页
内容：
搜索框——吸顶
显示热门内容——至多100条
底部功能栏——滑框 -->

<template>
  <div>
    <transition enter-active-class="animate__animated animate__fadeIn"
      leave-active-class="animate__animated animate__fadeOut">
      <div class="fixedSearch" v-show="showFixedSearch">
        <searchBtn class="searchBtn" href="https://" target="_blank" rel="noopener">
          <img src="@/assets/箭头二.svg">
        </searchBtn>
        <textarea class="helping information input box" maxlength="50" placeholder="less than 50 chars" cols="32"
          style="resize:none; margin-bottom: 10px;" v-model="searchBox">
          </textarea>
        <el-input v-model="searchBox" maxlength="25" placeholder="less than 25 chars" clearable>
        </el-input>
        <searchBtn href="https://" target="_blank" rel="noopener">
          <img src="@/assets/search.svg" style="margin-bottom: 15px;">
        </searchBtn>
      </div>
    </transition>
    <br>

    <router-link to='/FirstPage'>
      <img src="@/assets/箭头二.svg">
    </router-link>
    <!--
      <textarea 
        class="helping information input box" 
        maxlength="50" 
        placeholder="less than 50 chars" 
        cols="32" 
        style="resize:none; margin-bottom: 10px;"
        v-model="searchBox">
      </textarea>
      -->
    <el-input v-model="searchBox" maxlength="50" placeholder="less than 50 chars" suffix-icon="el-icon-search"
      clearable>
    </el-input>
    <router-link to='/PP1Search/PP1Result'>
      <img src="@/assets/search.svg" style="margin-bottom: 15px;">
    </router-link>
    <RouterView></RouterView>

    <navi-box></navi-box>
  </div>
</template>

<script>
import NaviBox from '@/components/NaviBox.vue';
export default {
  components: { NaviBox },
  name: 'PP1Search',
  data() {
    return {
      showFixedSearch: false,
      showFixedBottom: false,
      searchBox: ''
    }
  },
  mounted() {
    // 监听页面滚动事件
    window.addEventListener("scroll", this.showSearch)
  },
  methods: {
    showSearch() {
      // 获取当前滚动条向下滚动的距离
      let scrollTop1 = document.documentElement.scrollTop || document.body.scrollTop;
      // 当页面滚动到高度160px处时，显示搜索框
      if (scrollTop1 > 160) {
        this.showFixedSearch = true;
      } else {
        this.showFixedSearch = false;
      }
    },
  }
}
</script>

<style scoped>
.fixedSearch {
  position: fixed;
  width: 100%;
  z-index: 999;
  background: #f6f6f6;
  height: 60px;
  overflow: hidden;
}

.searchBox {
  /* 输入框 */
  position: absolute;
  left: 104px;
  top: 8px;
  width: 260px;
  height: 61px;
  display: flex;
  flex-direction: column;
  padding: 0px;
}

.box100 {
  height: 100px;
  background: #ffffff;
  border: 0.1px solid black;
}

searchBtn {
  /* search */
  position: static;
  left: 328px;
  top: 40px;
  width: 24px;
  height: 24px;
}

.el-input {
  width: 240px;
  height: 40px;
  top: -22px;
  left: -5px;
}
</style>

