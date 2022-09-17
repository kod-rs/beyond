<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col">
        <br />

        <TheLocationAddForm @closePopup="closePopup"></TheLocationAddForm>
      </div>

      <div class="col">
        <MapComponent ref="map"></MapComponent>
        <MapPopup ref="mappopup"></MapPopup>
      </div>
    </div>
  </div>
</template>

    


<script>
import MapPopup from "../../components/MapPopup.vue";
import MapComponent from "@/components/MapComponent.vue";
import TheLocationAddForm from "@/components/TheLocationAddForm.vue";

export default {
  data() {
    return {
      map: undefined,
    };
  },
  methods: {
    closePopup() {
      this.$refs.mappopup.closePopup();
    },
    initMapPopup() {
      /**
       * Add a click handler to the map to render the popup.
       */
      // this.map.on("singleclick", (evt) => {
      //   const coordinate = evt.coordinate;
      //   const hdms = toStringHDMS(toLonLat(coordinate));
      //   this.$refs.mappopup.setText(hdms);
      //   this.$refs.mappopup.setPosition(coordinate);
      //   this.$store.dispatch("setClickedLocation", {
      //     longitude: toLonLat(coordinate)[0],
      //     latitude: toLonLat(coordinate)[1],
      //   });
      // });
    },
  },
  async mounted() {
    this.map = this.$refs.map.map;

    this.map.addOverlay(this.$refs.mappopup.getOverlay());

    this.map.on("singleclick", this.$refs.mappopup.clickEvent);
  },
  components: {
    MapPopup,
    MapComponent,
    TheLocationAddForm,
  },
};
</script> 
