<template>
    <button @click="clickHand(friend)">{{ friend}}</button><br>
    <!-- <button @click="judge(friend)">{{ friend}}</button><br> -->
    <a style="margin-right: 240px">
        <router-link :to="url">
            <img v-show="isShow" :src="paths">
            <img v-show="!isShow" src="@/assets/头像.svg">
        </router-link>
        <br>
    </a>
    <img src="@/assets/分割线-2.svg">
    <br>
</template>

<script>
import axios from "axios"
export default {
    name: "AbstractDis",
    props: ['friend'],
    data() {
        return {
            isShow: false,
            paths: '',
            p: [],
            publicPath: process.env.BASE_URL,
            url: '',
        }
    },
    mounted() {
        
        this.judge(this.friend)

    },
    methods: {
        clickHand(id) {
            this.$router.push({
                path: `/InfoList/InfoDetail/${id}`
            })
        },
        judge(id) {
            axios.post('http://127.0.0.1:8000/json/showAvatar/', {name: id})
                .then((response) => {
                    console.log(response.data)
                    if(response.data['status'] == 0){
                        this.isShow = true
                        this.p = response.data['content']
                        this.url = "/InfoList/InfoDetail/" + this.p[0]
                        // this.paths = require("../../static/avatars/" + this.p[0] + '/' + this.p[1])
                        this.paths = this.publicPath + "static/avatars/" + this.p[0] + '/' + this.p[1]
                    } else {
                        this.isShow = false
                    }
                })
        }
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