<!-- 说明：职业发展板块搜索页
内容：
搜索框——吸顶
显示热门内容——至多100条
底部功能栏——滑框 -->

<template>
  <div>
    <transition enter-active-class="animate__animated animate__fadeIn"
      leave-active-class="animate__animated animate__fadeOut">
      <div class="fixedSearch" v-show="showFixedSearch">
        <router-link to='/FirstPage'>
          <img src="@/assets/箭头二.svg">
        </router-link>
        <el-input v-model="searchBox" maxlength="50" placeholder="less than 50 chars" suffix-icon="el-icon-search"
          clearable>
        </el-input>
        <el-button @click="Search()" style="margin-top:-3%">
          <img src="@/assets/search.svg">
        </el-button>
      </div>
    </transition>
    <br>

    <router-link to='/FirstPage'>
      <img src="@/assets/箭头二.svg">
    </router-link>
    <el-input v-model="searchBox" maxlength="50" placeholder="less than 50 chars" suffix-icon="el-icon-search"
      clearable>
    </el-input>
    <el-button @click="Search()" style="margin-top:-3%">
      <img src="@/assets/search.svg">
    </el-button>
  </div>

    <RouterView></RouterView>
    <li>
      <AbstractDis v-for="blog in bloglist" :key="blog.title" :title="blog.title" :summary="blog.summary"
        :date_posted="blog.date_posted" :pk="blog.pk" :img_name="blog.img_name">
      </AbstractDis><br/>
    </li>

  <div>
    <navi-box></navi-box>
  </div>
</template>

<script>
import NaviBox from '@/components/NaviBox.vue';
import AbstractDis from '@/components/AbstractDis.vue';
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

export default {
  components: { NaviBox ,AbstractDis},
  name: 'PP1Search',
  data() {
    return {
      showFixedSearch: false,
      showFixedBottom: false,
      searchBox: '',
      bloglist: [],
    }
  },
  mounted() {
    this.showBlogs()
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

    Search() {
      if (this.searchBox == "") {
        alert("Please check your input")
      } else {
        this.$router.push({
            path: `/PP3Search/PP3Result/${this.searchBox}`
        })
      }
    },

    showBlogs() {
      axios.post('http://127.0.0.1:8000/json/home/', {post_type: "Personal Development" })
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

li {
  display: inline-block;
  margin: 100px 0px;
}

</style>

