<template>
  <div class="container mt-2">
    <div class="row">
      <!-- <div class="col"> -->
      <BasePortfolioList></BasePortfolioList>
      <!-- </div> -->
    </div>

    <!-- <div class="row">
      <button>Optimize selected</button>
    </div> -->
  </div>
</template>


<script>
import BasePortfolioList from "@/components/BasePortfolioList.vue";

export default {
  name: "PortfolioIndex",
  data() {
    return {};
  },
  methods: {
    getSelected() {
      return { l1: "d1", l2: "d2" };
    },
  },
  components: {
    BasePortfolioList,
  },
};
</script> 
