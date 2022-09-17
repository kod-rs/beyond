<template>
  <button @click="openLeft">click</button>

  <TheMapFullSize ref="map"></TheMapFullSize>
  <TheAddLocationPopup ref="mappopup"></TheAddLocationPopup>
  <w-drawer v-model="openDrawer" left>
    <hr />
    <br />
    <br />
    <br />
    <br />
    <br />
  </w-drawer>
</template>

<script>
import TheMapFullSize from "@/components/TheMapFullSize.vue";
import TheAddLocationPopup from "../../components/TheAddLocationPopup.vue";

export default {
  components: {
    TheMapFullSize,

    TheAddLocationPopup,
  },
  data() {
    return {
      openDrawer: false,
    };
  },
  async mounted() {
    let map = this.$refs.map.map;
    this.bindPopupToMap(map);
  },
  methods: {
    bindPopupToMap(map) {
      map.addOverlay(this.$refs.mappopup.getOverlay());
      map.on("singleclick", this.$refs.mappopup.clickEvent);
    },
    closePopup() {
      this.$refs.mappopup.closePopup();
    },
    openLeft() {
      console.log("left");
      this.openDrawer = !this.openDrawer;
    },
  },
};
</script>

<style>
w-drawer {
  margin: 0;
  height: 100%;
  overflow: hidden;
  min-height: 75rem;
  /* padding-top: 4.5rem; */
  padding-top: 3.5rem;
}
</style>