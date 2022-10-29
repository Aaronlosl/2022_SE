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
    Post() {
      if(this.username == "" || this.password == "") {
        alert("Please check your input")
      } else {
        // post
        this.$axios({
          url: '',
          method:'post',
          //发送格式为json
          data:JSON.stringify({func:'query',
            param:['3aa3a1fe7fe987945c8a097fa5274d352609b65021de4f0f0f8a4027479e802d']}),
          headers: {'Content-Type': 'application/json'}
        }).then(function(return_data) {
          alert(return_data)
        },
        function(return_data)
        {
          // TODO: router
          alert(return_data)
        });
      }
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
