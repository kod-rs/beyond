<template>

    <div id="root">


        <TopNavigationBar />

        <ContentNavigationBar />

        <main class="mt-5 pt-3">
            <div class="container-fluid">

                <div class="row">
                    add new
                    <LocationForm></LocationForm>

                </div>



            </div>
        </main>

    </div>

</template>

<script>
import { router } from '../../_helpers';
import { userService } from '../../_services';
import LocationForm from '../../components/LocationForm.vue';

export default {
    name: "f",
    data() {
        return {
            searchInput: "",
            modelFields: ["section", "type", "longitude", "latitude"],
            modelContent: [],
            // modelContent: [["a", "b", "c", "d"], ["f", "f", "g", "i"]],
            error: "",
            loading: false
        };
    },
    mounted() {
        // refreshLocations()

        userService.getAllLocations().then(res => {
            console.log("new locations");
            console.log(res);
            this.modelContent = res["payload"]["content"];
            console.log(this.modelContent);
        }, error => {
            console.log("err", error);
            this.error = "invalid credentials";
            // this.error = error;
            this.loading = false;
        });
    },
    methods: {
        refreshLocations() {
            console.log("refreshing locations");
            userService.getAllLocations().then(res => {
                console.log("new locations");
                console.log(res);
                this.modelContent = res["payload"]["content"];
                console.log(this.modelContent);
            }, error => {
                console.log("err", error);
                this.error = "invalid credentials";
                // this.error = error;
                this.loading = false;
            });
        },
        search() {
            this.fetchData();
        },
        async fetchData() {
            const apiKey = import.meta.env.tTT;
            const url = ``;
            this.searchInput = "";
            const res = await fetch(url);
            const jsonResponse = await res.json();
        },
        async deleteElement(i) {
            console.log("delete i", i)

            userService.deleteLocation(i).then(res => {
                console.log("location deleted");
                this.refreshLocations()

            }, error => {
                console.log("err", error);
                this.error = "invalid credentials";
                // this.error = error;
                this.loading = false;
            });

        }
    },
    components: { LocationForm }
}

</script>

<style>
/* @import './style.css'; */

#root {
    border-style: solid;
}
</style>
