import { createApp } from 'vue';
import App from './template/App.vue'
import { router } from './_helpers';

const app = createApp(App);
app.use(router).mount('#app');

import TopNavigationBar from './components/TopNavigationBar.vue'
import ContentNavigationBar from './components/ContentNavigationBar.vue'
import Map from './components/Map.vue'

app
    .component('TopNavigationBar', TopNavigationBar)
    .component('ContentNavigationBar', ContentNavigationBar)
    .component('Map', Map)

// webpack

console.log("src index")