<template>
  <div>
    <br />

    {{ t }}

    <div class="row">
      <div class="col">Section</div>
      <div class="col">Type</div>
      <div class="col"></div>
      <div class="col"></div>
      <div class="col"></div>
      <div class="col"></div>
    </div>

    <div class="row" v-for="locationPayload in t" :key="locationPayload">
      <div class="col">
        <input
          class="form-check-input"
          type="checkbox"
          id="checkboxNoLabel"
          aria-label="..."
          v-model="locationPayload.isSelected"
        />
      </div>

      <div class="col">
        <input
          type="text"
          class="form-control"
          v-model="locationPayload.newSection"
          placeholder="Location section"
        />
      </div>

      <div class="col">
        <input
          type="text"
          class="form-control"
          v-model="locationPayload.newType"
          placeholder="Location type"
        />
      </div>

      <div class="col">
        <img
          @click="mapClicked(locationPayload)"
          src="assets/map/map.png"
          alt="img"
          class="img-fluid float-left"
          style="width: 50%; height: auto"
        />
      </div>

      <!-- <div class="col">
        <button
          class="btn btn-primary"
          @click="updateLocation(locationPayload)"
        >
          Update
        </button>
      </div> -->

      <div class="col">
        <button
          v-if="isChanged(locationPayload)"
          @click="updateLocation(locationPayload)"
          class="btn btn-primary"
        >
          Update
        </button>

        <button v-else class="btn btn-secondary" disabled>Update</button>
      </div>

      <!-- <div v-if="portfolioPayload.isInDb" class="col"> -->
      <!-- </div> -->

      <div class="col">
        <button
          class="btn btn-primary"
          @click="deleteLocation(locationPayload)"
        >
          Delete
        </button>
      </div>

      <!-- <div class="col">
        <button @click="testClick(locationPayload)">test</button>
      </div> -->

      <div class="col">
        <router-link
          :to="{
            name: `chart`,
            params: {
              portfolio: portfolio,
              section: locationPayload.oldSection,
              type: locationPayload.oldType,
            },
          }"
          target="_blank"
        >
          Show charts
        </router-link>
      </div>

      <hr />
      <br />
    </div>
    <!-- <button @click="getSelected">show selected</button> -->
  </div>
</template>

<script>
import { apiLocation } from "@/scripts/api/location";
import { apiTemperature } from "@/scripts/api/temperature";

export default {
  props: {
    t: Object,
    portfolio: String,
    // portfolioPayload: Object,
  },
  data() {
    return {
      selected: {},
    };
  },
  methods: {
    getSelected() {
      console.log("selected");
      // let se

      // todo rewrite as selected is dictionary, key = portfolio, value = list of section, type tuples
      this.selected = [];

      this.t.forEach((element) => {
        if (element.isSelected) {
          // todo what if names are updated for portfolio, section or type

          this.selected.push({
            portfolio: this.portfolio,
            section: this.oldSection,
            type: this.oldType,
          });
          console.log(this.portfolio, element.oldSection, element.oldType);
        }
      });

      console.table(this.selected);

      return this.selected;
    },

    updateSelected(locationPayload) {
      console.log("update selected", locationPayload);
      // this.selected.
    },

    async testClick(locationPayload) {
      let r = await apiTemperature.getAllTemperature(
        this.portfolio,
        // this.location.portfolio,
        locationPayload.oldSection,
        locationPayload.oldType
      );

      console.table(r["payload"]["result"]);

      // if (r["payload"]["status"]) {
      //       console.log(r["payload"]["result"]);
      //       // this.locations[portfolioPayload.oldName] = Object.values(
      //       //   r["payload"]["content"]
      //       // ).map((item) => {
      //       //   return this.castLocation(item.section, item.type, item.lat, item.lon);
      //       // });
      //     } else {
      //       this.showMessage(false, "", "Error fetching data, contact admin");
      //     }
    },

    selectLocation(locationPayload) {
      this.$store.commit("selectLocation", {
        type: locationPayload.oldType,
        section: locationPayload.oldSection,
        portfolio: this.portfolio,
      });
      // this.$store.selectLocation(locationPayload);
    },

    mapClicked(locationPayload) {
      console.log("map clicked", locationPayload);
    },
    setPortfolioName() {
      console.log("todo parent portfolio name changed");
    },
    async deleteLocation(locationPayload) {
      console.log(locationPayload);
      //   if (
      //     !confirm(
      //       "Are you sure you want to delete " + portfolioPayload.newName + "?"
      //     )
      //   ) {
      //     return;
      //   }
      let r = await apiLocation.deleteLocation(
        this.portfolio,
        locationPayload.section,
        locationPayload.type
      );
      console.table(r);
      let l = this.locations || this.t;
      console.log(l);
      if (r["payload"]["status"]) {
        // delete this.t[currentName];
        // this.locations = l.filter(
        //   (data) =>
        //     data.section == locationPayload.section &&
        //     data.type == locationPayload.type
        // );
        // let index = this.portfolios.indexOf(currentName);
        // if (index !== -1) {
        //   this.portfolios.splice(index, 1);
        // }
        console.log("deleted, refresh site");
        // this.$refs.green.setContent("deleted " + currentName);
        // this.$refs.green.show();
      } else {
        alert("error deleting");
        console.log("error delete");
      }
    },
    isChanged(locationPayload) {
      return (
        locationPayload.newSection !== locationPayload.oldSection ||
        locationPayload.oldType !== locationPayload.newType
      );
    },
    async updateLocation(locationPayload) {
      console.log("update");
      console.log(locationPayload);

      let params = {};

      //   todo click and drag drop UI
      params["section"] = locationPayload.newSection;
      params["type"] = locationPayload.newType;
      params["latitude"] = locationPayload.lat;
      params["longitude"] = locationPayload.lon;

      //   if (this.isNewName(portfolioPayload)) {
      //     params["name"] = portfolioPayload.newName;
      //   }
      //   if (this.isNewColour(portfolioPayload)) {
      //     params["colour"] = portfolioPayload.newColour;
      //   }
      console.log(params);
      let r = await apiLocation.patchLocation(
        this.portfolio,
        locationPayload.oldSection,
        locationPayload.oldType,
        params
      );
      if (r["payload"]["status"]) {
        console.log("location update done");
        //   this.showMessage("updated changes for " + "old name");
      } else {
        console.log("error saving");
      }
    },
  },
};
</script>

<style>
</style>