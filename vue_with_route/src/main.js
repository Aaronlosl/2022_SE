import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import qs from 'qs'
// import { Button, Input } from 'element-ui';


const app = createApp(App)
// app.use(ElementUI)
app.use(router).mount('#app')
app.prototype.$axios = axios;
app.prototype.$qs = qs;
