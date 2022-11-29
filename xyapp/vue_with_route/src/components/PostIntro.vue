<!-- 说明：个人信息修改页
内容：
五块主要内容——未做对接 -->

<template>
    <router-link to='/PostDetail1'>
        <img src="@/assets/子页面1按钮.svg" style="
        position: absolute;
        left: -127px;
        top: 57px;
        width: 59px;
        height: 59px;
        opacity: 1;">
    </router-link>
    <img src="@/assets/描述1.svg" style="
        position: absolute;
        left: -12px;
        top: 26px;
        width: 153px;
        height: 120px;
        opacity: 1;
        font-family: SourceHanSansCN-Regular;
        font-size: 18px;
        font-weight: normal;
        letter-spacing: 0em;
        color: #3D3D3D;">
    <router-link to='/PostDetail2'>
        <img src="@/assets/子页面2按钮.svg" style="
        position: absolute;
        left: 82px;
        top: 297px;
        width: 59px;
        height: 59px;
        opacity: 1;">
        <img src="@/assets/描述2.svg" style="
        position: absolute;
        left: -127px;
        top: 260px;
        width: 153px;
        height: 127px;
        opacity: 1;
        font-family: SourceHanSansCN-Regular;
        font-size: 18px;
        font-weight: normal;
        letter-spacing: 0em;
        color: #3D3D3D;">
    </router-link>
    <router-link to='/PostDetail3'>
        <img src="@/assets/子页面3按钮.svg" style="
        position: absolute;
        left: -127px;
        top: 517px;
        width: 59px;
        height: 59px;
        opacity: 1;">
        <img src="@/assets/描述3.svg" style="
        position: absolute;
        left: -12px;
        top: 472px;
        width: 173px;
        height: 140px;
        opacity: 1;
        font-family: SourceHanSansCN-Regular;
        font-size: 18px;
        font-weight: normal;
        letter-spacing: 0em;
        color: #3D3D3D;">
    </router-link>
</template>

<script>
export default {
    name: "PostIntro",
}
</script>
