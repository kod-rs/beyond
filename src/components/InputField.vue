
<template>
  <div>
    <input
      hidden
      :placeholder="reset"
      class="form-control"
      :value="reset"
      @input="$emit('update:reset', $event.target.value)"
    />

    <div v-if="autocompleteContent">
      <select
        content="please select..."
        name="choosable"
        @input="$emit('update:modelValue', $event.target.value)"
        class="form-select"
      >
        <option v-if="!isDeletedTemplate" value="1" disabled selected>
          Portfolio
        </option>

        <option v-for="i in autocompleteContent" :key="i" :value="i">
          {{ i }}
        </option>
      </select>
    </div>
    <div v-else>
      <input
        :list="id"
        :placeholder="placeholder"
        class="form-control"
        :value="modelValue"
        :key="id"
        :name="id"
        @input="$emit('update:modelValue', $event.target.value)"
        autocomplete="off"
      />
      <br />

      <datalist :id="id">
        <option v-for="i in autocompleteContent" :key="i" :value="i" />
      </datalist>
    </div>

    <datalist :id="id">
      <option v-for="i in autocompleteContent" :key="i" :value="i" />
    </datalist>

    <div v-if="showValidationMessage">
      <br />
      <div class="alert alert-danger">
        {{ validationMessage }}
      </div>
    </div>

    <!-- todo -->
    <!-- <div v-if="submitted && !option.value" class="red">
            {{ option.key }} is required
        </div> -->
  </div>
</template>

<script>
export default {
  data() {
    return {
      showValidationMessage: false,
      re: undefined,
      isDeletedTemplate: false,
      open: false,
    };
  },
  props: {
    reset: Boolean,
    placeholder: String,
    modelValue: String,
    id: String,
    validationMessage: String,
    validationRegex: RegExp,

    initShowValidationMessage: Boolean,
    autocompleteContent: Set,
  },
  mounted() {
    this.re = new RegExp(this.validationRegex, "g");
  },
  watch: {
    reset(newValue) {
      if (newValue) {
        this.showValidationMessage = false;
      }
    },
    modelValue(newValue) {
      if (this.autocompleteContent) {
        console.log("delete template");
        this.isDeletedTemplate = true;
      }

      this.showValidationMessage = !this.validateInput(newValue);
    },
  },

  emits: ["update:modelValue"],
  methods: {
    validateInput(content) {
      if (content === "") {
        return false;
      }

      return this.validationRegex.test(content);
    },
  },
};
</script>
    

