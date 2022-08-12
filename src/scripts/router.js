import { createRouter, createWebHistory } from 'vue-router';

import IndexPage from '../views/index/IndexPage';
import LoginPage from '../views/login/LoginPage';
import LocationAdd from "../views/location/Add.vue";
import LocationView from "../views/location/View.vue";
import Location from "../views/location/Home.vue";
import LogoutPage from '../views/logout/LogoutPage';

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
  // console.log("to", to)
  // console.log("from", from)
  // console.log("next", next)

  let result = decodeURIComponent(to.path);
  // console.log(result);
  // console.log(to)
  // console.table(to)
  // console.table(to.query)

  // if (sessionStorage.getItem("user")) {
  // } else {


  // }

  const publicPages = ['/login'];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = sessionStorage.getItem('user');
  // console.log("is loged in", !!loggedIn)

  // console.table(from.query)
  // console.log(typeof (from.query))

  // console.log(!!loggedIn)
  // console.log(from.query)
  // console.log(from.query["returnUrl"])

  if (loggedIn && from.query.returnUrl) {
    // console.log(from.query.returnUrl)
    // console.log("", from.query.returnUrl)

    if (from.query.returnUrl === "" || from.query.returnUrl === "/") {
      // console.log("route")
    } else {
      // return next({
      //   path: from.query.returnUrl,
      //   query: {}
      // });

    }



  }

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