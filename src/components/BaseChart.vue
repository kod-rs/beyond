<template>
  <!-- <div class="container-fluid"> -->
  <!-- <div class="row"> -->
  <!-- <div class="col"> -->

  <div class="row">
    <CChartLine :data="defaultData" />
  </div>

  <div class="row">
    <CChartLine :data="defaultData" />
  </div>

  <div class="row">
    <button @click="refreshCharts">refresh</button>
  </div>

  <!-- left -->
  <!-- </div> -->
  <!-- <div class="col"> -->
  <!-- <CChartLine :data="defaultData" /> -->

  <!-- right -->
  <!-- </div>
    </div>
  </div> -->
</template>

<script>
import { apiTemperature } from "@/scripts/api/temperature";

import { CChartLine } from "@coreui/vue-chartjs";
export default {
  data() {
    return {
      location: undefined,
    };
  },

  components: { CChartLine },
  computed: {
    defaultData() {
      return {
        // labels: [],
        labels: ["months", "a", "b", "c", "d", "e", "f", "g"],
        datasets: [
          {
            label: "Data One",
            backgroundColor: "rgb(228,102,81,0.9)",
            data: [30, 39, 10, 50, 30, 70, 35],
          },
          {
            label: "Data Two",
            backgroundColor: "rgb(0,216,255,0.9)",
            data: [39, 80, 40, 35, 40, 20, 45],
          },
        ],
      };
    },
  },
  mounted() {
    console.log("mounted");
    // this.location = this.$store.state.location;
    // console.log(this.location);
  },

  methods: {
    async refreshCharts() {
      console.log("refresh");

      await this.fetchTemperature();
    },

    async fetchTemperature() {
      this.location = this.$store.state.location;
      console.log(this.location);

      console.log("get temp");

      let r = await apiTemperature.getAllTemperature(
        this.location.portfolio,
        this.location.section,
        this.location.type
      );

      if (r["payload"]["status"]) {
        console.log(r["payload"]["result"]);
        // this.locations[portfolioPayload.oldName] = Object.values(
        //   r["payload"]["content"]
        // ).map((item) => {
        //   return this.castLocation(item.section, item.type, item.lat, item.lon);
        // });
      } else {
        this.showMessage(false, "", "Error fetching data, contact admin");
      }
    },
  },
};
</script>
