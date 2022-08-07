<template>


    <!-- <div class="row" id="demo">ffffff</div> -->

    <!-- <input type="text" value="ff" > -->
    your coordinates
    <input type="text" v-model="lat" :name="lat" class="form-control" />
    <input type="text" v-model="lon" :name="lonn" class="form-control" />

    <ol-map :loadTilesWhileAnimating="true" :loadTilesWhileInteracting="true" style="height:400px">
        <ol-view ref="view" :center="center" :rotation="rotation" :zoom="zoom" :projection="projection" />

        <ol-tile-layer>
            <ol-source-osm />
        </ol-tile-layer>

        <ol-vector-layer>
            <ol-source-vector ref="vectors">
                <ol-interaction-draw @drawstart="drawstart" :type="drawType">
                </ol-interaction-draw>
            </ol-source-vector>

            <ol-style>
                <ol-style-icon :src="markerIcon" :scale="2"></ol-style-icon>
            </ol-style>
        </ol-vector-layer>

    </ol-map>
</template>

<script>
import markerIcon from './../../assets/login_logo.png'
import { ref } from "vue";

export default {
    name: "test",
    data() {
        return {
            lat: 0,
            lon: 0
        }
    },

    methods: {
        getUserLocation() {
            // this.content = event.target.value.trim() // Formatting example
            // this.$store.commit('setSynchronizerToken', this.content)
            console.log("get user location")
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(showPosition, showError, { timeout: 5000 });
            }
            else {

                alert("Geolocation is not supported by this browser.")
            }




        },
        showPosition(position) {
            var x = document.getElementById("demo");

            this.$store.commit('latitude', position.coords.latitude);
            this.$store.commit('longitude', position.coords.longitude);


            alert("Latitude: " + position.coords.latitude +
                "<br>Longitude: " + position.coords.longitude);
        },

        showError(error) {
            switch (error.code) {
                case error.PERMISSION_DENIED:
                    alert("User denied the request for Geolocation.")
                    break;
                case error.POSITION_UNAVAILABLE:
                    alert("Location information is unavailable.")
                    break;
                case error.TIMEOUT:
                    alert("The request to get user location timed out.")
                    break;
                case error.UNKNOWN_ERROR:
                    alert("An unknown error occurred.")
                    break;
            }
        }

    },
    setup() {
        // this.getUserLocation();


        const center = ref([54.1966794, 31.8797732])



        //  function getLocation() {


        // const center = ref([54.1966794, 31.8797732])
        const projection = ref('EPSG:4326')
        const zoom = ref(6)
        const rotation = ref(0)

        const markers = ref(null);
        const drawType = ref("Point")

        const drawedMarker = ref()
        const vectors = ref(null);

        const drawstart = (event) => {
            vectors.value.source.removeFeature(drawedMarker.value);
            drawedMarker.value = event.feature;
            console.log(vectors.value.source)
        }

        return {
            vectors,
            drawstart,
            center,
            projection,
            zoom,
            rotation,
            markerIcon,
            markers,
            drawType
        }
    }
}
</script>