<!-- 说明：个人发展信息 发布页
内容：
根据板块不同有三个入口——每个入口一个vue UI，这里只实现了一种
个人信息，内容简介，PS须知或其他事项，图片描述——图片描述 -->

<template>
  <div class="home">
    <h1>
      <img src="@/assets/logo.svg">
    </h1>
    <h1>Personal Development Post</h1>
    <h2>
      <p>
        <t style="margin-right: 200px">Name</t><br>
        <textarea maxlength="25" placeholder="less than 25 characters" cols="32" style="resize:none;"
          v-model="title"></textarea><br>
      </p>
      <p>
        <t style="margin-right: 210px">Field</t><br>
        <textarea maxlength="25" placeholder="less than 25 characters" cols="32" style="resize:none;"></textarea><br>
      </p>
      <p>
        <t style="margin-right: 155px">Requirement</t><br>
        <textarea maxlength="25" placeholder="less than 25 characters" cols="32" style="resize:none;"></textarea><br>
      </p>
      <p>
        <t style="margin-right: 205px">Detail</t><br>
        <textarea maxlength="500" placeholder="less than 500 characters" cols="32" rows="10" style="resize:none;"
          v-model="content"></textarea><br>
      </p>
      <!-- TODO：增加图片上传按钮和功能 -->
      <t style="margin-right: 205px">Photo</t><br>
        <el-upload action="" :on-change="handleelchange"  :auto-upload="false" list-type="picture-card" accept="image/png,image/gif,image/jpg,image/jpeg" :limit="1">
          <i class="el-icon-plus">Upload</i>
        </el-upload>


      <el-button style="margin-left: 14%; " @click="Post()" type="text">
        <img src="@/assets/send.svg">
      </el-button>
    </h2>



    <navi-box></navi-box>

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


import NaviBox from '@/components/NaviBox.vue'
export default {
  components: { NaviBox },
  name: 'PP1Search',
  data() {
    return {
      title: '',
      content: '',
      formdata: new FormData(),
    }
  },
  methods: {
    Post() {
      if (this.title == "" || this.content == "") {
        alert("Please check your input")
      } else {
        console.log(this.formdata)
        this.formdata.append("title", this.title)
        this.formdata.append("content", this.content)
        this.formdata.append("post_type", "Personal Development")
        axios.post('http://127.0.0.1:8000/json/post/',this.formdata, { pic:this.formdata, title: this.title, content: this.content, post_type: "Personal Development" })
          .then((response) => {
            console.log(response.data)
            if (response.data['status'] != 1) {
              alert(response.data['message'])
              this.$router.push('/');
            } else {
              alert(response.data['message'])
              this.$router.push('/FirstPage');
            }
          })
      }
    },
    handleelchange(file, fileList) {
      console.log("123")
      console.log(file, fileList)
      //this.formdata = file.raw
      //console.log(this.formdata)
      
      this.formdata = new FormData()
      fileList.map(item => { //fileList本来就是数组，就不用转为真数组了
        this.formdata.append("pic", item.raw)  //将每一个文件图片都加进formdata
      })
      console.log(this.formdata)
      // axios.post("接口地址", formdata).then(res => { console.log(res) })
    },
  }
}
</script>
  
<style scoped>
h2 {
  font: 1em sans-serif;
  margin: 0px 0px 60px;
}

a {
  color: #000000;
  margin: 32px;
}

h3 {
  margin: 0px 0px 60px;
}
</style>