"use strict";(self["webpackChunktest_vue"]=self["webpackChunktest_vue"]||[]).push([[479],{8614:function(t,e,n){n.d(e,{Z:function(){return g}});var l=n(6252),s=n(363),a=n(6164),r=n(5428);const o=(0,l._)("img",{style:{"margin-left":"0px","margin-top":"200px"},src:s},null,-1),u=(0,l._)("img",{style:{"margin-left":"90px","margin-top":"200px"},src:a},null,-1),i=(0,l._)("img",{style:{"margin-left":"90px","margin-top":"200px"},src:r},null,-1);function c(t,e,n,s,a,r){const c=(0,l.up)("router-link");return(0,l.wg)(),(0,l.iD)("div",null,[(0,l.Wm)(c,{to:"/FirstPage"},{default:(0,l.w5)((()=>[o])),_:1}),(0,l.Wm)(c,{to:"/PostPage"},{default:(0,l.w5)((()=>[u])),_:1}),(0,l.Wm)(c,{to:"/InfoList"},{default:(0,l.w5)((()=>[i])),_:1})])}var p={name:"NaviBox"},m=n(3744);const d=(0,m.Z)(p,[["render",c]]);var g=d},1479:function(t,e,n){n.r(e),n.d(e,{default:function(){return C}});var l=n(6252),s=n(9963),a=n(9574),r=n(4492);const o=t=>((0,l.dD)("data-v-7036e01d"),t=t(),(0,l.Cn)(),t),u={class:"home"},i=o((()=>(0,l._)("h1",null,[(0,l._)("img",{src:a})],-1))),c=o((()=>(0,l._)("h1",null,"Student Request Post",-1))),p=o((()=>(0,l._)("br",null,null,-1))),m=o((()=>(0,l._)("br",null,null,-1))),d=o((()=>(0,l._)("br",null,null,-1))),g=o((()=>(0,l._)("textarea",{maxlength:"25",placeholder:"less than 25 characters",cols:"32",style:{resize:"none"}},null,-1))),h=o((()=>(0,l._)("br",null,null,-1))),_=o((()=>(0,l._)("br",null,null,-1))),f=o((()=>(0,l._)("br",null,null,-1))),x=o((()=>(0,l._)("img",{src:r},null,-1))),v=[x];function k(t,e,n,a,r,o){const x=(0,l.up)("t"),k=(0,l.up)("navi-box");return(0,l.wg)(),(0,l.iD)("div",u,[i,c,(0,l._)("h2",null,[(0,l._)("p",null,[(0,l.Wm)(x,{style:{"margin-right":"200px"}},{default:(0,l.w5)((()=>[(0,l.Uk)("Name")])),_:1}),p,(0,l.wy)((0,l._)("textarea",{maxlength:"25",placeholder:"less than 25 characters",cols:"32",style:{resize:"none"},"onUpdate:modelValue":e[0]||(e[0]=t=>r.title=t)},null,512),[[s.nr,r.title]]),m]),(0,l._)("p",null,[(0,l.Wm)(x,{style:{"margin-right":"185px"}},{default:(0,l.w5)((()=>[(0,l.Uk)("Abstract")])),_:1}),d,g,h]),(0,l._)("p",null,[(0,l.Wm)(x,{style:{"margin-right":"205px"}},{default:(0,l.w5)((()=>[(0,l.Uk)("Detail")])),_:1}),_,(0,l.wy)((0,l._)("textarea",{maxlength:"500",placeholder:"less than 500 characters",cols:"32",rows:"10",style:{resize:"none"},"onUpdate:modelValue":e[1]||(e[1]=t=>r.content=t)},null,512),[[s.nr,r.content]]),f])]),(0,l._)("button",{onClick:e[2]||(e[2]=t=>o.Post()),style:{"margin-left":"200px"}},v),(0,l.Wm)(k)])}n(7658);var y=n(9669),w=n.n(y),b=n(8614);w().interceptors.request.use((t=>{t.headers["X-Requested-With"]="XMLHttpRequest";let e=/.*csrftoken=([^;.]*).*$/;return t.headers["X-CSRFToken"]=null===document.cookie.match(e)?null:document.cookie.match(e)[1],t}));var P={components:{NaviBox:b.Z},name:"PostDetail1",data(){return{title:"",content:""}},methods:{Post(){""==this.title||""==this.content?alert("Please check your input"):w().post("http://127.0.0.1:8000/json/post/",{title:this.title,content:this.content,post_type:"Student Request"}).then((t=>{console.log(t.data),1!=t.data["status"]?(alert(t.data["message"]),this.$router.push("/")):(alert(t.data["message"]),this.$router.push("/FirstPage"))}))}}},W=n(3744);const q=(0,W.Z)(P,[["render",k],["__scopeId","data-v-7036e01d"]]);var C=q},9574:function(t,e,n){t.exports=n.p+"assets/img/logo.c938592f.svg"},5428:function(t,e,n){t.exports=n.p+"assets/img/message-circle.0e89ed1d.svg"},6164:function(t,e,n){t.exports=n.p+"assets/img/plus.41e8021f.svg"},4492:function(t,e,n){t.exports=n.p+"assets/img/send.19d54b57.svg"},363:function(t,e,n){t.exports=n.p+"assets/img/多选.7719a2d6.svg"}}]);
//# sourceMappingURL=479.d3e29938.js.map