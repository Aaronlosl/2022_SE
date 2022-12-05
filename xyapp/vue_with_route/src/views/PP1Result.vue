<!-- 说明：同学互助板块中的一条搜索结果的详情
内容：
全部信息的显示 -->

<template>
  <div class="PP1Result">
    <router-view></router-view>
    <!--
      <abstract-dis-1 v-for="blog in bloglist" :key="blog.title" :title="blog.title" :summary="blog.summary"
      :date_posted="blog.date_posted">
      </abstract-dis-1><br>
      <abstract-dis-1></abstract-dis-1><br>
      <abstract-dis-1></abstract-dis-1><br>
    -->
    
    <AbstractDis v-for="blog in bloglist" :key="blog.title" :title="blog.title" :summary="blog.summary"
      :date_posted="blog.date_posted" :pk="blog.pk" :img_name="blog.img_name">
    </AbstractDis><br/>
    <div class="fixed">
      <navi-box></navi-box>
    </div>
  </div>
</template>
<script>
import NaviBox from '@/components/NaviBox.vue';
// import AbstractDis1 from '@/components/AbstractDis1.vue';
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
  name: "PP1",
  components: { NaviBox, AbstractDis, },
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
      axios.post('http://127.0.0.1:8000/json/home/', { search: this.$route.params.search_content, post_type: "Student Request" })
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


