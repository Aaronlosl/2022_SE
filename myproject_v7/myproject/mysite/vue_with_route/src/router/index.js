import { createRouter, createWebHashHistory } from 'vue-router'
import SignIn from '../views/SignIn.vue'

const routes = [
  {
    path: '/',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/FirstPage',
    name: 'FirstPage',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/FirstPage.vue')
  },
  {
    path: '/PP1Search',
    name: 'PP1Search',
    component: () => import('../views/PP1Search')
  },
  {
    path: '/PP3Detail',
    name: 'PP3Detail',
    component: () => import('../views/PP3Detail')
  },
  {
    path: '/PP1Result',
    name: 'PP1Result',
    component: () => import('../views/PP1Result')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
