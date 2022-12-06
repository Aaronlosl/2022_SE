<!-- 说明：自己的个人信息更改界面
内容：
更改内容到后端——对接 -->

<template>
  <div class="home">
    <h1>
      <img src="@/assets/logo.svg">
    </h1>
    <h1>Update Infomation</h1>
    <h2>
      <p>
        <t style="margin-right: 200px">Name</t><br>
        <textarea maxlength="25" placeholder="less than 25 characters" cols="32" style="resize:none;" v-model="name"></textarea><br>
      </p>
      <p>
        <t style="margin-right: 190px">Identity</t><br>
        <textarea maxlength="25" placeholder="less than 25 characters" cols="32" style="resize:none;" v-model="identity"></textarea><br>
      </p>
      <p>
        <t style="margin-right: 215px">Info</t><br>
        <textarea maxlength="50" placeholder="less than 50 characters" cols="32" rows="4"
          style="resize:none;" v-model="info"></textarea><br>
      </p>
      <p>
        <t style="margin-right: 125px">Optional Contact</t><br>
        <textarea maxlength="25" placeholder="less than 25 characters" cols="32" style="resize:none;" v-model="optical_contact_info"></textarea><br>
      </p>
    </h2>

      <el-button style="margin-left: 14%; " @click="Post()" type="text">
        <img src="@/assets/send.svg">
      </el-button>
    <router-view></router-view>

    <div class="scroll" :class="{ 'is-fixed': isFixed }">
      <navi-box></navi-box>
    </div>

  </div>
</template>

<script>
import axios from "axios"

// ensure csrf-token append to post requests
// https://www.freesion.com/article/8944598323/
axios.interceptors.request.use((config) => {
  config.headers['X-Requested-With'] = 'XMLHttpRequest';
  let regex = /.*csrftoken=([^;.]*).*$/; // 用于从cookie中匹配 csrftoken值
  config.headers['X-CSRFToken'] = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1];
  return config
});

import NaviBox from '@/components/NaviBox.vue';
export default {
  components: { NaviBox },
  name: 'UpdateInfo',
  data() {
    return {
      isFixed: false,
    }
  },
  methods: {
    Post() {
      if (this.name == "" || this.identity == "" || this.info == "" || this.optical_contact_info == "") {
        alert("Please check your input")
      } else {
        axios.post('http://127.0.0.1:8000/json/update_userinfo/', { name: this.name, identity: this.identity, info: this.info, optical_contact_info:this.optical_contact_info })
          .then((response) => {
            console.log(response.data)
            if (response.data['status'] != 1) {
              alert(response.data['message'])
              this.$router.push('/');
            } else {
              alert(response.data['message'])
              this.$router.push('/InfoList');
            }
          })
      }
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

.is-fixed {
  position: fixed;
  top: 2000;
  z-index: 999;
}

b {
  position: static;
}

backBtn {
  /* 箭头二 */
  position: absolute;
  left: -180px;
  top: 25px;
  width: 50px;
  height: 50px;
  transform: rotate(90);
}

moreInfoBtn {
  /* more-horizontal */
  position: absolute;
  left: 105px;
  top: 25px;
  width: 50px;
  height: 50px;
}

headPic {
  /* 头像 */
  position: absolute;
  left: -175px;
  top: 109px;
  width: 120px;
  height: 120px;
  border-radius: 100px;
}

addFriend {
  /* user-plus */
  position: absolute;
  left: 105px;
  top: 144px;
  width: 50px;
  height: 50px;
}

name {
  /* Name： */
  position: absolute;
  left: -166px;
  top: 307px;
  width: 78px;
  height: 22px;
  font-family: SourceHanSansCN-Regular;
  font-size: 18px;
  font-weight: normal;
  letter-spacing: 0em;
  color: #000000;
  -webkit-text-stroke: #000000 1px;
  /* 浏览器可能不支持 */
}

identity {
  /* Identity： */
  position: absolute;
  left: -166px;
  top: 412px;
  width: 78px;
  height: 22px;
  font-family: SourceHanSansCN-Regular;
  font-size: 18px;
  font-weight: normal;
  letter-spacing: 0em;
  color: #000000;
  -webkit-text-stroke: #000000 1px;
  /* 浏览器可能不支持 */
}

info {
  /* Info： */
  position: absolute;
  left: -166px;
  top: 513px;
  width: 51px;
  height: 22px;
  font-family: SourceHanSansCN-Regular;
  font-size: 18px;
  font-weight: normal;
  letter-spacing: 0em;
  color: #000000;
  -webkit-text-stroke: #000000 1px;
  /* 浏览器可能不支持 */
}

otherInfo {
  /* Optional contact info： */
  position: absolute;
  left: -166px;
  top: 618px;
  width: 199px;
  height: 22px;
  font-family: SourceHanSansCN-Regular;
  font-size: 18px;
  font-weight: normal;
  letter-spacing: 0em;
  color: #000000;
  -webkit-text-stroke: #000000 1px;
  /* 浏览器可能不支持 */
}
</style>
