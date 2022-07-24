import Vue from 'vue';
import Router from 'vue-router';

import HomePage from '../home/HomePage'
import LoginPage from '../login/LoginPage'
import IndexPage from '../index/IndexPage'
// import MessagesPage from '../messages/MessagesPage'
import Page1 from "../page1/Page1"
import Page2 from "../page2/Page2"

Vue.use(Router);

export const router = new Router({
  mode: 'history',
  routes: [
    // { path: '/home', component: HomePage },
    { path: '/login', component: LoginPage },
    { path: '/', component: IndexPage },
    { path: '/page1', name: "page1", component: Page1 },
    { path: '/page2', name: "page2",component: Page2 },
    
    // { path: '/msg', component: MessagesPage },

    // otherwise redirect to home
    { path: '*', redirect: '/' }
  ]
});

router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page
  const publicPages = ['/login'];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem('user');

  if (authRequired && !loggedIn) {
    return next({ 
      path: '/login', 
      query: { returnUrl: to.path } 
    });
  }

  next();
})