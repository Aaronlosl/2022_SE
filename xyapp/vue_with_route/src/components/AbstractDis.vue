<template>
    <li>
        <a>
            <img :src="imgaddr">
            
            
        </a>

    </li>
    <p>{{ title }}</p>
    <p>{{ date_posted }}</p>
    <p>{{ summary}}</p>
</template>

<script>
export default {
    name: "AbstractDis",
    props: ['title', 'summary', 'date_posted','pk'],
    data() {
        return {
        imgaddr:"",
        a1:"123",
        publicPath:process.env.BASE_URL
        }
    },
    
    mounted() {
        console.log(this.pk)
        // this.imgaddr = require("@/assets/" + this.title + ".svg")
        // this.imgaddr = require("../../static/blogs/" + this.pk +"/" + this.pk+".jpg")
        this.imgaddr = this.publicPath + "static/blogs/" + this.pk +"/" + this.pk+".jpg"
        //this.imgaddr = "/static/blogs/" + this.pk +"/" + this.pk+".jpg"
        
        console.log(this.imgaddr)
        // root/blogs/title/img.jpg
        // 
        
    },
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