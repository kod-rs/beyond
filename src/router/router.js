import { createRouter, createWebHistory } from 'vue-router';

import IndexPage from '../views/index/IndexPage';
import LoginPage from '../views/login/LoginPage';
import LogoutPage from '../views/logout/LogoutPage';
import PortfolioPage from '../views/portfolio/Index.vue';
import TestPage from '../views/test/TestPage.vue';
import ForgotPassword from '../views/login/ForgotPassword.vue';
import TermsOfUse from '../views/login/TermsOfUse.vue';
import PrivacyPolicy from '../views/login/PrivacyPolicy.vue';
import HistoryView from '../views/history/HistoryView.vue';
import ChartView from '../views/graph/Index.vue';
import SetttingsView from '../views/settings/SettingsView.vue';

export const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/settings',
      name: 'settings',
      component: SetttingsView
    },
    {
      path: '/history',
      name: 'history',
      component: HistoryView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginPage
    },
    {
      path: '/chart/:portfolio/:section/:type',
      name: "chart",
      component: ChartView,
      params: true
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
      path: '/portfolio',
      name: "portfolio",
      component: PortfolioPage
    },
    {
      path: "/test",
      name: "test",
      component: TestPage
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
    },
    {
      path: '/forgotpassword',
      name: 'forgotpassword',
      component: ForgotPassword
    },
    {
      path: '/termsofuse',
      name: 'termsofuse',
      component: TermsOfUse
    },
    {
      path: '/privacypolicy',
      name: 'privacypolicy',
      component: PrivacyPolicy
    }
  ]
});

router.beforeEach((to, from, next) => {

  // fixme chart should not be public

  const publicPages = ['/login', '/forgotpassword', '/termsofuse', '/privacypolicy', '/logout', "/chart"];
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