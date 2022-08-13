<template>

    <div class="container-fluid">

        test routes:
        <router-link :to="{ name: 'addlocation' }">Create</router-link> |
        <router-link :to="{ name: 'viewlocation' }">View</router-link> |
        <router-link to="/logout">Logout</router-link>


        <div class="row">
            <div class="col-sm">
                <div class="row">
                    enter location
                    <InputAutocomplete :ph="fromTimeWindow" ref="inputautocompletefield" :items="getLocations()">

                        <!-- :items="['Apple', 'Banana', 'Orange', 'Mango', 'Pear', 'Peach', 'Grape', 'Tangerine', 'Pineapple']">
                     -->
                        <!-- getLocations -->
                    </InputAutocomplete>

                    <div class="">

                    </div>

                    country:
                    <div id="info">&nbsp;</div>

                    <UserCoordinates @userCoordinates="drawUserLocation" :canSend="this.canSend"
                        ref="userCoordinatesManager">
                    </UserCoordinates>
                    <button>
                        <router-link class="dropdown-item" to="/logout">Logout</router-link>
                    </button>
                    <button @click="allowLocationAdding()">add location, when user wants to add new location to
                        map, allow location adding</button>
                    <div>
                        lon: <div id="lon_tmp">1</div>
                    </div>
                    <div>
                        lat: <div id="lat_tmp">2</div>
                    </div>
                    <button>position map on user location</button>
                    <button id="zoom-out">Zoom out</button>
                    <button id="zoom-in">Zoom in</button>
                </div>
            </div>
            <div class="col-sm">
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
            <div class="col-sm">
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
import GeoJSON from 'ol/format/GeoJSON';
import { Stroke } from 'ol/style';

import InputAutocomplete from '../../components/form/InputAutocomplete.vue'; //Optional default CSS


import marker2 from "./../../assets/markers/baseline_place_black_24dp.png"
import countriesjson from "./../../assets/layers/countries.json";
import countryNameJson from "./../../assets/layers/country_names.json";
import axios from 'axios';
import { resolve } from 'path';


export default {
    components: {
        InputAutocomplete
    },
    data() {
        return {
            addLocationEnabled: false,
            userLat: undefined,
            userLon: undefined,
            map: undefined,
            userLocationLayer: undefined,
            canSend: false,
            view: undefined,
            vectorSource: undefined,
            countriesLayer: undefined,

        }
    },
    methods: {
        getLocations() {
            console.log("getting locations")

            // return axios.get(countryNameJson)
            //     .then(r => {
            //         r = r.data
            //         // console.table(r)
            //         // console.log("alb")
            //         // console.log(r["Albania"])
            //         // // c = r.map(i => i)
            //         let c = Object.keys(r)
            //         console.log(c)
            //         // resolve(c)
            //         return c
            //     })

            return ['Apple', 'Banana', 'Orange', 'Mango', 'Pear', 'Peach', 'Grape', 'Tangerine', 'Pineapple']
        },

        findLocation() {
            console.log("entered sth new")
        },

        drawUserLocation(lat, lon) {

            console.log("draw user location", lat, lon)

            if (this.userLocationLayer) {
                this.map.removeLayer(this.userLocationLayer)
            }

            this.userLat = this.$store.state.latitude;
            this.userLon = this.$store.state.longitude;

            let f = new Feature({
                geometry: new Point(fromLonLat([lon, lat])),
            });

            f.setStyle(
                new Style({
                    image: new Icon({

                        src: marker2,

                        scale: 0.5,

                    }),
                })
            );

            const vectorSource = new VectorSource({
                features: [f],
            });

            const vectorLayer = new VectorLayer({
                source: vectorSource,
            });

            this.map.addLayer(vectorLayer);

            this.userLocationLayer = vectorLayer

            console.log(this.map.getView().getCenter())

            // center
            const feature = vectorSource.getFeatures()[0];
            const point = feature.getGeometry();
            const size = this.map.getSize();
            this.view.centerOn(point.getCoordinates(), size, [500, 500]);

            // zoom
            this.view.fit(point, { padding: [170, 50, 30, 150], minResolution: 50 });

        },
        allowLocationAdding() {
            this.addLocationEnabled = true
            console.log("enabled", this.addLocationEnabled)
        },
        getExistingLocations() {

            // todo extract as api
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

                let icon = new Icon({

                    src: marker2,

                    scale: 0.2,

                })


                f.setStyle(
                    new Style({
                        image: icon
                    })
                );

                features.push(f)


            }

            this.vectorSource = new VectorSource({
                features: features,
            });

            const vectorLayer = new VectorLayer({
                source: this.vectorSource,
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
            this.view = new View({
                center: [0, 0],
                zoom: 2,
            });

            return new Map({
                layers: [
                    new TileLayer({
                        source: new OSM(),
                    }),

                ],
                target: 'map',
                view: this.view,
            });
        },
        createCountriesLayer() {

            this.countriesLayer = new VectorLayer({
                source: new VectorSource({
                    format: new GeoJSON(),
                    url: countriesjson,
                }),
            })

            this.map.addLayer(
                this.countriesLayer
            )
        },
        filterByCountry() {

            const highlightStyle = new Style({
                stroke: new Stroke({
                    color: 'rgba(255, 255, 255, 0.7)',
                    width: 2,
                }),
            });

            const featureOverlay = new VectorLayer({
                source: new VectorSource(),
                map: this.map,
                style: highlightStyle,
            });

            let highlight;
            const displayFeatureInfo = (pixel) => {

                this.countriesLayer.getFeatures(pixel).then(function (features) {
                    const feature = features.length ? features[0] : undefined;

                    const info = document.getElementById('info');
                    if (features.length) {
                        info.innerHTML = feature.get('name');
                        console.log("todo: get from db for location", feature.get('name'));
                    } else {
                        info.innerHTML = '&nbsp;';
                    }



                    if (feature !== highlight) {
                        if (highlight) {
                            featureOverlay.getSource().removeFeature(highlight);
                        }
                        if (feature) {
                            featureOverlay.getSource().addFeature(feature);
                        }
                        highlight = feature;
                    }
                });
            };

            this.map.on('pointermove', (evt) => {
                if (evt.dragging) {
                    return;
                }
                const pixel = this.map.getEventPixel(evt.originalEvent);
                displayFeatureInfo(pixel);
            });

            this.map.on('click', (evt) => {
                displayFeatureInfo(evt.pixel);
            });
        }
    },

    mounted() {
        console.log("moutned")

        this.$refs.inputautocompletefield.setPlaceholder("type location");

        console.table(countriesjson)
        console.table(typeof (countriesjson))

        const map = this.initMap();
        this.map = map;

        this.$refs.userCoordinatesManager.enableCoordinates();

        // ----------------------------------------------------------------------------------------------
        this.activatePopup(this.map)

        // ----------------------------------------------------------------------------------------------

        const featuresApi = this.getExistingLocations();

        this.drawLocations(this.map, featuresApi);

        // ----------------------------------------------------------------------------------------------
        this.zoomSetupButtons(this.map)

        this.createCountriesLayer()

        this.filterByCountry()

    }
}
</script>

<style>
#map:focus {
    outline: #4A74A8 solid 0.15em;
}
</style>