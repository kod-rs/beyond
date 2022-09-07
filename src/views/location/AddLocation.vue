<!-- todo no reloading -->

<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col">
                <br>
                <div v-if="error" class="alert alert-danger">{{ error }}</div>

                <form @submit.prevent="handleSubmit">

                    <h5>csrf</h5>
                    <CSRFToken ref="csrf" />

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
                <MapComponent ref="map" id="map"></MapComponent>
                <MapPopup ref="mappopup"></MapPopup>

            </div>
        </div>
    </div>


</template>

    


<script>

import CSRFToken from "../../components/form/CSRFToken.vue"
import MapPopup from "../../components/map/MapPopup.vue"
import { apiLocation } from '../../scripts/api/location';
import { toLonLat } from 'ol/proj';
import { toStringHDMS } from 'ol/coordinate';


import PortfolioSelector from '../../components/form/PortfolioSelector.vue';
import LoadingComponent from "@/components/misc/LoadingComponent.vue";
import InputFieldsForm from "@/components/misc/InputFieldsForm.vue";
import MapComponent from "@/components/map/MapComponent.vue";


export default {

    data() {
        return {
            latitude: undefined,
            longitude: undefined,

            submitted: false,
            loading: false,
            error: undefined,

            map: undefined,
            view: undefined
        };
    },
    methods: {


        async handleSubmit() {
            this.$refs.inputFields.fields["Section"]["reset"] = false;
            this.$refs.inputFields.fields["Type"]["reset"] = false;

            this.submitted = true;
            this.error = "";

            let section = this.$refs.inputFields.fields["Section"]["value"];
            let type = this.$refs.inputFields.fields["Type"]["value"];

            if (!(section && type)) {
                this.error += "fill all fields"
            }
            if (!(this.latitude && this.longitude)) {
                this.error += "\nselect location"
            }

            // todo check portfolio
            const csrfToken = this.$store.state.synchronizerToken;

            if (!csrfToken) {
                alert("error with auth, reloading");
                this.$router.go();
            }

            let portfolio = this.$refs.portfolioSelector.getSearch();

            if (this.error) {
                return
            }

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

            // this.$router.go();

            // restart
            this.$refs.inputFields.fields["Section"]["value"] = "";
            this.$refs.inputFields.fields["Type"]["value"] = "";

            this.$refs.inputFields.fields["Section"]["reset"] = true;
            this.$refs.inputFields.fields["Type"]["reset"] = true;

            await this.$refs.csrf.refresh();

            this.$refs.mappopup.closePopup();
            this.longitude = "";
            this.latitude = "";

            this.submitted = false;
        }
    },
    async mounted() {
        this.map = this.$refs.map.map;
        this.view = this.$refs.map.view;


        this.map.addOverlay(this.$refs.mappopup.getOverlay());

        /**
         * Add a click handler to the map to render the popup.
         */
        this.map.on("singleclick", (evt) => {
            const coordinate = evt.coordinate;
            const hdms = toStringHDMS(toLonLat(coordinate));

            this.longitude = toLonLat(coordinate)[0];
            this.latitude = toLonLat(coordinate)[1];

            this.$refs.mappopup.setText(hdms);
            this.$refs.mappopup.setPosition(coordinate);
        });
    },
    components: { PortfolioSelector, CSRFToken, MapPopup, LoadingComponent, InputFieldsForm, MapComponent }
};
</script> 
