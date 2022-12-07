<!-- 说明：好友信息详情页
内容：
显示后端信息TODO
显示自己信息的页有修改信息功能 -->

<template>
  <div class="InfoDetail">
    <mid>
      <div class="PP3 Detail Page">
        <backBtn href="https://" target="_blank" rel="noopener">
          <router-link to="/InfoList">
            <img src="@/assets/箭头二.svg">
          </router-link>
        </backBtn>

        <moreInfoBtn href="https://" target="_blank" rel="noopener">
          <router-link to="/UpdateInfo">
            <img src="@/assets/more-horizontal.svg">
          </router-link>
        </moreInfoBtn>

        <headPic href="https://" target="_blank" rel="noopener">
          <img :src="avatar">
          <!-- 头像 -->
        </headPic>

        <addFriend href="https://" target="_blank" rel="noopener">
          <img src="@/assets/user-plus.svg">
        </addFriend>

      </div>
    </mid>
  </div>
   <mydiv>
    <h2>Name: </h2>{{ name }}<br>
    <h2>Identity: </h2>{{ identity }}<br>
    <h2>Info: </h2>{{ info }}<br>
    <h2>Otherinfo: </h2>{{ optional }}<br>
   </mydiv>

  <div>
    <router-link to='/FirstPage'>
      <img style="margin-left: 0px; margin-top: 720px;" src="@/assets/多选.svg">
    </router-link>
    <router-link to='/PostPage'>
      <img style="margin-left: 30px; margin-top: 720px;" src="@/assets/plus.svg">
    </router-link>
    <router-link to='/InfoList'>
      <img style="margin-left: 30px; margin-top: 720px;" src="@/assets/message-circle.svg">
    </router-link>
  </div>
</template>

<script>
import axios from "axios"
export default {
  name: "InfoDetail",
  components: {
  },
  data() {
    return {
      username: '',
      bloglist: [],
      name: '',
      identity: '',
      info: '',
      optional: '',
      avatar:'',
      publicPath: process.env.BASE_URL,
    }
  },
  mounted() {
    this.username = this.$route.params.username
    this.showUserInfo()
  },
  methods: {
    showUserInfo() {
      axios.post('http://127.0.0.1:8000/json/showUserInfo/', { name: this.$route.params.username })
        .then((response) => {
          console.log(response.data)
          if (response.data['status'] != 1) {
            alert('Sorry but you are not login')
            this.$router.push('/');
          } else {
            this.bloglist = response.data['content']
            this.name = this.bloglist[0].name
            this.identity = this.bloglist[0].identity
            this.info = this.bloglist[0].info
            this.optional = this.bloglist[0].optional
            this.avatar = this.publicPath + "static/avatars/" + this.name + '/square_' + this.bloglist[0].avatar
          }
        })
    }
  },
}
</script>


<style scoped>
h2 {
  position: absolute;
  margin-left: -60px;
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
  position: static;
}

backBtn {
  /* 箭头二 */
  position: absolute;
  left: -160px;
  top: 25px;
  width: 40px;
  height: 40px;
  transform: rotate(90);
}

moreInfoBtn {
  /* more-horizontal */
  position: absolute;
  left: 70px;
  top: 25px;
  width: 40px;
  height: 40px;
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
  top: 104px;
  width: 20px;
  height: 20px;
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

mydiv{
  width: 100px;
  height: 100px;
  position: absolute;
  left: 50%;top: 50%;
  margin-left: -50px;
  margin-top: -50px;
}

mid {
  position: absolute;
}
</style>
