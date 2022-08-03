<template>

    <div id="root">


        <TopNavigationBar />

        <ContentNavigationBar />

        <main class="mt-5 pt-3">
            <div class="container-fluid">



                <div class="row">




                    <Map />


                    <!-- <input v-model="searchInput" @keyup.enter="search" placeholder="Enter place" /> -->
                    <!-- <button @click="refreshLocations">refresh locations, maybe someone else placed something
                        new</button> -->
                </div>

                <!-- <hr>
                <hr>
                <hr> -->

                <!-- <div class="row">
                    <div class="col-md-12 mb-3">

                        <div class="card">
                            <div class="card-header">
                                <span><i class="bi bi-table me-2"></i></span> Locations

                            </div>
                            <div class="card-body">
                                <div class="table-responsive">
                                    <table id="example" class="table table-striped data-table" style="width: 100%">
                                        <thead>
                                            <tr>
                                                <th>id curr</th>
                                                <th>section</th>
                                                <th>type</th>
                                                <th>latitude</th>
                                                <th>longitude</th>
                                                <th>delete</th>
                                            </tr>
                                        </thead>
                                        <tbody>

                                            <tr v-for="(item, i) in modelContent" :key="item.id">
                                                <td v-for="(jitem, j) in item">{{ jitem }}</td>
                                                <td><button @click="deleteElement(modelContent[i]['pk'])">delete
                                                        id = {{ modelContent[i]["pk"] }}</button>
                                                </td>
                                            </tr>

                                        </tbody>
                                        <tfoot>
                                            <tr>
                                                <th></th>
                                                <th></th>
                                                <th></th>
                                                <th></th>
                                                <th></th>
                                                <th></th>
                                            </tr>
                                        </tfoot>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>
                </div> -->



            </div>
        </main>

    </div>

</template>

<script>
import { router } from '../_helpers';
import { userService } from '../_services';
import LocationForm from '../components/LocationForm.vue';

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
@import './style.css';

#root {
    border-style: solid;
}
</style>
