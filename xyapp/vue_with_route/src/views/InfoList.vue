<!-- 说明：好友列表页
内容：
默认置顶自己，可以修改个人信息
添加的好友显示——至多100条 -->


<template>
  <div class="InfoList">
    <img src="@/assets/分割线-2.svg"><br>

    <contact v-for="friend in friends" :key="friend" :friend="friend"></contact><br>

    <el-form-item label="upload" prop="">
      <el-button size="small" type="primary" @click="select()">Upload Profile Photo<i class="el-icon-upload el-icon--right"></i></el-button><br>
      <input type="file" id="file" ref="upload" style="visibility:hidden" @change="update($event)" accept="image/*">
    </el-form-item>


    <navi-box></navi-box>
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

import NaviBox from '@/components/NaviBox.vue'
import Contact from '@/components/Contact.vue'
export default {
  name: 'InfoList',
  components: { NaviBox, Contact, },
  data() {
    return {
      friends: [],

    }
  },
  mounted() {
    this.showFriends()
  },
  methods: {
    showFriends() {
      axios.post('http://127.0.0.1:8000/json/showFriends/', { name: ' ' })
        .then((response) => {
          console.log(response.data)
          if (response.data['status'] != 1) {
            alert('Sorry but you are not login')
            this.$router.push('/');
          } else {
            this.friends = response.data['content']
          }
        })
    },
    select() {
      this.$refs.upload.click()
    },
    update(event) {
      console.log(arguments)
      const file = event.target.files[0]
      let param = new FormData()
      param.append('avatar', file)
      console.log(param.get('file'))
      axios.post('http://127.0.0.1:8000/json/changeAvatar/',  param, {name:this.friends[0] })
        .then((response) => {
          console.log(response.data)
          console.log(this.$refs.file)
          console.log(this.$refs.file.files[0])
          if (response.data['status'] == 0) {
            alert('change success!')
          } else {
            alert('invalid!')
          }
        })
    },
  },
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

backBtn {
  /* 箭头二 */
  position: absolute;
  left: 35px;
  top: 25px;
  width: 50px;
  height: 50px;
  transform: rotate(90);
}

moreInfoBtn {
  /* more-horizontal */
  position: absolute;
  left: 320px;
  top: 25px;
  width: 50px;
  height: 50px;
}

headPic {
  /* 头像 */
  position: absolute;
  left: 40px;
  top: 109px;
  width: 120px;
  height: 120px;
  border-radius: 100px;
}

addFriend {
  /* user-plus */
  position: absolute;
  left: 320px;
  top: 144px;
  width: 50px;
  height: 50px;
}

name {
  /* Name： */
  position: absolute;
  left: 49px;
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
  left: 49px;
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
  left: 49px;
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
  left: 49px;
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

