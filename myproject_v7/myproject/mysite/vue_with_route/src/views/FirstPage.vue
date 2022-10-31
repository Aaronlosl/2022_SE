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

    <ol>
      <li v-for="blog in bloglist" :key="blog.title">
        {{ blog.title }}<br>
        {{ blog.summary }}<br>
      </li>
    </ol>

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

const baseURL = 'http://localhost:3000'
axios.defaults.baseURL = baseURL


import AbstractDis from '@/components/AbstractDis.vue';
export default {
    name: "FirstPage",
    components: { AbstractDis },
    data () {
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
        // 当页面滚动到高度160px处时，显示搜索框
        if (scrollTop > 160) {
            this.showFixedSearch = true;
        } else {
            this.showFixedSearch = false;
        }
    },
    methods: {
      showBlogs(){
        axios.post('http://127.0.0.1:8000/json/home/')
          .then((response) => {
            console.log(response.data)
            if(response.data['status'] != 1){
              alert('Sorry but you are not login')
              this.$router.push('/');
            } else {
              this.bloglist=response.data['content']
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
.fixedSearch {
  position: fixed;
  width: 100%;
  z-index: 999;
  background: #f6f6f6;
  height: 120px;
  overflow: hidden;
}
</style>