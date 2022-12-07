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
    path: '/InfoList',
    name: 'InfoList',
    component: () => import('../views/InfoList.vue'),
  },
  {
    path: '/InfoList/InfoDetail/:username',
    name: 'InfoDetail',
    component: () => import('../views/InfoDetail.vue'),
  },

  {
    path: '/InfoList/InfoDetail',
    name: 'InfoDetail_temp',
    component: () => import('../views/InfoDetail.vue'),
  },


  {
    path: '/PP1Search',
    name: 'PP1Search',
    component: () => import('../views/PP1Search.vue'),
  },
  {
    path: '/PP1Search/PP1Result/:search_content',
    name: 'PP1Result',
    component: () => import('../views/PP1Result.vue'),

  },
  {
    path: '/PP1Search/PP1Result/PP1Detail',
    name: 'PP1Detail',
    component: () => import('../views/PP1Detail.vue'),
  },


  {
    path: '/PP2Search',
    name: 'PP2Search',
    component: () => import('../views/PP2Search.vue'),
  },
  {
    path: '/PP2Search/PP2Result',
    name: 'PP2Result',
    component: () => import('../views/PP2Result.vue'),

  },
  {
    path: '/PP2Search/PP2Result/PP2Detail',
    name: 'PP2Detail',
    component: () => import('../views/PP2Detail.vue'),
  },

  {
    path: '/PP3Search',
    name: 'PP3Search',
    component: () => import('../views/PP3Search.vue'),
  },
  {
    path: '/PP3Search/PP3Result/:search_content',
    name: 'PP3Result',
    component: () => import('../views/PP3Result.vue'),

  },
  {
    path: '/PP3Search/PP3Result/PP3Detail',
    name: 'PP3Detail',
    component: () => import('../views/PP3Detail.vue'),
  },

  {
    path: '/PostPage',
    name: 'PostPage',
    component: () => import('../views/PostPage.vue')
  },

  {
    path: '/PostDetail1',
    name: 'PostDetail1',
    component: () => import('../views/PostDetail1.vue')
  },

  {
    path: '/PostDetail2',
    name: 'PostDetail2',
    component: () => import('../views/PostDetail2.vue')
  },

  {
    path: '/PostDetail3',
    name: 'PostDetail3',
    component: () => import('../views/PostDetail3.vue')
  },

  {
    path: '/UpdateInfo',
    name: 'UpdateInfo',
    component: () => import('../views/UpdateInfo.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
