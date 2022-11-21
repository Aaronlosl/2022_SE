<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h4>
      <p><br><b>Username</b><br>
        <el-input v-model="username" maxlength="25" placeholder="less than 25 chars" clearable>
        </el-input><br>
      </p>
      <p><br><b>Password</b><br>
        <el-input v-model="password" maxlength="25" placeholder="less than 25 chars" clearable show-password>
        </el-input><br>
      </p>

    </h4>
    <el-button style="margin-left: 12%; margin-top: 3%; " @click="Login()" type="text">
      <img src="@/assets/箭头一.svg">
    </el-button>
    <RouterView></RouterView>

  </div>
  <div class="link">
    <ul>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel" target="_blank"
          rel="noopener">
          <img src="@/assets/facebook.svg">
        </a></li>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-router" target="_blank"
          rel="noopener">
          <img src="@/assets/twitter.svg">
        </a></li>
      <li><a href="https://github.com/Aaronlosl/2022_SE" target="_blank" rel="noopener">
          <img src="@/assets/github.svg">
        </a></li>
    </ul>
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
/*
const loginCheck = params => {
  return axios.post('/login', params).then(res => {
      return res.data
  })
}
*/
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
  methods: {
    Login() {
      if (this.username == "" || this.password == "") {
        alert("Please check your input")
      } else {
        axios.post('http://127.0.0.1:8000/json/auth/', { username: this.username, password: this.password })
          .then((response) => {
            console.log(response.data)
            if (response.data['status'] != 1) {
              alert(response.data['message'])
            } else {
              alert(response.data['message'])
              this.$router.push('/FirstPage');
            }
          })
      }
    },
  }
}
</script>

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

b {
  margin-right: 10%;
}

.el-input {
  width: 260px;
  height: 40px;
  top: 5px;
  left: 0px;
}
</style>
