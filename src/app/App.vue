<template>

    <div>
        <div>
            <router-link :to="{ name: 'dashboard' }">dashboard</router-link> |
            <router-link :to="{ name: 'login' }">login</router-link> |
            <router-link :to="{ name: 'home' }">home</router-link> |
            <router-link :to="{ name: 'messages' }">db communicator test</router-link>
        </div>


        <div class="jumbotron">
            <div class="container">
                <div class="row">
                    <div class="col-sm-6 offset-sm-3">
                        <router-view>
                        </router-view>
                    </div>
                </div>
            </div>
        </div>


    </div>


</template>

<script>
export default {
    name: 'app'
};
</script>