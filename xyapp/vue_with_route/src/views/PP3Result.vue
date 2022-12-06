<!-- 说明：个人发展板块搜索结果页
内容：
搜索框——吸顶
显示热门内容——至多100条
底部功能栏——滑框 -->

<template>
  <div class="PP3">
    <br>
    <AbstractDis v-for="blog in bloglist" :key="blog.title" :title="blog.title" :summary="blog.summary"
      :date_posted="blog.date_posted" :pk="blog.pk" :img_name="blog.img_name">
    </AbstractDis><br>
    
    <router-view></router-view>

    <navi-box></navi-box>
  </div>
</template>

<script>
import NaviBox from '@/components/NaviBox.vue'
// mport AbstractDis3 from '@/components/AbstractDis3.vue'
import AbstractDis from '@/components/AbstractDis.vue';
import axios from "axios"
// import { Search } from '@element-plus/icons-vue'

// ensure csrf-token append to post requests
// https://www.freesion.com/article/8944598323/
axios.interceptors.request.use((config) => {
  config.headers['X-Requested-With'] = 'XMLHttpRequest';
  let regex = /.*csrftoken=([^;.]*).*$/; // 用于从cookie中匹配 csrftoken值
  config.headers['X-CSRFToken'] = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1];
  return config
});

export default {
  components: { NaviBox, AbstractDis },
  name: 'PP3',
  data() {
    return {
      bloglist: [],
      // search_content:'',
    }
  },
  mounted() {
    // this.search_content = this.$route.params.search_content,
    this.Search()
  },
  methods:{
    Search() {
      axios.post('http://127.0.0.1:8000/json/home/', { search: this.$route.params.search_content, post_type: "Personal Development" })
        .then((response) => {
          console.log(response.data)
          if (response.data['status'] != 1) {
            alert('Sorry but you are not login')
            this.$router.push('/');
          } else {
            this.bloglist = response.data['content']
          }
        })
    },
  }
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
