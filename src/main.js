import { createApp } from 'vue';
import App from './template/App.vue'
import { router } from './_helpers';

const app = createApp(App);
app.use(router).mount('#app');

import TopNavigationBar from './components/TopNavigationBar.vue'
import ContentNavigationBar from './components/ContentNavigationBar.vue'
import Map from './components/Map.vue'
import LocationForm from './components/LocationForm.vue'

import OpenLayersMap from 'vue3-openlayers'
import 'vue3-openlayers/dist/vue3-openlayers.css'

const hsts = require('hsts')

app.use(OpenLayersMap);

app.use(hsts({maxAge: 15552000})) // 180 days in seconds

app
    .component('TopNavigationBar', TopNavigationBar)
    .component('ContentNavigationBar', ContentNavigationBar)
    .component('Map', Map)
    .component('LocationForm', LocationForm)

// webpack

console.log("src index")