<!-- 说明：个人信息页（自己的或好友的）
内容：
固定从后端返回的各项信息
自己的内容页——修改信息
他人的内容页——添加好友 -->

<template>
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
      <img src="@/assets/头像-2.svg">
      <!-- 头像 -->
    </headPic>

    <addFriend href="https://" target="_blank" rel="noopener">
      <img src="@/assets/user-plus.svg">
    </addFriend>

    <name>
      <img src="@/assets/Name.svg">
    </name>
<!-- 名字 -->
    <identity>
      <img src="@/assets/Id.svg">
    </identity>
<!-- ID -->
    <info>
      <img src="@/assets/Info.svg">
    </info>
<!-- Info -->
    <otherInfo>
      <img src="@/assets/O.svg">
    </otherInfo>
<!-- email -->
  </div>
</template>

<script>
export default {
  name: "InfoCard",
}
</script>


<style scoped>
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