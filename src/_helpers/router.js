import { createRouter, createWebHistory } from 'vue-router';

import IndexPage from '../index/IndexPage';
import LoginPage from '../login/LoginPage';
import Page1 from "../page1/Page1";
import Page2 from "../page2/Page2";

export const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/login',
      component: LoginPage
    },
    {
      path: '/',
      component: IndexPage
    },
    {
      path: '/page1',
      name: "page1",
      component: Page1
    },
    {
      path: '/page2',
      name: "page2",
      component: Page2
    },
    {
      path: '/:pathMatch(.*)*',
      redirect: '/'
    }
  ]
});

router.beforeEach((to, from, next) => {
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