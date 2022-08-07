import { createApp } from 'vue';
import App from './template/App.vue'
import { router } from './_helpers';





// import { createApp } from 'vue'
import { createStore } from 'vuex'

// Create a new store instance.
const store = createStore({
    state() {
        return {
            count: 0,
            synchronizer_token: ""
        }
    },
    mutations: {
        increment(state) {
            state.count++
        },
        setSynchronizerToken(synchronizer_token, newValue) {
            synchronizer_token = newValue;
        }
    }
})







const app = createApp(App);




app.use(store)





app.use(router).mount('#app');

import TopNavigationBar from './components/TopNavigationBar.vue'
import ContentNavigationBar from './components/ContentNavigationBar.vue'
import Map from './components/Map.vue'
import LocationForm from './components/LocationForm.vue'
import CSRFToken from './components/CSRFToken.vue'

import OpenLayersMap from 'vue3-openlayers'
import 'vue3-openlayers/dist/vue3-openlayers.css'

const sts = require('strict-transport-security');
const globalSTS = sts.getSTS({ 'max-age': { 'days': 10 }, 'includeSubDomains': true });

app.use(OpenLayersMap, globalSTS);

app
    .component('TopNavigationBar', TopNavigationBar)
    .component('ContentNavigationBar', ContentNavigationBar)
    .component('Map', Map)
    .component('LocationForm', LocationForm)
    .component('CSRFToken', CSRFToken)

// webpack

console.log("src index")