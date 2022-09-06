<!-- todo no reloading -->

<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col">
                <!-- add new -->
                <br>
                <!-- <hr> -->
                <div v-if="error" class="alert alert-danger">{{ error }}</div>


                <form @submit.prevent="handleSubmit">

                    <h5>csrf</h5>
                    <CSRFToken />

                    <h5>input part</h5>
                    <InputFieldsForm ref="inputFields"></InputFieldsForm>

                    <h5>portfolio selector</h5>
                    <PortfolioSelector ref="portfolioSelector"></PortfolioSelector>

                    <hr>
                    hidden
                    <hr>
                    lon
                    <input type="text" v-model="latitude">
                    lat
                    <input type="text" v-model="longitude">

                    <hr>

                    <button class="btn btn-primary btn-dark btn-lg btn-block" :disabled="loading">add</button>

                    <LoadingComponent></LoadingComponent>

                </form>
            </div>
            <div class="col">
                <div id="map" class="map"></div>
                <MapPopup ref="mappopup"></MapPopup>

            </div>
        </div>
    </div>


</template>

    


<script>

import CSRFToken from "../../components/form/CSRFToken.vue"
import MapPopup from "../../components/map/MapPopup.vue"
import { apiLocation } from '../../scripts/api/location';
import Map from 'ol/Map';

import TileLayer from 'ol/layer/Tile';
import View from 'ol/View';

import OSM from 'ol/source/OSM';
import { toLonLat } from 'ol/proj';
import { toStringHDMS } from 'ol/coordinate';


import PortfolioSelector from '../../components/form/PortfolioSelector.vue';
import LoadingComponent from "@/components/misc/LoadingComponent.vue";
import InputFieldsForm from "@/components/misc/InputFieldsForm.vue";


export default {

    data() {
        return {
            checkedNames: [],
            hover: false,

            latitude: undefined,
            longitude: undefined,

            submitted: false,
            loading: false,
            error: undefined,
        };
    },
    watch: {
        // whenever question changes, this function will run
        // question(newQuestion, oldQuestion) {
        //     if (newQuestion.includes('?')) {
        //         this.getAnswer()
        //     }
        // }
    },
    methods: {


        async handleSubmit() {
            console.log("submit for p",)
            // return
            this.submitted = true;
            this.error = "";
            // let formContent = {};
            // for (const element of this.formData) {
            //     if (element.value) {
            //         formContent[element.key] = element.value;
            //     }
            //     else {
            //         this.error = "fields not filled";
            //         return;
            //     }
            // }
            const csrfToken = this.$store.state.synchronizerToken;

            let section = this.$refs.inputFields.fields["Section"]["value"];
            let type = this.$refs.inputFields.fields["Section"]["value"];

            // check if portfolio input has content and is valid

            let portfolio = this.$refs.portfolioSelector.getSearch();
            console.log("port", portfolio);

            await apiLocation.addLocation(
                portfolio,
                section,
                type,
                this.latitude,
                this.longitude,

                csrfToken

            ).then(r => {
                if (r.payload.status) {
                    alert("Location add successful.");
                }
                else {
                    alert("Location add failed.");
                }
            }, error => {
                alert("Location add failed.");
                console.log("error", error);
            });

            // restart fields insted of refresh site

            this.$router.go();
            this.submitted = false;
        }
    },
    async mounted() {



        /**
      * Create the map.
      *
     */
        const map = new Map({
            layers: [
                new TileLayer({
                    source: new OSM(),
                }),
            ],
            target: "map",
            view: new View({
                center: [0, 0],
                zoom: 2,
            }),
        });
        map.addOverlay(this.$refs.mappopup.getOverlay());
        /**
         * Add a click handler to the map to render the popup.
         */
        map.on("singleclick", (evt) => {
            const coordinate = evt.coordinate;
            const hdms = toStringHDMS(toLonLat(coordinate));

            this.longitude = toLonLat(coordinate)[0];
            this.latitude = toLonLat(coordinate)[1];

            // console.log("log coord", hdms);
            // console.log("set postiion,", coordinate);
            this.$refs.mappopup.setText(hdms);
            this.$refs.mappopup.setPosition(coordinate);
        });
    },
    components: { PortfolioSelector, CSRFToken, MapPopup, LoadingComponent, InputFieldsForm }
};
</script> 


<style>
.hint {
    background: #e3e3e3;
    border-radius: 50%;
    color: #6e6e6e;
    display: inline-block;
    font-weight: bold;
    text-align: center;
    width: 1.2vw;
    height: 1.2vw;
}

.hint_text {
    background: #e3e3e3;
    color: #6e6e6e;
    display: inline;
    text-align: center;
}
</style>