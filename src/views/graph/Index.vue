<template>
  <!-- <div class="container-fluid"> -->
  <div class="row">
    <div class="col">
      <BaseChart :portfolio="portfolio" :p="chartOptions"></BaseChart>
    </div>
    <!-- <div class="col">
      <BaseChart></BaseChart>
    </div> -->
  </div>
</template>
  
  <script>
import BaseChart from "@/components/BaseChart.vue";
// import { apiTemperature } from "@/scripts/api/temperature";
// import VueApexCharts from "vue3-apexcharts";
// import BaseChart from "@/components/BaseChart.vue";
export default {
  name: "GraphIndex",
  data() {
    return {
      chartOptions: {
        chart: {
          id: "vuechart-example",
        },
        xaxis: {
          categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998],
        },
      },

      portfolio: undefined,
      section: undefined,
      type: undefined,
      // portfolio_1: "portfolio_1",
      // section_1: "section_1",
      // type_1: "type_1",
    };
  },
  mounted() {
    console.log("moutned p");
    this.portfolio = this.$route.params.portfolio;
    this.section = this.$route.params.section;
    this.type = this.$route.params.type;
    console.log(this.portfolio, this.section, this.type);
  },
  components: { BaseChart },
};
</script>
  
