<!-- 说明：科研板块结果页
内容：
注意！！没有搜索框
显示热门内容——至多100条
底部功能栏——滑框 -->

<template>
  <div class="PP2">

    <AbstractDis2 v-for="blog in bloglist" :key="blog.title" :title="blog.title" :summary="blog.summary"
      :date_posted="blog.date_posted">
    </AbstractDis2><br>


    <router-view></router-view>
    <navi-box></navi-box>
  </div>
</template>


<script>
import NaviBox from '@/components/NaviBox.vue'
import axios from "axios"
import AbstractDis2 from '@/components/AbstractDis2.vue'

// ensure csrf-token append to post requests
// https://www.freesion.com/article/8944598323/
axios.interceptors.request.use((config) => {
  config.headers['X-Requested-With'] = 'XMLHttpRequest';
  let regex = /.*csrftoken=([^;.]*).*$/; // 用于从cookie中匹配 csrftoken值
  config.headers['X-CSRFToken'] = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1];
  return config
});

export default {
  components: { NaviBox, AbstractDis2 },
  name: 'PP2',
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
  methods: {
    showBlogs() {
      axios.post('http://127.0.0.1:8000/json/showpost/')
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