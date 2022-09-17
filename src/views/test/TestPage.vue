<template>
  <button @click="openLeft">click</button>

  <TheMapFullSize></TheMapFullSize>

  <w-drawer v-model="openDrawer" left>
    <!-- <w-button
      @click="openDrawer = false"
      sm
      outline
      round
      absolute
      icon="wi-cross"
    >
    </w-button> -->
  </w-drawer>
</template>

<script>
import TheMapFullSize from "@/components/TheMapFullSize.vue";

export default {
  components: {
    TheMapFullSize,
  },
  data() {
    return {
      openDrawer: false,
    };
  },
  methods: {
    openLeft() {
      console.log("left");
      this.openDrawer = !this.openDrawer;
    },
  },
};
</script>

<style>
</style>