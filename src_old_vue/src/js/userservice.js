
import VueDemo from '@/components/VueDemo'
import LoginNew from '@/components/LoginNew'

export const userService = {
    login,
    logout,
    getAll
};

import Vue from 'vue';
import Router from 'vue-router';
import Dashboard from '@/components/Dashboard'

Vue.use(Router);

export const router = new Router({
  mode: 'history',
  routes: [
    // { path: '/', component: HomePage },
    // { path: '/login', component: LoginPage },

    {
        path: '/',
        name: 'home',
        component: VueDemo
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
      },
  


    // otherwise redirect to home
    { path: '*', redirect: '/' }
  ]
});

// router.beforeEach((to, from, next) => {
//     // redirect to login page if not logged in and trying to access a restricted page
//     const publicPages = ['/login'];
//     const authRequired = !publicPages.includes(to.path);
//     const loggedIn = localStorage.getItem('user');
  
//     if (authRequired && !loggedIn) {
//       return next({ 
//         path: '/login', 
//         query: { returnUrl: to.path } 
//       });
//     }
  
//     next();
//   })



function login(username, password) {
    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    };

    let user = {
        id: "user.id",
        username: "user.username",
        firstName: "user.firstName",
        lastName: "user.lastName"
    };

         // to keep user logged in between page refreshes
        //  user.authdata = window.btoa(username + ':' + password);
        //  localStorage.setItem('user', JSON.stringify(user));



    // return user;

    const myPromise = new Promise((resolve, reject) => {
        setTimeout(() => {
            let user = {
                id: "user.id",
                username: "user.username",
                firstName: "user.firstName",
                lastName: "user.lastName"
            };
        
            resolve(user)
            // resolve('foo');
        }, 300);
      });
      
    return  myPromise
        .then(
            user => {
                user.authdata = window.btoa(username + ':' + password);
                localStorage.setItem('user', JSON.stringify(user));
                return user;

            }

        );
      

    return fetch(`${config.apiUrl}/users/authenticate`, requestOptions)
        .then(handleResponse)
        .then(user => {
            // login successful if there's a user in the response
            if (user) {
                // store user details and basic auth credentials in local storage 
                // to keep user logged in between page refreshes
                user.authdata = window.btoa(username + ':' + password);
                localStorage.setItem('user', JSON.stringify(user));
            }

            return user;
        });
}

function logout() {
    // remove user from local storage to log user out
    localStorage.removeItem('user');
}

function getAll() {
    const requestOptions = {
        method: 'GET',
        headers: authHeader()
    };

    return fetch(`${config.apiUrl}/users`, requestOptions).then(handleResponse);
}

function handleResponse(response) {
    return response.text().then(text => {
        const data = text && JSON.parse(text);
        if (!response.ok) {
            if (response.status === 401) {
                // auto logout if 401 response returned from api
                logout();
                location.reload(true);
            }

            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
        }

        return data;
    });
}