<template>
  <div>
      <transition
        enter-active-class="animate__animated animate__fadeIn"
        leave-active-class="animate__animated animate__fadeOut"
      >
        <div class="fixedSearch" v-show="showFixedSearch">
          <a class="searchBtn" href="https://" target="_blank" rel="noopener">
            <img src="@/assets/箭头二.svg">
          </a>
          <textarea 
            class="helping information input box" 
            maxlength="50" 
            placeholder="less than 50 chars" 
            cols="32" 
            style="resize:none;"
            v-model="searchBox">
          </textarea>
          <a href="https://" target="_blank" rel="noopener">
            <img src="@/assets/search.svg">
          </a>
        </div>
      </transition>
      <br>

      <a href="https://" target="_blank" rel="noopener">
        <img src="@/assets/箭头二.svg">
      </a>
      <textarea 
        class="helping information input box" 
        maxlength="50" 
        placeholder="less than 50 chars" 
        cols="32" 
        style="resize:none;"
        v-model="searchBox">
      </textarea>
      <a href="https://" target="_blank" rel="noopener">
        <img src="@/assets/search.svg">
      </a>
      <div class="box100">100</div>
      <div class="box100">200</div>
      <div class="box100">300</div>
      <div class="box100">400</div>
      <div class="box100">500</div>
      <div class="box100">600</div>
      <div class="box100">700</div>
      <div class="box100">800</div>
      <div class="box100">900</div>
      <div class="box100">1000</div>
  </div>
</template>

<script>
  export default {
      name: 'PP1Search',
      data() {
          return {
              showFixedSearch: false,
              showFixedBottom: false
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
</style>

