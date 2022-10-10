import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// import { Button, Input } from 'element-ui';


const app = createApp(App)
// app.use(ElementUI)
app.use(router).mount('#app')
 