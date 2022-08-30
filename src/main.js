import { createApp } from 'vue';
import App from './App.vue'
import { router } from './scripts/router';
import { store } from "./scripts/store"
import OpenLayersMap from 'vue3-openlayers'
import 'vue3-openlayers/dist/vue3-openlayers.css'

const app = createApp(App);
const sts = require('strict-transport-security');
const globalSTS = sts.getSTS({ 'max-age': { 'days': 10 }, 'includeSubDomains': true });

app.use(router).use(store).mount('#app');
app.use(OpenLayersMap, globalSTS);
