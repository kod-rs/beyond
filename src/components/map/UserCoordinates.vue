<template>
    your coordinates
    <input type="text" v-model="lat" :name="lat" class="form-control" />
    <input type="text" v-model="lon" :name="lon" class="form-control" />
    <!-- <button @click="$emit('userCoordinates', this.lat, this.lon)">click me</button> -->
    <button @click="emitCoordinates()">zoom on my location</button>
</template>

<script>
import { apiExternal } from '@/scripts/api/external';


export default {
    props: { "canSend": Boolean },
    emits: ["userCoordinates"],
    data() {
        return {
            lat: 0,
            lon: 0,
            canEmit: false
        };
    },
    methods: {
        enableCoordinates() {

            console.log("now i can emit")
            this.canEmit = true;
        },
        emitCoordinates() {
            console.log("try to emit")
            if (this.canEmit) {
                this.$emit('userCoordinates', this.lat, this.lon);

            }
        }
        ,

        displayUserCoordinatesWillingly() {
            navigator.geolocation.getCurrentPosition(this.showPosition, this.showError, { timeout: 5000 });
        },
        async displayUserCoordinatesUnwillingly() {
            let r = await apiExternal.getCoordinates();
            this.showPosition({
                coords: r
            });
        },
        showPosition(position) {
            this.$store.commit("setLatitude", position.coords.latitude);
            this.$store.commit("setLongitude", position.coords.longitude);

            this.lat = this.$store.state.latitude;
            this.lon = this.$store.state.longitude;
            this.emitCoordinates();
        },
        showError(error) {
            switch (error.code) {
                case error.PERMISSION_DENIED:
                    // alert("User denied the request for Geolocation.");
                    break;
                case error.POSITION_UNAVAILABLE:
                    // alert("Location information is unavailable.");
                    break;
                case error.TIMEOUT:
                    // alert("The request to get user location timed out.");
                    break;
                case error.UNKNOWN_ERROR:
                    // alert("An unknown error occurred.");
                    break;
            }
            this.displayUserCoordinatesUnwillingly();
        }
    },
    mounted() {
        this.emitCoordinates();

        if (navigator.geolocation) {
            this.displayUserCoordinatesWillingly();
        } else {
            alert("Geolocation is not supported by this browser");
            this.displayUserCoordinatesUnwillingly();
        }

    }
}
</script>