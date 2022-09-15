
<template>
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
</template>

<script>
export default {
  data() {
    return {
      showValidationMessage: false,
      re: undefined,
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
    

