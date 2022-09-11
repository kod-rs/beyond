<template>
    <div id="map"></div>
</template>

<script>

import Map from 'ol/Map';
import OSM from 'ol/source/OSM';
import TileLayer from 'ol/layer/Tile';
import View from 'ol/View';
export default {
    data() {
        return {
            map: undefined,
            // view: undefined
        }
    },
    methods: {
    },
    mounted() {
        // this.view = new View({
        //     center: [0, 0],
        //     zoom: 2,
        // });

        this.map = new Map({
            layers: [
                new TileLayer({
                    source: new OSM(),
                }),
            ],
            target: 'map',
            view: new View({
                center: [0, 0],
                zoom: 2,
            }),
        });

        this.$store.dispatch("setMap", this.map);

    }

}
</script>


<style>
/* #map:focus {
    outline: #4A74A8 solid 0.15em;
} */

#map {
    width: 45%;
    height: 90%;
    position: fixed;
    border: 1px solid #ccc;
}
</style>