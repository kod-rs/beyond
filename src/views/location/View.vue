<template>

    <div id="root">
        <NavigationTemplate />

        <main class="mt-5 pt-3">
            <div class="container-fluid">

                <div class="row">
                    <!-- <input v-model="searchInput" @keyup.enter="search" placeholder="Enter place" /> -->
                    <button @click="refreshLocations">refresh locations, maybe someone else placed something
                        new</button>
                </div>

                <hr>
                <hr>
                <hr>

                <div class="row">
                    <div class="col-md-12 mb-3">
                        only showing locations for this user
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
                                                <!-- <td>{{ i }}</td> -->
                                                <td v-for="(jitem) in item" :key="jitem.id">{{ jitem }}</td>
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

export default {
    name: "viewLocation",
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
        this.refreshLocations()
    },
    methods: {
        refreshLocations() {
            console.log("refreshing locations");
            apiCalls.getLocationsFilterUsername().then(res => {
                this.modelContent = res["payload"]["content"];
            }, error => {
                console.log("err", error);
                this.error = "invalid credentials";
                // this.error = error;
                this.loading = false;
            });
        },

        async deleteElement(i) {
            console.log("delete i", i);
            apiCalls.deleteLocation(i).then(() => {
                console.log("location deleted");
                this.refreshLocations();
            }, error => {
                console.log("err", error);
                this.error = "invalid credentials";
                // this.error = error;
                this.loading = false;
            });
        }
    }

}

</script>

<style>
#root {
    border-style: solid;
}
</style>
