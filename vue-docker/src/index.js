import { createApp } from 'vue';
import OpenLayersMap from 'vue3-openlayers';
import 'vue3-openlayers/dist/vue3-openlayers.css';
import CSRFToken from './components/form/CSRFToken.vue';
import Map from './components/map/Map.vue';
import Navigation from './components/navigation/Navigation.vue';
import { router } from './scripts/router';
import { store } from "./scripts/store";
import App from './template/App.vue';
const sts = require('strict-transport-security');

const app = createApp(App);

app.use(router).use(store).mount('#app');

const globalSTS = sts.getSTS({ 'max-age': { 'days': 10 }, 'includeSubDomains': true });

app.use(OpenLayersMap, globalSTS);

app
    .component('Map', Map)
    .component('CSRFToken', CSRFToken)
    .component('Navigation', Navigation)
