<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col">
        <br />

        <div class="row">
          <AddContent></AddContent>
        </div>

        <div class="row">
          <TheDialogAddLocation></TheDialogAddLocation>
        </div>
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
import AddContent from "@/components/AddContent.vue";
import TheDialogAddLocation from "@/components/TheDialogAddLocation.vue";

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
    bindPopupToMap(map) {
      map.addOverlay(this.$refs.mappopup.getOverlay());
      map.on("singleclick", this.$refs.mappopup.clickEvent);
    },
  },
  async mounted() {
    let map = this.$refs.map.map;
    this.bindPopupToMap(map);
  },
  components: {
    MapPopup,
    MapComponent,
    AddContent,
    TheDialogAddLocation,
  },
};
</script> 
