<template>

    <div> test </div>

    <div id="map" class="map"></div>
    <MapPopup ref="mappopup"></MapPopup>

</template>


    <style>
    .map {
        width: 100%;
        height: 800px;
    }
    </style>

<script>
import Map from 'ol/Map';

import TileLayer from 'ol/layer/Tile';
import View from 'ol/View';

import OSM from 'ol/source/OSM';
import { toLonLat } from 'ol/proj';
import { toStringHDMS } from 'ol/coordinate';



export default {
    data() {

    },
    mounted() {


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
            target: 'map',
            view: new View({
                center: [0, 0],
                zoom: 2,
            }),
        });

        map.addOverlay(this.$refs.mappopup.getOverlay())

        /**
         * Add a click handler to the map to render the popup.
         */
        map.on('singleclick', (evt) => {

            const coordinate = evt.coordinate;
            const hdms = toStringHDMS(toLonLat(coordinate));

            console.log("log coord", hdms)
            console.log("set postiion,", coordinate)
            this.$refs.mappopup.setText(hdms);
            this.$refs.mappopup.setPosition(coordinate);

        });
    }

};
</script> 