// import { createApp } from 'vue'
// import App from './App.vue'

// createApp(App).mount('#app')


import { createApp } from 'vue';
import App from './App.vue'
const app = createApp(App);


import { router } from './scripts/router';
import { store } from "./scripts/store"

// import MapComponent from './components/map/MapComponent.vue'

import OpenLayersMap from 'vue3-openlayers'
import 'vue3-openlayers/dist/vue3-openlayers.css'
const sts = require('strict-transport-security');

const globalSTS = sts.getSTS({ 'max-age': { 'days': 10 }, 'includeSubDomains': true });

app.use(router).use(store).mount('#app')

app
    .use(OpenLayersMap, globalSTS)
// .component('MapComponent', MapComponent)

console.log("src index")


/////////////////////////
// development entry point
/////////////////////////
