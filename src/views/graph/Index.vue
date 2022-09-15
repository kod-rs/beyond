<template>
  <!-- <div class="container-fluid"> -->
  <!-- <div class="row"> -->
  <!-- <div class="col"> -->

  <div class="row">
    <div class="col">
      <apexchart
        width="500"
        type="area"
        :options="chartOptions"
        :series="series"
      ></apexchart>
      <div>
        <button @click="updateChart">Update!</button>
      </div>
    </div>
    <div class="col">
      <apexchart
        width="500"
        type="area"
        :options="chartOptions"
        :series="series"
      ></apexchart>
      <div>
        <button @click="updateChart">Update!</button>
      </div>
    </div>
  </div>

  <div class="row"></div>
</template>
  
  <script>
import { apiTemperature } from "@/scripts/api/temperature";
import VueApexCharts from "vue3-apexcharts";
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
      series: [
        {
          name: "series-1",
          data: [30, 40, 35, 50, 49, 60, 70, 91],
        },
      ],

      portfolio: "",
      section: "",
      type: "",

      location: undefined,
      // temperatures: undefined,
    };
  },
  components: { apexchart: VueApexCharts },
  computed: {
    defaultData() {
      return {
        // labels: [],
        labels: ["months", "a", "b", "c", "d", "e", "f", "g"],
        datasets: [
          {
            label: "Data One",
            backgroundColor: "rgb(228,102,81,0.9)",
            data: [10, 10, 10, 50, 30, 70, 35],
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
  async mounted() {
    console.log("mounted");
    console.log(this.$route.params);
    this.portfolio = this.$route.params.portfolio;
    this.section = this.$route.params.section;
    this.type = this.$route.params.type;

    console.log(this.portfolio, this.section, this.type);
    await this.fetchTemperature();
    // this.temperatures["labels"] = ["fff", "40", "40", "40"];
    // console.log(this.temperatures);
    // = {
    //   // labels: [],
    //   labels: ["months", "a", "b", "c", "d", "e", "f", "g"],
    //   datasets: [
    //     {
    //       label: "temp",
    //       backgroundColor: "rgb(0,216,255,0.9)",
    //       data: [40, 40, 40, 40, 40, 20, 45],
    //     },
    //   ],
    // };
  },

  methods: {
    updateChart() {
      console.log("updating");
      const max = 90;
      const min = 20;
      const newData = this.series[0].data.map(() => {
        return Math.floor(Math.random() * (max - min + 1)) + min;
      });

      // const colors = ["#008FFB", "#00E396", "#FEB019", "#FF4560", "#775DD0"];

      // // Make sure to update the whole options config and not just a single property to allow the Vue watch catch the change.
      // this.chartOptions = {
      //   colors: [colors[Math.floor(Math.random() * colors.length)]],
      // };

      // In the same way, update the series option
      this.series = [
        {
          data: newData,
        },
      ];
    },
    async refreshCharts() {
      console.log("refresh");

      await this.fetchTemperature();
    },

    async fetchTemperature() {
      // this.location = this.$store.state.location;

      // console.log(this.location);
      // if (!this.location) {
      //   console.log("undefined");
      //   return;
      // }

      console.log("get temp");

      let r = await apiTemperature.getAllTemperature(
        this.portfolio,
        this.section,
        this.type
      );

      if (r["payload"]["status"]) {
        let values = r["payload"]["result"];
        if (!values) {
          console.log("no values for this location");
          return;
        }

        console.log("have values");

        console.table(values);

        // this.chartOptions = {
        //   colors: [colors[Math.floor(Math.random() * colors.length)]],
        // };

        this.chartOptions = {
          chart: {
            id: "temperature",
          },
          xaxis: {
            categories: Object.keys(values),
          },
        };

        // In the same way, update the series option
        this.series = [
          {
            data: Object.values(values),
          },
        ];

        // let timestamps = [];
        // let values =

        //         for (const [key, value] of Object.entries(object)) {
        //     console.log(key, value);
        // }

        // console.log();

        // this.temperatures = {
        //   // labels: [],
        //   labels: ["months", ...Object.keys(values)],
        //   datasets: [
        //     {
        //       label: "Data Two",
        //       data: Object.values(values),
        //     },
        //   ],
        // };
      } else {
        console.log("error fetching");
        // this.showMessage(false, "", "Error fetching data, contact admin");
      }
    },
  },
};
</script>
  