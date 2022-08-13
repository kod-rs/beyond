<template>
    fff
    <hr>
    <hr>
    <hr>
    <hr>

    <!-- <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top"> -->
    <div class="testnavigation">
        test navigation routes:
        <router-link :to="{ name: 'index' }">home</router-link> |
        <router-link :to="{ name: 'addlocation' }">Create</router-link> |
        <router-link :to="{ name: 'viewlocation' }">View</router-link> |
        <router-link to="/logout">Logout</router-link> |
        <router-link :to="{ name: 'portfolio' }">manage portfolio</router-link> |
        <router-link :to="{ name: 'locations' }">manage locations</router-link> |
        <!-- <router-link>delete portfolio</router-link> | -->


    </div>


</template>

<script>
export default {
    data() {
        return {

        }
    }
}
</script>

<style>
.testnavigation {
    border: 1mm solid black;
}
</style>

