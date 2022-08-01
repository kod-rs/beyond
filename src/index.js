import { createApp } from 'vue';
import App from './template/App.vue'
import { router } from './_helpers';

const app = createApp(App);
app.use(router).mount('#app');

// import MyComponent from './App.vue'
import TopNavigationBar from './components/TopNavigationBar.vue'
import ContentNavigationBar from './components/ContentNavigationBar.vue'

app
    .component('TopNavigationBar', TopNavigationBar)
    .component('ContentNavigationBar', ContentNavigationBar)


// webpack

console.log("src index")