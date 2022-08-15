<template>

    <div class="testnavigation">
        test navigation routes:
        <router-link :to="{ name: 'index' }">home</router-link> |
        <router-link :to="{ name: 'addlocation' }">Create</router-link> |
        <router-link :to="{ name: 'viewlocation' }">View</router-link> |
        <router-link to="/logout">Logout</router-link> |
        <router-link :to="{ name: 'portfolio' }">manage portfolio</router-link> |
        <router-link :to="{ name: 'locations' }">manage locations</router-link> |
        <router-link :to="{ name: 'test' }">test</router-link> |


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

