import { createRouter, createWebHistory } from 'vue-router';

import IndexPage from '../views/index/IndexPage';
import LoginPage from '../views/login/LoginPage';
import LocationAdd from "../views/location/AddLocation.vue";
import LocationView from "../views/location/View.vue";
import Location from "../views/location/Home.vue";
import LogoutPage from '../views/logout/LogoutPage';
import PortfolioPage from '../views/portfolio/Index.vue';

export const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/login',
      component: LoginPage
    },
    {
      path: '/logout',
      component: LogoutPage
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
      path: '/portfolio',
      name: "portfolio",
      component: PortfolioPage
    },
    {
      path: "/locations",
      name: "locations",
      component: Location
    },

    // {
    //   path: '/location',
    //   component: Location,
    //   children: [,
    //     { path: '', component: Location },
    //     {
    //       path: '/addlocation',
    //       name: "addlocation",
    //       component: LocationAdd
    //     },
    //     {
    //       path: '/viewLocation',
    //       name: "viewlocation",
    //       component: LocationView
    //     },

    //   ]
    // },
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

// router.beforeEach((to, from, next) => {
//   if (!isAuthenticated) next('/login')
//   else next()
// })