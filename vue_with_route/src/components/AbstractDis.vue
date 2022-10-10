<template>
    <li>
        <a href="https://" target="_blank" rel="noopener">
            <img src="@/assets/多媒体卡片1.png">
        </a>
    </li>
</template>

<script>
export default {
    name: "AbstractDis",
}
</script>

<style scoped>
a {
/* 多媒体卡片 1 */

position: static;
left: 42px;
top: 161px;
width: 328px;
height: 396px;
display: flex;
flex-direction: column;
padding: 24px;
border-radius: 16px;

/* 纯白 */
background: #FFFFFF;

/* 阴影/低阴影 */
box-shadow: 0px 3px 8px 0px rgba(0, 0, 0, 0.16);
}
li {
  display: inline-block;
  margin: 100px 0px;
}
</style>