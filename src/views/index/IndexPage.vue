<template>
  <div>
    <div class="container-fluid">
      <div class="row">
        <div class="col">
          <div class="row">
            <div>
              portfolio
              <div id="example-3">
                <div v-for="p in Object.keys(portfolios)" :key="p">
                  <input
                    type="checkbox"
                    :id="p"
                    :value="p"
                    v-model="checkedNames"
                  />
                  <label :for="p">{{ p }}</label>
                  <hr />
                </div>
                <span>Checked portfolios: {{ checkedNames }}</span>
                <hr />
                <button @click="onChange">click to filter</button>
              </div>
            </div>
          </div>
        </div>
        <div class="col">
          <MapComponent></MapComponent>
          <MapPopup ref="mappopup"></MapPopup>
        </div>
      </div>
    </div>

    <div>
      <UserCoordinates
        @userCoordinates="drawUserLocation"
        :canSend="this.canSend"
        ref="userCoordinatesManager"
      >
      </UserCoordinates>
    </div>
  </div>
</template>



<script>
import { toStringHDMS } from "ol/coordinate";
import { fromLonLat, toLonLat } from "ol/proj";
import Point from "ol/geom/Point";
import Feature from "ol/Feature";
import { Icon, Style } from "ol/style";
import VectorSource from "ol/source/Vector";
import { Vector as VectorLayer } from "ol/layer";

import userMarker from "/public/assets/markers/geolocation_marker.png";

import { apiLocation } from "../../scripts/api/location";
import UserCoordinates from "../../components/map/UserCoordinates.vue";
import MapPopup from "../../components/map/MapPopup.vue";
import MapComponent from "@/components/map/MapComponent.vue";
import { apiPortfolio } from "@/scripts/api/portfolio";
// import FilterLocations from './FilterLocations.vue';

export default {
  components: {
    UserCoordinates,
    MapPopup,
    MapComponent,
    // FilterLocations
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
      checkedNames: [],
    };
  },
  methods: {
    onChange() {
      console.log("clicked", this.checkedNames);

      for (const [key, value] of Object.entries(this.portfolios)) {
        console.log(key, value);
        value["visible"] = false;
        this.map.removeLayer(value["vectorLayer"]);
      }
      this.checkedNames.forEach((i) => {
        console.log("portf", i);
        this.portfolios[i]["visible"] = true;
      });
      for (const [key, value] of Object.entries(this.portfolios)) {
        console.log(key, value);
        // value["visible"] = false;
        console.log(value["visible"]);
        if (value["visible"]) {
          this.map.addLayer(value["vectorLayer"]);
        } else {
          console.log("lele");
        }
      }
    },
    drawUserLocation(lat, lon) {
      this.userLat = this.$store.state.latitude;
      this.userLon = this.$store.state.longitude;

      const point = new Point(fromLonLat([lon, lat]));

      let feature = new Feature({
        geometry: point,
      });

      feature.setStyle(
        new Style({
          image: new Icon({
            src: userMarker,
            scale: 0.6,
          }),
        })
      );

      if (this.userLocationLayer) {
        this.map.removeLayer(this.userLocationLayer);
      }

      this.userLocationLayer = new VectorLayer({
        source: new VectorSource({
          features: [feature],
        }),
      });

      this.map.addLayer(this.userLocationLayer);

      // this.view.centerOn(
      //     point.getCoordinates(),
      //     this.map.getSize(),
      //     [500, 500]
      // );

      // zoom
      // this.view.fit(point, { padding: [170, 50, 30, 150], minResolution: 50 });
    },
    allowLocationAdding() {
      this.addLocationEnabled = true;
      console.log("enabled", this.addLocationEnabled);
    },
    createMarker(hexColour) {
      return `
                <svg viewBox="5 2 14 20" width="50" height="50" version="1.1" xmlns="http://www.w3.org/2000/svg">
                <path d="M0 0h24v24H0z" fill="none"/>
                <path fill="%23${hexColour}" d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z" />
                </svg>
                `;
    },
    drawLocations(featuresApi, marker, portfolioName) {
      let style = new Style({
        image: new Icon({
          src: "data:image/svg+xml;utf8," + marker,
          scale: 0.4,
        }),
      });

      let features = [];

      for (const [key, value] of Object.entries(featuresApi)) {
        console.log(key);

        let f = new Feature({
          geometry: new Point(fromLonLat([value.lon, value.lat])),
        });

        f.setStyle(style);

        features.push(f);
      }

      const vectorLayer = new VectorLayer({
        source: new VectorSource({
          features: features,
        }),
      });
      this.portfolios[portfolioName] = {
        vectorLayer: vectorLayer,
      };
      this.map.addLayer(vectorLayer);
    },
    activatePopup() {
      this.map.addOverlay(this.$refs.mappopup.getOverlay());

      /**
       * Add a click handler to the map to render the popup.
       */
      this.map.on("singleclick", (evt) => {
        if (this.addLocationEnabled) {
          const coordinate = evt.coordinate;
          const hdms = toStringHDMS(toLonLat(coordinate));

          // console.log("log coord", hdms)
          // console.log("set postiion,", coordinate)
          this.$refs.mappopup.setText(hdms);
          this.$refs.mappopup.setPosition(coordinate);

          document.querySelector("#lat_tmp").innerHTML = coordinate[0];
          document.querySelector("#lon_tmp").innerHTML = coordinate[1];
        } else {
          console.log("not enabled");
        }
      });
    },
    async fetchLocations() {
      let r = await apiPortfolio.getPortoflios();
      if (r["auth"]["status"]) {
        let pl = r["payload"]["portfolios"];

        for (const [key, value] of Object.entries(pl)) {
          let hexColour = value["colourHexEncoded"];

          let r = (await apiLocation.getAllLocationsInPortfolio(value.name))
            .payload.content;
          let marker = this.createMarker(hexColour);

          this.drawLocations(r, marker, key);
        }
      }
    },
  },

  async mounted() {
    this.map = this.$store.getters.map;

    this.activatePopup();

    // todo enable
    this.$refs.userCoordinatesManager.enableCoordinates();

    await this.fetchLocations();
  },
};
</script>
