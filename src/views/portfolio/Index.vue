<template>
  <div class="container mt-2">
    <div class="row">
      <div class="col">
        <portfolio-list />
      </div>
      <div class="col">
        <div class="row">
          <BaseChart></BaseChart>
        </div>
        <div class="row">
          <!-- <BaseChart></BaseChart> -->
        </div>
      </div>
      <!-- <div class="row"> -->
      <!-- <div class="col">
          <BaseChart></BaseChart>
        </div> -->
      <!-- </div> -->
    </div>
  </div>
</template>


<script>
import PortfolioList from "../../components/BasePortfolioList.vue";
import BaseChart from "@/components/BaseChart.vue";

export default {
  name: "PortfolioIndex",
  data() {
    return {};
  },
  components: {
    "portfolio-list": PortfolioList,
    BaseChart,
  },
};
</script> 
