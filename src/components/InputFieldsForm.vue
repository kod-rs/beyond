<template>
  <div>
    <div v-for="(f, index) in fields" :key="f">
      <InputField
        :reset="f.reset"
        :placeholder="index"
        v-model="f.value"
        :id="index"
        :validationMessage="f.validationMessage"
        :showValidationMessage="f.initShowValidationMessage"
        :validationRegex="f.validationRegex"
        :autocompleteContent="f.autocomplete"
      />
    </div>
  </div>
</template>

<script>
import { apiPortfolio } from "@/scripts/api/portfolio";
import InputField from "./InputField.vue";

export default {
  components: {
    InputField,
  },
  data() {
    return {
      fields: {
        Section: {
          value: "",
          validationMessage:
            "Only letters, numbers, spaces, commas and dots accepted in the input",
          showValidationMessage: false,
          validationRegex: /^(\w|,|\.| )*$/,
          reset: false,
          autocomplete: undefined,
        },
        Type: {
          value: "",
          validationMessage:
            "Only letters, numbers, spaces, commas and dots accepted in the input",
          showValidationMessage: true,
          validationRegex: /^(\w|,|\.| )*$/,
          reset: false,
          autocomplete: undefined,
        },

        // todo create new portfolio if entered does not exist
        // check if manager and show error mesage else ask for confirmation
        Portfolio: {
          value: "",
          validationMessage:
            "Only letters, numbers, spaces, commas and dots accepted in the input",
          showValidationMessage: true,
          validationRegex: /^(\w|,|\.| )*$/,
          reset: false,
          autocomplete: undefined,
        },

        // "Latitude": {
        //     "value": "",
        //     "validationMessage": "Only coordinates (float)",
        //     "showValidationMessage": false,
        //     "validationRegex": /^[+-]?\d+(\.\d+)?$/
        // },
        // "Longitude": {
        //     "value": "",
        //     "validationMessage": "Only coordinates (float)",
        //     "showValidationMessage": false,
        //     "validationRegex": /^[+-]?\d+(\.\d+)?$/
        // },
      },
    };
  },
  async created() {
    this.fields["Portfolio"]["autocomplete"] = await this.getDataFromApi();
  },
  methods: {
    async getDataFromApi() {
      let r = await apiPortfolio.getPortoflios();
      if (r["auth"]["status"]) {
        let pl = r["payload"]["portfolios"];
        return new Set(Object.values(pl).map((i) => i.name));
      }

      return undefined;
    },
  },
};
</script>

