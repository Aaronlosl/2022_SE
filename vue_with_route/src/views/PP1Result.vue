<template>
  <div class="PP1Result">
      <transition
        enter-active-class="animate__animated animate__fadeIn"
        leave-active-class="animate__animated animate__fadeOut"
      >
        <div class="fixedSearch" v-show="showFixedSearch">
          <searchBtn class="searchBtn" href="https://" target="_blank" rel="noopener">
            <img src="@/assets/箭头二.svg">
          </searchBtn>
          <textarea 
            class="helping information input box" 
            maxlength="50" 
            placeholder="less than 50 chars" 
            cols="32" 
            style="resize:none;"
            v-model="searchBox">
          </textarea>
          <searchBtn href="https://" target="_blank" rel="noopener">
            <img src="@/assets/search.svg">
          </searchBtn>
        </div>
      </transition>
      <br>

      <searchBtn href="https://" target="_blank" rel="noopener">
        <img src="@/assets/箭头二.svg">
      </searchBtn>
      <textarea 
        class="helping information input box" 
        maxlength="50" 
        placeholder="less than 50 chars" 
        cols="32" 
        style="resize:none;"
        v-model="searchBox">
      </textarea>
      <searchBtn href="https://" target="_blank" rel="noopener">
        <img src="@/assets/search.svg">
      </searchBtn>
      <br>

        <a href="https://" target="_blank" rel="noopener">
          <img src="@/assets/多媒体卡片1-2.png">
        </a>
        <a href="https://" target="_blank" rel="noopener">
          <img src="@/assets/多媒体卡片1-2.png">
        </a>
      <br>
        <a href="https://" target="_blank" rel="noopener">
          <img src="@/assets/多媒体卡片1-2.png">
        </a>
        <a href="https://" target="_blank" rel="noopener">
          <img src="@/assets/多媒体卡片1-2.png">
        </a>
      <br>

    <h3>
      <b href="https://" target="_blank" rel="noopener">
        <img src="@/assets/首页icon.png">
      </b>
      <b href="https://" target="_blank" rel="noopener">
        <img src="@/assets/发布icon.png">
      </b>
      <b href="https://" target="_blank" rel="noopener">
        <img src="@/assets/聊天icon.png">
      </b>
    </h3>
  </div>
</template>

<script>
export default {
    name: "PP1Result",
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
    method: {
      showSearch() {
          // 获取当前滚动条向下滚动的距离
          let scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
          // 当页面滚动到高度160px处时，显示搜索框
          if (scrollTop > 160) {
              this.showFixedSearch = true;
          } else {
              this.showFixedSearch = false;
          }
      },
  }
}


</script>

<style scoped>
h3 {
  margin: 600px 0px 60px;
}
a {
  color: #000000;
  margin: -6px;
}
b {
  color: #000000;
  margin: 32px;
}
.fixedSearch {
  position: fixed;
  width: 100%;
  z-index: 999;
  background: #f6f6f6;
  height: 120px;
  overflow: hidden;
}
link1 {
    /* 多媒体卡片 1 */

  position: relative;
  width: 167px;
  height: 246px;
  display: flex;
  flex-direction: column;
  padding: 24px;
  gap: 16;
  border-radius: 16px;
  opacity: 1;

  /* 纯白 */
  background: #FFFFFF;

  /* 阴影/低阴影 */
  box-shadow: 0px 3px 8px 0px rgba(0, 0, 0, 0.16);
}
</style>