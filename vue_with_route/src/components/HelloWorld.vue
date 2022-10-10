<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h3>
      <p>
        Please enter your username below<br>
        <textarea maxlength="25" placeholder="less than 25 chars" cols="32"></textarea><br>
        <el-input 
          v-model="input" 
          placeholder="less than 25 chars"
          clearable>
        </el-input>
      </p>
      <p>
        Please enter your password below. <br>
        <textarea maxlength="25" placeholder="less than 25 chars" cols="32"></textarea><br>
        <el-input 
          v-model="input" 
          placeholder="less than 25 chars"
          clearable
          show-password>
        </el-input>
      </p>
    </h3>
    <h2 href="http://localhost:8080/#/FirstPage" target="_blank" rel="noopener">
      <img src="@/assets/箭头一.png">
    </h2>
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
import { } from '@element-plus/icons-vue'
export default {
    name: "HelloWorld",
    props: {
        msg: String
    },
    data() {
      return {
        input: ''
      }
    },
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
