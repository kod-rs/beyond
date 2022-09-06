<template>
    <div id="map" class="map"></div>
</template>

<script>

import Map from 'ol/Map';
// import OSM from 'ol/source/OSM';
// import TileLayer from 'ol/layer/Tile';
import View from 'ol/View';
export default {
    data() {
        return {
            map: undefined,
            view: undefined
        }
    },
    methods: {
    },
    mounted() {
        this.view = new View({
            center: [0, 0],
            zoom: 2,
        });

        this.map = new Map({
            // layers: [
            //     new TileLayer({
            //         source: new OSM(),
            //     }),
            // ],
            target: 'map',
            view: this.view,
        });
    }

}
</script>