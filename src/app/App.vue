<template>

    <div>
        <div>
            <router-link :to="{ name: 'page1' }">page 1</router-link> |
            <router-link :to="{ name: 'page2' }">page 2</router-link> |
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

        <p>
            <router-link to="/login">Logout</router-link>
        </p>


    </div>


</template>

<script>
export default {
    name: 'app'
};
</script>