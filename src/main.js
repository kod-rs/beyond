// import { createApp } from 'vue';
import App from './App.vue'
import { router } from './router/router';
import { store } from "./store/store"

import OpenLayersMap from 'vue3-openlayers'
import 'vue3-openlayers/dist/vue3-openlayers.css'

import WaveUI from 'wave-ui'
import 'wave-ui/dist/wave-ui.css'

import BalmUI from 'balm-ui'; // Official Google Material Components
import BalmUIPlus from 'balm-ui/dist/balm-ui-plus'; // BalmJS Team Material Components

// import Toast from "vue-toastification";
// import "vue-toastification/dist/index.css";
// import "vue-toastification/dist/index.css";
// import "vue-toastification/dist/index.css";

import { createApp } from 'vue/dist/vue.esm-bundler';
// import ToastPlugin from 'vue-toast-notification';
// import 'vue-toast-notification/dist/theme-sugar.css';





import Toast from "vue-toastification";
// Import the CSS or use your own!
import "vue-toastification/dist/index.css";


const app = createApp(App)
const sts = require('strict-transport-security');
const globalSTS = sts.getSTS({ 'max-age': { 'days': 10 }, 'includeSubDomains': true });

new WaveUI(app, {
    // notificationManager: {
    //     align: 'left', // Or 'left'.
    //     bottom: true,
    //     transition: 'default' // Sliding from the side by default.
    //   }
    // Some Wave UI options.
})


app.use(Toast, {
    transition: "Vue-Toastification__bounce",
    maxToasts: 20,
    newestOnTop: true
  });

app.use(BalmUI); // Mandatory
app.use(BalmUIPlus); // Optional

app.use(router).use(store).mount('#app');
app.use(OpenLayersMap, globalSTS);


