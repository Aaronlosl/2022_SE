<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h3>
      
      <p>
        Please enter your username below<br>
        <textarea 
          class="username" 
          maxlength="25" 
          placeholder="less than 25 chars" 
          cols="32" 
          style="resize:none;"
          v-model="username">
        </textarea><br>
        <el-input 
          v-model="input" 
          placeholder="less than 25 chars"
          clearable>
        </el-input>
      </p>
      <p>
        Please enter your password below. <br>
        <textarea 
          class="password" 
          maxlength="25" 
          placeholder="less than 25 chars" 
          cols="32" 
          style="resize:none;"
          v-model="password">
        </textarea><br>
        <el-input 
          v-model="input" 
          placeholder="less than 25 chars"
          clearable
          show-password>
        </el-input>
      </p>
    </h3>  
    <h2 href="http://localhost:8080/#/FirstPage" target="_blank" rel="noopener" @click="Login()">
      <img src="@/assets/箭头一.png">
    </h2>
    <button @click="Login()">
      <img src="@/assets/箭头一.png">
    </button>
  </div>
  <div class="link">
    <ul>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel" target="_blank" rel="noopener">
        <img src="@/assets/facebook.png">
      </a></li>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-router" target="_blank" rel="noopener">
        <img src="@/assets/twitter.png">
      </a></li>
      <li><a href="https://github.com/Aaronlosl/2022_SE" target="_blank" rel="noopener">
        <img src="@/assets/github.png">
      </a></li>
    </ul>
  </div>
</template>

<script>
import axios from "axios"
import { } from '@element-plus/icons-vue'

const baseURL = 'http://localhost:3000'
axios.defaults.baseURL = baseURL
const loginCheck = params => {
  return axios.post('/login', params).then(res => {
      return res.data
  })
}

export default {
  name: "HelloWorld",
  props: {
      msg: String
  },
  data() {
    return {
      username: '',
      password: '',
    }
  },
  methods:{
    async Login(){
      this.form = "&username:" + this.username + "&password:" + this.password
      // 调用登录请求接口
      loginCheck(this.form).then(res => {
        // 登录成功,提示成功信息，然后跳转到首页
        if(res.meta.status === 200){
          // 提示成功信息
          this.$message({
              message: res.meta.msg,
              type: 'success'
        });
          var that = this;
          // 跳转到首页
          setTimeout(function(){
              that.$router.push({name:'FirstPage'})
          },1000)
        } else {
          // 登录失败，提示错误信息
          this.$message({
              message: 'Login Failed,' + res.meta.msg,
              type: 'error'
          });
        }
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h2 {
  margin-right: -117px;
}
h3 {
  font: 1em sans-serif;
  margin: 80px 0px 60px;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 100px 0px;
}
a {
  color: #000000;
  margin: 30px;
}
</style>
