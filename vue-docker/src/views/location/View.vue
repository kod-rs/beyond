<template>

    <div id="root">
        <Navigation />
        <main class="mt-5 pt-3">
            <div class="container-fluid">
                <div class="row">
                    <button @click="refreshLocations">refresh locations, maybe someone else placed something
                        new</button>
                </div>
                <hr>
                <hr>
                <hr>
                <div class="row">
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
                </div>





            </div>
        </main>

    </div>

</template>

<script>
import { apiCalls } from '../../scripts/api';
import Navigation from '../../components/navigation/Navigation.vue';

export default {
    name: "f",
    data() {
        return {
            searchInput: "",
            modelFields: ["section", "type", "longitude", "latitude"],
            modelContent: [],
            error: "",
            loading: false
        };
    },
    mounted() {
        apiCalls.getAllLocations().then(res => {
            this.modelContent = res["payload"]["content"];
        }, error => {
            this.error = "invalid credentials";
            this.loading = false;
        });
    },
    methods: {
        refreshLocations() {
            apiCalls.getAllLocations().then(res => {
                this.modelContent = res["payload"]["content"];
            }, error => {
                this.error = "invalid credentials";
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
            apiCalls.deleteLocation(i).then(res => {
                this.refreshLocations();
            }, error => {
                this.error = "invalid credentials";
                this.loading = false;
            });
        }
    },
    components: { Navigation }
}

</script>

<style>
/* @import './style.css'; */

#root {
    border-style: solid;
}
</style>
