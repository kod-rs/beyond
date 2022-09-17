<template>
  <div id="mapelement"></div>
</template>

<script>
import Map from "ol/Map";
import OSM from "ol/source/OSM";
import TileLayer from "ol/layer/Tile";
import View from "ol/View";
export default {
  data() {
    return {
      map: undefined,
    };
  },
  methods: {},
  mounted() {
    this.map = new Map({
      layers: [
        new TileLayer({
          source: new OSM(),
        }),
      ],
      target: "mapelement",
      view: new View({
        center: [0, 0],
        zoom: 2,
      }),
    });

    this.$store.dispatch("setMap", this.map);

    // setTimeout(() => {
    //   this.map.updateSize();
    // });
  },
};
</script>


<style>
#mapelement {
  width: 100%;
  height: 100%;
  /* border: 5px solid Tomato; */
  position: absolute;
}

/* #map:focus {
    outline: #4A74A8 solid 0.15em;
} */
</style>