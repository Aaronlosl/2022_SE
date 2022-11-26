<template>
    <router-link to='/PP2Search/PP2Result/PP2Detail'>
        <img src="@/assets/多媒体卡片2.png">
        <img src="@/assets/多媒体卡片2.png">
    </router-link>
</template>

<script>
export default {
    name: "AbstractDis2",
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