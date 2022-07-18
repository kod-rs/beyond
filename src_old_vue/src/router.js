import Vue from 'vue'
import Router from 'vue-router'
import VueDemo from '@/components/VueDemo'
import Messages from '@/components/Messages'
import Login from '@/components/Login'
import LoginNew from '@/components/LoginNew'
import Dashboard from '@/components/Dashboard'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: VueDemo
    },
    {
      path: '/messages',
      name: 'messages',
      component: Messages
    },
    {
      path: '/login',
      name: 'login',
      // component: Login
      component: LoginNew
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard
    }


  ]
})
