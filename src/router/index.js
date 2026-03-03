import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Chant from '../views/Chant.vue'
import Prepare from '../views/prepare.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/prepare', component: Prepare },
  { path: '/:chapter', component: Chant, props: true }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    // 始终滚动到顶部
    return { top: 0 }
  }
})

export default router