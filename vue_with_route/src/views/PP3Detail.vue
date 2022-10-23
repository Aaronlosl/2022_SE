<template>
  <div class="PP3 Detail Page">
    <backBtn href="https://" target="_blank" rel="noopener">
      <img src="@/assets/箭头二.png">
    </backBtn> 

    <moreInfoBtn href="https://" target="_blank" rel="noopener">
      <img src="@/assets/more-horizontal.png">
    </moreInfoBtn>

    <headPic href="https://" target="_blank" rel="noopener">
      <img src="@/assets/头像.png">
    </headPic>

    <addFriend href="https://" target="_blank" rel="noopener">
      <img src="@/assets/user-plus.png">
    </addFriend>

    <name>
      <img src="@/assets/Name.png">
    </name>

    <identity>
      <img src="@/assets/Identity.png">
    </identity>

    <info>
      <img src="@/assets/Info.png">
    </info>

    <otherInfo>
      <img src="@/assets/OptionalContactInfo.png">
    </otherInfo>
  </div>
</template>

<script>
export default {
  name: 'PP3Detail',
  
}
</script>

<style scoped>
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
    -webkit-text-stroke: #000000 1px; /* 浏览器可能不支持 */
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
    -webkit-text-stroke: #000000 1px; /* 浏览器可能不支持 */
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
    -webkit-text-stroke: #000000 1px; /* 浏览器可能不支持 */
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
    -webkit-text-stroke: #000000 1px; /* 浏览器可能不支持 */
  }
</style>
