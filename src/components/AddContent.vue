<template>
  <div>
    <form @submit.prevent="addLocation">
      <CSRFToken ref="csrf"></CSRFToken>

      <div v-if="error" class="alert alert-danger">{{ error }}</div>

      <ui-textfield
        fullwidth
        v-model="section"
        helper-text-id="my-text-field-helper-text"
      >
        Section
      </ui-textfield>

      <br />
      <br />
      <ui-textfield
        fullwidth
        v-model="type"
        helper-text-id="my-text-field-helper-text"
      >
        Type
      </ui-textfield>
      <br />
      <br />
      <section>
        <ui-select fullwidth :options="options" v-model="portfolio">
          Portfolio
        </ui-select>
      </section>

      <br />
      <div class="row">
        <div class="col">
          <button :disabled="loading" class="btn btn-primary">Add</button>
        </div>
      </div>
    </form>
    <br />
    <br />

    <div class="col">
      <button class="btn btn-primary" @click="clearForm">Clear</button>
    </div>
  </div>

  <!-- </div> -->
</template>

<script>
import { apiPortfolio } from "@/scripts/api/portfolio";
import { apiLocation } from "../scripts/api/location";
import CSRFToken from "@/components/CSRFToken.vue";

export default {
  data() {
    return {
      options: [],
      portfolio: "",
      section: "",
      type: "",

      submitted: false,
      loading: false,
      error: undefined,
    };
  },
  async mounted() {
    await this.getPortfolios();
  },
  methods: {
    async handleSubmit() {
      //     "Only letters, numbers, spaces, commas and dots accepted in the input",
      //   validationRegex: /^(\w|,|\.| )*$/,

      let t = this.$store.getters["clickedLocation"];

      if (!t) {
        console.log("no t", t);
        this.error = "Select location";
        // this.$waveui.notify("Select location", "warning");

        return;
      }

      let longitude = t.longitude;
      let latitude = t.latitude;

      this.submitted = true;
      this.error = "";

      let section = this.section;
      let portfolio = this.portfolio;
      let type = this.type;

      if (!(this.section && this.type && this.portfolio)) {
        this.error += "fill all fields";
      }
      if (!(latitude && longitude)) {
        this.error += "\nselect location";
      }

      // todo check portfolio
      const csrfToken = this.$store.state.synchronizerToken;

      if (!csrfToken) {
        alert("error with auth, reloading");
        this.$waveui.notify("Authentication failed! Reloading", "warning");

        this.$router.go();
      }

      if (this.error) {
        return;
      }

      await apiLocation
        .addLocation(portfolio, section, type, latitude, longitude, csrfToken)
        .then(
          (r) => {
            if (r.payload.status) {
              console.log("add ok");
              this.$waveui.notify("Location added successfully!", "success");
            } else {
              this.$waveui.notify("Location adding failed!", "error");
              console.log("add err");
            }
          },
          (error) => {
            console.log("Location adding failed");

            this.$waveui.notify("Location adding failed!", "error");

            console.log("error", error);
          }
        );

      //   await this.restartForm();
      this.clearForm();
      await this.$refs.csrf.refresh();
      this.submitted = false;
      this.$emit("closePopup");
    },
    addLocation() {
      console.log("add location", this.section, this.type, this.portfolio);
      this.handleSubmit();
    },
    clearForm() {
      this.section = "";
      this.type = "";
    },
    onSelected(selected) {
      this.selected = selected.value;
    },
    transformForSelection(p) {
      let t = [];
      for (const value of Object.values(p)) {
        t.push({ label: value.name, value: value.name });
      }

      return t;
    },
    async getPortfolios() {
      let r = await apiPortfolio.getPortoflios();
      if (r["auth"]["status"]) {
        let pl = r["payload"]["portfolios"];

        this.options = this.transformForSelection(pl);
      }

      return undefined;
    },
  },
  components: {
    CSRFToken,
  },
};
</script>

<style>
</style>