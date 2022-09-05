<template>

    <div class="container-fluid">

        <!-- test routes:
        <router-link :to="{ name: 'addlocation' }">Create</router-link> |
        <router-link :to="{ name: 'viewlocation' }">View</router-link> |
        <router-link to="/logout">Logout</router-link> | -->
        <!-- <router-link>edit portfolio</router-link> |
        <router-link>delete portfolio</router-link> | -->
        <!-- <div class="row">
            <div class="col-sm">
                <div class="row">
                    r1
                </div>
            </div>
            <div class="col-sm">
                <div class="row">
                    r2 </div>
            </div>
            <div class="col-sm">
                r3 </div>
        </div>
        <hr> -->



        <!-- <hr> -->

        <!-- <button @click="createNewGroup">create new group</button> -->


        <form @submit.prevent="handleSubmit">

            portfolio name
            <input type="text" v-model="portfolioName">


        </form>

        <hr>

        <!-- <button @click="deletePortfolio">delete portfolio</button> -->


    </div>

</template>

<script>

export default {
    name: "portfolioIndex",
    components: {
    },
    data() {
        return {
            portfolioName: "tmp"
        }
    },
    methods: {
        // createNewGroup() {
        //     console.log("create new group")
        // },

        // handleSubmit() {
        //     this.submitted = true;
        //     const { username, password } = this;
        //     if (!(username && password)) {
        //         return;
        //     }
        //     this.loading = true;
        //     apiCalls.login(username, password).then(() => {
        //         router.push(this.returnUrl);
        //         this.$store.commit("setUsername", username);
        //     }, error => {
        //         this.error = "invalid credentials";
        //         this.error = error;
        //         this.loading = false;
        //     });
        // },
        deletePortfolio() {
            console.log("delete portfolio")
        }
    }
}
</script>

<style>
#map:focus {
    outline: #4A74A8 solid 0.15em;
}
</style>