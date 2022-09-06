<template>

    <div class="container-fluid">
        <div class="row">
            <div class="col-sm">
                <div class="row">
                    red - your
                    <br>
                    yellow - other
                    <LocationSelector>

                    </LocationSelector>
                    <hr>
                    mouse is pointing at this country:
                    <div id="info">&nbsp;</div>
                    <hr>
                    <!-- todo  -->
                    <!-- <UserCoordinates @userCoordinates="drawUserLocation" :canSend="this.canSend"
                        ref="userCoordinatesManager">
                    </UserCoordinates> -->
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


                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24" width="24px"
                        fill="#FF0000">
                        <path d="M0 0h24v24H0z" fill="none" />
                        <path fill="#FF0000"
                            d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z" />
                    </svg>

                    <div>

                        portfolio
                        <!-- <select @change="onChange($event)">
                            <option v-for="p in Object.keys(portfolios)" :key="p">{{ p }}</option>

                        </select>
                        <hr> -->


                    </div>

                    <div>
                        <div id='example-3'>
                            <div v-for="p in Object.keys(portfolios)" :key="p">
                                <!-- {{ p }} -->
                                <input type="checkbox" :id="p" :value="p" v-model="checkedNames">
                                <label :for="p">{{ p }}</label>
                                <hr>

                            </div>
                            <!-- <input type="checkbox" id="jack" value="Jack" v-model="checkedNames">
                            <label for="jack">Jack</label>
                            <hr>
                            <input type="checkbox" id="john" value="John" v-model="checkedNames">
                            <label for="john">John</label>
                            <input type="checkbox" id="mike" value="Mike" v-model="checkedNames">
                            <label for="mike">Mike</label>
                            <br> -->
                            <span>Checked names: {{ checkedNames }}</span>
                            <hr>
                            <button @click="onChange">click to filter</button>
                        </div>
                    </div>

                </div>
            </div>
            <div class="col-sm">
                <div class="row">
                    <div id="map" class="map" tabindex="0" style="width: 90%; height: 90%; 
                        position:fixed; 
                            border: 1px solid #ccc;     ">
                    </div>

                    <MapPopup ref="mappopup"></MapPopup>

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
import { toStringHDMS } from 'ol/coordinate';
import { fromLonLat, toLonLat } from 'ol/proj';
import Point from 'ol/geom/Point';
import Feature from 'ol/Feature';
import { Icon, Style } from 'ol/style';
import VectorSource from 'ol/source/Vector';
import { Vector as VectorLayer } from 'ol/layer';
import GeoJSON from 'ol/format/GeoJSON';
import { Stroke } from 'ol/style';

import LocationSelector from '../../components/map/LocationSelector.vue'; //Optional default CSS
import userMarker from "/public/assets/markers/geolocation_marker.png"
import countriesjson from "/public/assets/layers/countries.json";
import { apiCalls } from '../../scripts/api';
import { apiLocations } from '../../scripts/api_locations';
// import UserCoordinates from "../../components/map/UserCoordinates.vue";
import MapPopup from "../../components/map/MapPopup.vue";

export default {
    components: {
        LocationSelector,
        //  UserCoordinates, 
        MapPopup
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
            countriesLayer: undefined,
            portfolios: {},
            checkedNames: []
        }
    },
    methods: {
        onChange() {
            console.log("clicked", this.checkedNames)



            for (const [key, value] of Object.entries(this.portfolios)) {
                console.log(key, value);
                value["visible"] = false;
                // console.log(value["visible"])
                this.map.removeLayer(value["vectorLayer"]);

            }
            this.checkedNames.forEach(i => {
                console.log("portf", i)
                this.portfolios[i]["visible"] = true
            })
            for (const [key, value] of Object.entries(this.portfolios)) {
                console.log(key, value);
                // value["visible"] = false;
                console.log(value["visible"])
                if (value["visible"]) {
                    this.map.addLayer(value["vectorLayer"]);
                } else {
                    console.log("lele")
                }
            }

            // let portfolioName = event.target.value;
            // console.log("on change", portfolioName)

            // let t = this.portfolios[portfolioName]
            // console.log(t);

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
                        src: userMarker,
                        scale: 0.6,
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
        drawLocations(featuresApi, marker, portfolioName) {

            var style = new Style({
                image: new Icon({
                    opacity: 1,
                    src: 'data:image/svg+xml;utf8,' + marker,
                    scale: 0.9
                })
            });

            let features = []

            for (const [key, value] of Object.entries(featuresApi)) {
                console.log(key);

                let f = new Feature({
                    geometry: new Point(fromLonLat([value.lat, value.lon])),
                });

                f.setStyle(style);

                features.push(f)

            }

            const vectorLayer = new VectorLayer({
                source: new VectorSource({
                    features: features,
                })
            });

            this.portfolios[portfolioName] = {
                "vectorLayer": vectorLayer,
                "visible": true
            }
            this.map.addLayer(vectorLayer)
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
        activatePopup() {

            this.map.addOverlay(this.$refs.mappopup.getOverlay())

            /**
             * Add a click handler to the map to render the popup.
             */
            this.map.on('singleclick', (evt) => {

                if (this.addLocationEnabled) {
                    const coordinate = evt.coordinate;
                    const hdms = toStringHDMS(toLonLat(coordinate));

                    console.log("log coord", hdms)
                    console.log("set postiion,", coordinate)
                    this.$refs.mappopup.setText(hdms);
                    this.$refs.mappopup.setPosition(coordinate);

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

            this.map = new Map({
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
        },
        prepareLocationsForDrawing(locations) {


            // var obj = { 'a': 1, 'b': 2, 'c': 3 };

            // let newObj = Object.fromEntries(Object.entries(obj).map(([k, v]) => [k, v * v]));

            // console.log(newObj)




            const featuresApi = {};
            let c = 0;
            // console.log("")
            locations.forEach(i => {
                featuresApi[c] = { lat: i.latitude, lon: i.longitude }
                c++;
            })

            return featuresApi;

        }
    },

    async mounted() {

        let marker = '<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24" width="24px" fill="#FF0000"><path d="M0 0h24v24H0z" fill="none"/><path fill="#FF0000" d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>'
        console.log("marker", marker);

        this.initMap();

        this.activatePopup()

        // todo enable
        // this.$refs.userCoordinatesManager.enableCoordinates();

        this.zoomSetupButtons(this.map)

        this.createCountriesLayer()

        this.filterByCountry();

        function createMarker(hexColour) {

            return `<svg width="120" height="120" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <path d="M0 0h24v24H0z" fill="none"/>
                        <path fill="%23${hexColour}" d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z" />
                    </svg>`

        }

        let r = await apiCalls.getPortoflios();
        if (r["auth"]["status"]) {
            let pl = r["payload"]["portfolios"];

            // this.portfolios = Object.keys(pl);

            for (const [key, value] of Object.entries(pl)) {
                let hexColour = value["hex"];
                let r = (await apiLocations.getLocationsFilterUsername(key)).payload.content
                let marker = createMarker(hexColour);


                this.drawLocations(
                    r,
                    marker,
                    key
                );
            }

        }

    }
}
</script>

<style>
#map:focus {
    outline: #4A74A8 solid 0.15em;
}
</style>