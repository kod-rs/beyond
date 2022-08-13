import { createApp } from 'vue';
import App from './template/App.vue'
import { router } from './scripts/router';
import { store } from "./scripts/store"
import Map from './components/map/Map.vue'
import CSRFToken from './components/form/CSRFToken.vue'
import InputAutocomplete from './components/form/InputAutocomplete.vue';
import TestNavigation from './components/navigation/TestNavigation.vue'
import Navigation from './components/navigation/Navigation.vue'
import OpenLayersMap from 'vue3-openlayers'
import 'vue3-openlayers/dist/vue3-openlayers.css'
const sts = require('strict-transport-security');
import TopNavigationBar from "./components/navigation/TopNavigationBar.vue";
const app = createApp(App);
import UserCoordinates from "./components/map/UserCoordinates.vue"


const globalSTS = sts.getSTS({ 'max-age': { 'days': 10 }, 'includeSubDomains': true });

app.use(router).use(store).mount('#app')

app
    .use(OpenLayersMap, globalSTS)
    .component('Map', Map)
    .component('CSRFToken', CSRFToken)
    .component("InputAutocomplete", InputAutocomplete)
    .component('Navigation', Navigation)
    .component("TestNavigation", TestNavigation)
    .component("TopNavigationBar", TopNavigationBar)
    .component("UserCoordinates", UserCoordinates)

console.log("production entry point")

/////////////////////////
// production entry point
/////////////////////////

