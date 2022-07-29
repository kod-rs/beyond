
<template>

    <div>
        <div>
            <router-link :to="{ name: 'page1' }">page 1</router-link> |
            <router-link :to="{ name: 'page2' }">map</router-link> |
        </div>


        <router-view>
        </router-view>

        <p>
            <router-link to="/login">Logout</router-link>
        </p>


    </div>

</template>

<style>
</style>

<script>

export default {
    name: 'app'
};
</script>