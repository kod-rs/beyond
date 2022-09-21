<template>
  <TopNavigationBar></TopNavigationBar>
  <div class="moveDown">
    <w-app>
      <div>
        <div class="nonscrollable">
          <slot> </slot>
        </div>
      </div>
    </w-app>
  </div>
</template>

<script>
import TopNavigationBar from "./TopNavigationBar.vue";
export default {
  data() {
    return {};
  },
  components: { TopNavigationBar },
};
</script>

<style>
.moveDown {
  margin: 0;
  height: 100%;
  /* overflow: hidden; */
}

/* html,
body {
  margin: 0;
  height: 100%;
  overflow: hidden; 
} */

/* Show it is fixed to the top */
.moveDown {
  min-height: 75rem;
  /* padding-top: 4.5rem; */
  padding-top: 3.5rem;
}
</style>