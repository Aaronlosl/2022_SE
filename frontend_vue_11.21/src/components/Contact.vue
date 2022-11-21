<template>
    <button @click="clickHand(friend)">{{ friend}}</button><br>
    <a style="margin-right: 240px">
        <router-link to="/InfoList/InfoDetail/bob">
            <img src="@/assets/头像.svg">
        </router-link>
        <br>
    </a>
    <img src="@/assets/分割线-2.svg">
    <br>
</template>

<script>
export default {
    name: "AbstractDis",
    props: ['friend'],
    methods: {
        clickHand(id) {
            this.$router.push({
                path: `/InfoList/InfoDetail/${id}`
            })
        },
    }
}

const info_img = document.createElement("img");
let img_request = new XMLHttpRequest();
let img_url = "/image?skuid=" // +
img_request.open("GET", img_url);
img_request.send();
img_request.onload = function () {
    let image_r = img_request.response;
    let imageSRC = "data:image/jpeg:base64," + image_r;
    info_img.src = imageSRC;
}

</script>