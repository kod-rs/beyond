<template>


    <!-- <div class="row" id="demo">ffffff</div> -->

    <!-- <input type="text" value="ff" > -->
    your coordinates
    <input type="text" v-model="lat" :name="lat" class="form-control" />
    <input type="text" v-model="lon" :name="lon" class="form-control" />

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
    data() {
        return {
            lat: 0,
            lon: 0
        }
    },
    methods: {
        getUserLocation() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    this.showPosition,
                    this.showError, { timeout: 5000 });
            }
            else {
                alert("Geolocation is not supported by this browser.")
            }
        },
        showPosition(position) {
            this.$store.commit('setLatitude', position.coords.latitude);
            this.$store.commit('setLongitude', position.coords.longitude);
            this.lat = this.$store.state.latitude
            this.lon = this.$store.state.longitude


            alert("Latitude: " + position.coords.latitude +
                "<br>Longitude: " + position.coords.longitude);
        }
        , showError(error) {
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
    mounted() {
        // this.setLat()
        this.$store.commit('setLatitude', 15);
        // setLat() {
        this.$store.commit('setLatitude', 28);
        this.lat = this.$store.state.latitude

        // },

        this.getUserLocation()
        // (this.$store.$store.latitude)
        // this.lat = this.$store.$store.latitude
        // this.lon = this.$store.$store.longitude

    },

    setup() {

        // this.updateLocation(2, 3)
        // this.storeVals()
        // this.$store.commit('setLatitude', 15);

        // const getUserLocation = () => {
        //     if (navigator.geolocation) {
        //         navigator.geolocation.getCurrentPosition(position => {
        //             this.$store.commit('setLatitude', position.coords.latitude);
        //             this.$store.commit('setLongitude', position.coords.longitude);

        //             alert("Latitude: " + position.coords.latitude +
        //                 "<br>Longitude: " + position.coords.longitude);
        //         })
        //     }

        // }
        const getUserLocation = () => {
            // this.$store.commit('setLatitude', 25);
            // this.content = event.target.value.trim() // Formatting example
            // this.$store.commit('setSynchronizerToken', this.content)
            console.log("get user location")
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(showPosition, showError, { timeout: 5000 });
            }
            else {
                alert("Geolocation is not supported by this browser.")
            }
        }
        const showPosition = (position) => {
            // var x = document.getElementById("demo");
            // this.$store.commit('setLatitude', position.coords.latitude);
            // this.$store.commit('setLongitude', position.coords.longitude);
            alert("Latitude: " + position.coords.latitude +
                "<br>Longitude: " + position.coords.longitude);
        }

        function showError(error) {
            // switch (error.code) {
            //     case error.PERMISSION_DENIED:
            //         alert("User denied the request for Geolocation.")
            //         break;
            //     case error.POSITION_UNAVAILABLE:
            //         alert("Location information is unavailable.")
            //         break;
            //     case error.TIMEOUT:
            //         alert("The request to get user location timed out.")
            //         break;
            //     case error.UNKNOWN_ERROR:
            //         alert("An unknown error occurred.")
            //         break;
            // }
        }

        // getUserLocation();

        const center = ref([54.1966794, 31.8797732])

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