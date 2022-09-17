<template>
  <div>
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
        Add
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
</template>

<script>
import LoadingComponent from "@/components/LoadingComponent.vue";
import InputFieldsForm from "@/components/InputFieldsForm.vue";
import CSRFToken from "@/components/CSRFToken.vue";
import { apiLocation } from "../scripts/api/location";

export default {
  data() {
    return {
      latitude: undefined,
      longitude: undefined,

      submitted: false,
      loading: false,
      error: undefined,
    };
  },
  methods: {
    async restartForm() {
      this.$refs.inputFields.fields["Section"]["value"] = "";
      this.$refs.inputFields.fields["Type"]["value"] = "";
      this.$refs.inputFields.fields["Portfolio"]["value"] = "";

      this.$refs.inputFields.fields["Section"]["reset"] = true;
      this.$refs.inputFields.fields["Type"]["reset"] = true;
      this.$refs.inputFields.fields["Portfolio"]["reset"] = true;

      await this.$refs.csrf.refresh();

      //   this.$refs.mappopup.closePopup();
      this.$emit("closePopup");
      this.longitude = "";
      this.latitude = "";

      this.submitted = false;
    },
    async handleSubmit() {
      this.$refs.inputFields.fields["Section"]["reset"] = false;
      this.$refs.inputFields.fields["Type"]["reset"] = false;
      this.$refs.inputFields.fields["Portfolio"]["reset"] = false;

      let t = this.$store.getters["clickedLocation"];

      this.longitude = t.longitude;
      this.latitude = t.latitude;

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
  },
  components: {
    LoadingComponent,
    InputFieldsForm,
    CSRFToken,
  },
};
</script>

<style>
</style>