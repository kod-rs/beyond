<template>
  <!-- <div class="container-fluid"> -->
  <!-- <div class="row"> -->
  <!-- <div class="col"> -->

  <div class="row">
    <CChartLine :data="temperatures" />
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
      temperatures: {
        // labels: [],
        labels: ["timestamp", "a", "b", "c", "d", "e", "f", "g"],
        datasets: [
          {
            label: "temperature",
            // backgroundColor: "rgb(0,216,255,0.9)",
            data: [39, 80, 40, 35, 40, 20, 45],
          },
        ],
      },
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
      if (!this.location) {
        console.log("undefined");
        return;
      }

      console.log("get temp");

      let r = await apiTemperature.getAllTemperature(
        this.location.portfolio,
        this.location.section,
        this.location.type
      );

      if (r["payload"]["status"]) {
        let values = r["payload"]["result"];
        if (!values) {
          console.log("no values for this location");
          return;
        }

        console.log("have values");

        console.table(values);

        // let timestamps = [];
        // let values =

        //         for (const [key, value] of Object.entries(object)) {
        //     console.log(key, value);
        // }

        console.log();

        this.temperatures = {
          // labels: [],
          labels: ["months", ...Object.keys(values)],
          datasets: [
            {
              label: "Data Two",
              data: Object.values(values),
            },
          ],
        };

        // console.log(r["payload"]["result"]);
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
