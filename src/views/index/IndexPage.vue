<template>


    <!-- <img src="./baseline_place_black_24dp.png" alt=""> -->

    <div class="container-fluid">

        <div class="row">
            image
            <!-- <img src="./baseline_place_black_24dp.png" alt=""> -->
        </div>

        <div class="row">
            <button>
                <router-link class="dropdown-item" to="/logout">Logout</router-link>
            </button>
        </div>

        <div class="row">
            <button @click="addLocation()">add location, when user wants to add new location to map</button>
            <div>
                lon: <div id="lon_tmp">1</div>
            </div>
            <div>
                lat: <div id="lat_tmp">2</div>
            </div>
        </div>

        <div class="row">
            <button>position map on user location</button>
        </div>

        <!-- <div class="row">
            <button>add this</button>
        </div> -->

        <div class="row">
            <button id="zoom-out">Zoom out</button>
            <button id="zoom-in">Zoom in</button>
        </div>

        <div class="row">
            <button @click="addLocation()">logout</button>
        </div>

        <div class="row">
            <div id="map" class="map" tabindex="0" style="width: 90%; height: 90%; 
                position:fixed; 
                border: 1px solid #ccc;">
            </div>

            <div style="display: none;">
                <div id="popup" title="Selected location"></div>
            </div>
        </div>

    </div>

</template>

<script>

import Map from 'ol/Map';
import OSM from 'ol/source/OSM';
import TileLayer from 'ol/layer/Tile';
import View from 'ol/View';
import Overlay from 'ol/Overlay';
import { toStringHDMS } from 'ol/coordinate';
import { fromLonLat, toLonLat } from 'ol/proj';
import Point from 'ol/geom/Point';
import Feature from 'ol/Feature';
import { Icon, Style } from 'ol/style';
import VectorSource from 'ol/source/Vector';
import { Vector as VectorLayer } from 'ol/layer';


import marker2 from "./../../assets/markers/baseline_place_black_24dp.png"
// import marker2 from "./baseline_place_black_24dp.png";

export default {
    data() {
        return {
            addLocationEnabled: false,

        }
    },
    methods: {
        addLocation() {
            console.log("adding lcoation")
            this.addLocationEnabled = true
            console.log("enabled", this.addLocationEnabled)
        },
        getExistingLocations() {
            const featuresApi = {};
            [
                { name: "n 1", lat: 1, lon: 2 },
                { name: "n 2", lat: 3, lon: 4 },
                { name: "a", lat: 1, lon: 21 },
                { name: "b 2", lat: 3, lon: 25 },
                { name: "d 1", lat: 7, lon: 11 },
                { name: "f 2", lat: 5, lon: 5 },
                { name: "g 1", lat: 6, lon: 3 },
                { name: "w 2", lat: 12, lon: 4 },
                { name: "d 1", lat: 63, lon: 3 },
                { name: "a 2", lat: 1, lon: 25 }


            ].forEach(i => {
                featuresApi[i.name] = { lat: i.lat, lon: i.lon }
            })
            return featuresApi;
        },
        drawLocations(map, featuresApi) {
            let features = []

            for (const [key, value] of Object.entries(featuresApi)) {

                let f = new Feature({
                    geometry: new Point(fromLonLat([value.lat, value.lon])),
                });


                // f.setStyle(
                //     new Style({
                //         image: new Icon({
                //             src: 'baseline_place_black_24dp.png',
                //             // src: 'marker-blue.png',
                //             scale: 1,

                //         }),
                //     })
                // );


                f.setStyle(
                    new Style({
                        image: new Icon({
                            // color: 'rgba(255, 0, 0, .5)',
                            // crossOrigin: 'anonymous',
                            src: marker2,
                            // src: './baseline_place_black_24dp.png',
                            // src: "marker-blue.png",
                            // img: 
                            // src: 'marker-blue.png',
                            scale: 0.2,

                        }),
                    })
                );

                features.push(f)

            }



            const vectorSource = new VectorSource({
                features: features,
            });

            const vectorLayer = new VectorLayer({
                source: vectorSource,
            });

            map.addLayer(vectorLayer)
        },
        addLocationPoint() {
            const london = new Feature({
                geometry: new Point(fromLonLat([-0.12755, 51.507222])),
            });

            london.setStyle(
                new Style({
                    image: new Icon({
                        color: 'rgba(255, 0, 0, .5)',
                        crossOrigin: 'anonymous',
                        src: 'marker-blue.png',
                        scale: 1,
                    }),
                })
            );
        },
        zoomSetupButtons(map) {

            document.getElementById('zoom-out').onclick = function () {
                const view = map.getView();
                const zoom = view.getZoom();
                view.setZoom(zoom - 1);
            };

            document.getElementById('zoom-in').onclick = function () {
                const view = map.getView();
                const zoom = view.getZoom();
                view.setZoom(zoom + 1);
            };
        },
        activatePopup(map,) {

            const popup = new Overlay({
                element: document.getElementById('popup'),
            });
            map.addOverlay(popup);


            map.on('click', (evt) => {

                if (this.addLocationEnabled) {
                    const element = popup.getElement();
                    const coordinate = evt.coordinate;
                    const hdms = toStringHDMS(toLonLat(coordinate));

                    $(element).popover('dispose');
                    popup.setPosition(coordinate);
                    $(element).popover({
                        container: element,
                        placement: 'top',
                        animation: false,
                        html: true,
                        content: '<p>Selected:</p><code>' + hdms + '</code>',
                    });
                    $(element).popover('show');

                    console.log("clicked", hdms, coordinate)
                    console.log(toLonLat(coordinate))
                    document.querySelector("#lat_tmp").innerHTML = coordinate[0]
                    document.querySelector("#lon_tmp").innerHTML = coordinate[1]

                } else {
                    console.log("not enabled")
                }

            });

        },
        initMap() {
            return new Map({
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
        }
    },



    mounted() {
        console.log("moutned")

        const map = this.initMap();

        // ----------------------------------------------------------------------------------------------
        this.activatePopup(map)

        // ----------------------------------------------------------------------------------------------

        const featuresApi = this.getExistingLocations();

        this.drawLocations(map, featuresApi);

        // ----------------------------------------------------------------------------------------------
        this.zoomSetupButtons(map)

    }
}
</script>

<style>
#map:focus {
    outline: #4A74A8 solid 0.15em;
}
</style>