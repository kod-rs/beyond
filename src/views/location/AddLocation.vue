<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col">
        <button @click="activateLD">click</button>

        <div v-if="ld">console.log("ld act")</div>

        <br />

        <div v-if="error" class="alert alert-danger">{{ error }}</div>

        <form @submit.prevent="handleSubmit">
          <CSRFToken ref="csrf"></CSRFToken>

          <InputFieldsForm ref="inputFields"></InputFieldsForm>

          <input hidden type="text" v-model="latitude" />
          <input hidden type="text" v-model="longitude" />

          <button
            class="btn btn-primary btn-dark btn-lg btn-block"
            :disabled="loading"
          >
            add
          </button>
          <hr />
          <button
            class="btn btn-primary btn-dark btn-lg btn-block"
            :disabled="loading"
          >
            clear
          </button>
          <LoadingComponent></LoadingComponent>
        </form>
      </div>
      <div class="col">
        <MapComponent ref="map"></MapComponent>
        <MapPopup ref="mappopup"></MapPopup>
      </div>
    </div>
  </div>
</template>

    


<script>
import MapPopup from "../../components/MapPopup.vue";
import { apiLocation } from "../../scripts/api/location";
import { toLonLat } from "ol/proj";
import { toStringHDMS } from "ol/coordinate";

import LoadingComponent from "@/components/LoadingComponent.vue";
import InputFieldsForm from "@/components/InputFieldsForm.vue";
import MapComponent from "@/components/MapComponent.vue";
import CSRFToken from "@/components/CSRFToken.vue";

export default {
  data() {
    return {
      valid: null,
      validators: {
        required: (value) => !!value || "This field is required",
      },
      latitude: undefined,
      longitude: undefined,

      submitted: false,
      loading: false,
      error: undefined,
      ld: false,
      map: undefined,
    };
  },
  methods: {
    activateLD() {
      this.ld = true;
    },
    async restartForm() {
      this.$refs.inputFields.fields["Section"]["value"] = "";
      this.$refs.inputFields.fields["Type"]["value"] = "";
      this.$refs.inputFields.fields["Portfolio"]["value"] = "";

      this.$refs.inputFields.fields["Section"]["reset"] = true;
      this.$refs.inputFields.fields["Type"]["reset"] = true;
      this.$refs.inputFields.fields["Portfolio"]["reset"] = true;

      await this.$refs.csrf.refresh();

      this.$refs.mappopup.closePopup();
      this.longitude = "";
      this.latitude = "";

      this.submitted = false;
    },

    async handleSubmit() {
      this.$refs.inputFields.fields["Section"]["reset"] = false;
      this.$refs.inputFields.fields["Type"]["reset"] = false;
      this.$refs.inputFields.fields["Portfolio"]["reset"] = false;

      this.submitted = true;
      this.error = "";

      let section = this.$refs.inputFields.fields["Section"]["value"];
      let type = this.$refs.inputFields.fields["Type"]["value"];
      let portfolio = this.$refs.inputFields.fields["Portfolio"]["value"];

      if (!(section && type && portfolio)) {
        this.error += "fill all fields";
      }
      if (!(this.latitude && this.longitude)) {
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
        .addLocation(
          portfolio,
          section,
          type,
          this.latitude,
          this.longitude,
          csrfToken
        )
        .then(
          (r) => {
            if (r.payload.status) {
              this.$waveui.notify("Location added successfully!", "success");
            } else {
              this.$waveui.notify("Location adding failed!", "error");
            }
          },
          (error) => {
            this.$waveui.notify("Location adding failed!", "error");

            console.log("error", error);
          }
        );

      await this.restartForm();
    },
    initMapPopup() {
      /**
       * Add a click handler to the map to render the popup.
       */
      this.map.on("singleclick", (evt) => {
        const coordinate = evt.coordinate;
        const hdms = toStringHDMS(toLonLat(coordinate));

        this.longitude = toLonLat(coordinate)[0];
        this.latitude = toLonLat(coordinate)[1];

        this.$refs.mappopup.setText(hdms);
        this.$refs.mappopup.setPosition(coordinate);
      });
    },
  },
  async mounted() {
    this.map = this.$refs.map.map;

    this.map.addOverlay(this.$refs.mappopup.getOverlay());

    this.initMapPopup();
  },
  components: {
    MapPopup,
    LoadingComponent,
    InputFieldsForm,
    MapComponent,
    CSRFToken,
  },
};
</script> 
