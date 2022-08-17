import { createRouter, createWebHistory } from 'vue-router';

import IndexPage from '../views/index/IndexPage';
import LocationAdd from "../views/location/Add.vue";
import LocationView from "../views/location/View.vue";
import LoginPage from '../views/login/LoginPage';

export const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/login',
      component: LoginPage
    },
    {
      path: '/',
      name: "index",
      component: IndexPage
    },
    {
      path: '/addlocation',
      name: "addlocation",
      component: LocationAdd
    },
    {
      path: '/viewlocation',
      name: "viewlocation",
      component: LocationView
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
  const loggedIn = sessionStorage.getItem('user');

  if (authRequired && !loggedIn) {
    return next({
      path: '/login',
      query: { returnUrl: to.path }
    });
  }
  next();
})