"use strict";(self["webpackChunktest_vue"]=self["webpackChunktest_vue"]||[]).push([[242],{5462:function(t,e,s){s.r(e),s.d(e,{default:function(){return z}});var a=s(6252),n=s(3577),i=s(2677),l=s.p+"assets/img/more-horizontal.97cf994a.svg",o=s.p+"assets/img/user-plus.aab4d264.svg",r=s(363),u=s(6164),p=s(5428);const m=t=>((0,a.dD)("data-v-242141af"),t=t(),(0,a.Cn)(),t),f={class:"InfoDetail"},h={class:"PP3 Detail Page"},d=m((()=>(0,a._)("img",{src:i},null,-1))),g=m((()=>(0,a._)("img",{src:l},null,-1))),c=["src"],_=m((()=>(0,a._)("img",{src:o},null,-1))),v=m((()=>(0,a._)("img",{style:{"margin-left":"0px","margin-top":"720px"},src:r},null,-1))),w=m((()=>(0,a._)("img",{style:{"margin-left":"30px","margin-top":"720px"},src:u},null,-1))),b=m((()=>(0,a._)("img",{style:{"margin-left":"30px","margin-top":"720px"},src:p},null,-1)));function I(t,e,s,i,l,o){const r=(0,a.up)("router-link"),u=(0,a.up)("backBtn"),p=(0,a.up)("moreInfoBtn"),m=(0,a.up)("headPic"),I=(0,a.up)("addFriend"),y=(0,a.up)("mid"),W=(0,a.up)("mydiv");return(0,a.wg)(),(0,a.iD)(a.HY,null,[(0,a._)("div",f,[(0,a.Wm)(y,null,{default:(0,a.w5)((()=>[(0,a._)("div",h,[(0,a.Wm)(u,{href:"https://",target:"_blank",rel:"noopener"},{default:(0,a.w5)((()=>[(0,a.Wm)(r,{to:"/InfoList"},{default:(0,a.w5)((()=>[d])),_:1})])),_:1}),(0,a.Wm)(p,{href:"https://",target:"_blank",rel:"noopener"},{default:(0,a.w5)((()=>[(0,a.Wm)(r,{to:"/UpdateInfo"},{default:(0,a.w5)((()=>[g])),_:1})])),_:1}),(0,a.Wm)(m,{href:"https://",target:"_blank",rel:"noopener"},{default:(0,a.w5)((()=>[(0,a._)("img",{src:l.avatar},null,8,c)])),_:1}),(0,a.Wm)(I,{href:"https://",target:"_blank",rel:"noopener"},{default:(0,a.w5)((()=>[_])),_:1})])])),_:1})]),(0,a.Wm)(W,null,{default:(0,a.w5)((()=>[(0,a._)("h2",null,"Name: "+(0,n.zw)(l.name),1),(0,a._)("h2",null,"Identity: "+(0,n.zw)(l.identity),1),(0,a._)("h2",null,"Info: "+(0,n.zw)(l.info),1),(0,a._)("h2",null,"Otherinfo: "+(0,n.zw)(l.optional),1)])),_:1}),(0,a._)("div",null,[(0,a.Wm)(r,{to:"/FirstPage"},{default:(0,a.w5)((()=>[v])),_:1}),(0,a.Wm)(r,{to:"/PostPage"},{default:(0,a.w5)((()=>[w])),_:1}),(0,a.Wm)(r,{to:"/InfoList"},{default:(0,a.w5)((()=>[b])),_:1})])],64)}s(7658);var y=s(9669),W=s.n(y),k={name:"InfoDetail",components:{},data(){return{username:"",bloglist:[],name:"",identity:"",info:"",optional:"",avatar:"",publicPath:"/vue_with_route/dist/"}},mounted(){this.username=this.$route.params.username,this.showUserInfo()},methods:{showUserInfo(){W().post("http://127.0.0.1:8000/json/showUserInfo/",{name:this.$route.params.username}).then((t=>{console.log(t.data),1!=t.data["status"]?(alert("Sorry but you are not login"),this.$router.push("/")):(this.bloglist=t.data["content"],this.name=this.bloglist[0].name,this.identity=this.bloglist[0].identity,this.info=this.bloglist[0].info,this.optional=this.bloglist[0].optional,this.avatar=this.publicPath+"static/avatars/"+this.name+"/square_"+this.bloglist[0].avatar)}))}}},x=s(3744);const P=(0,x.Z)(k,[["render",I],["__scopeId","data-v-242141af"]]);var z=P},5428:function(t,e,s){t.exports=s.p+"assets/img/message-circle.0e89ed1d.svg"},6164:function(t,e,s){t.exports=s.p+"assets/img/plus.41e8021f.svg"},363:function(t,e,s){t.exports=s.p+"assets/img/多选.7719a2d6.svg"},2677:function(t,e,s){t.exports=s.p+"assets/img/箭头二.eeccc4ae.svg"}}]);