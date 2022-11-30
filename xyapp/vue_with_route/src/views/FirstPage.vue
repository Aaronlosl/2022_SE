<!-- 说明：登陆后显示的第一页
内容：
抬头（三个PP的搜索入口）——吸顶
热门内容——内容绑定，每页显示100条，可翻页
底部功能滑框 -->

<template>
  <div class="PP_entry">
  <div class="head">
    <router-link to='/PP1Search'>
      <img src="@/assets/子页面1按钮.svg">
    </router-link>
    <router-link to='/PP2Search'>
      <img src="@/assets/子页面2按钮.svg">
    </router-link>
    <router-link to='/PP3Search'>
      <img src="@/assets/子页面3按钮.svg">
    </router-link>
    <br>
    <img src="@/assets/分割线.svg">
    </div>
    <br/>

    <AbstractDis v-for="blog in bloglist" :key="blog.title" :title="blog.title" :summary="blog.summary"
      :date_posted="blog.date_posted" :pk="blog.pk">
    </AbstractDis><br/>
    <div class="fixed">
      <navi-box></navi-box>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import { } from '@element-plus/icons-vue'

// ensure csrf-token append to post requests
// https://www.freesion.com/article/8944598323/
axios.interceptors.request.use((config) => {
  config.headers['X-Requested-With'] = 'XMLHttpRequest';
  let regex = /.*csrftoken=([^;.]*).*$/; // 用于从cookie中匹配 csrftoken值
  config.headers['X-CSRFToken'] = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1];
  return config
});

import AbstractDis from '@/components/AbstractDis.vue';
import NaviBox from '@/components/NaviBox.vue'
export default {
  name: "FirstPage",
  components: { AbstractDis, NaviBox, },
  data() {
    return {
      bloglist: [],
    }
  },
  mounted() {
    this.showBlogs()
    // 监听页面滚动事件
    window.addEventListener("scroll", this.showSearch)
  },
  showSearch() {
    // 获取当前滚动条向下滚动的距离
    let scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
    // 当页面滚动到高度300px处时，显示搜索框
    if (scrollTop > 300) {
      this.showFixedSearch = true;
    } else {
      this.showFixedSearch = false;
    }
  },
  methods: {
    showBlogs() {
      axios.post('http://127.0.0.1:8000/json/home/')
        .then((response) => {
          console.log(response.data)
          if (response.data['status'] != 1) {
            alert('Sorry but you are not login')
            this.$router.push('/');
          } else {
            this.bloglist = response.data['content']
          }
        })
    }
  },
}


</script>

<style scoped>
.fixed {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  height: 50px;
  background: #fff;
  /*height: calc(96rpx + env(safe-area-inset-bottom));*/
  /*padding-bottom: env(safe-area-inset-bottom);*/
}
.head {
  position: -webkit-sticky;
  position: sticky;
  top:0px;
  background: #fff;
}
h3 {
  margin: 0px 0px 60px;
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

.fixedSearch {
  position: fixed;
  width: 100%;
  z-index: 999;
  background: #f6f6f6;
  height: 120px;
  overflow: hidden;
}
</style>