<template>
  <div></div>
</template>
 
<script>
export default {
  data() {
    return {};
  },
  methods: {
    showMessage(result, successMessage, errorMessage) {
      if (result) {
        if (successMessage) {
          this.$waveui.notify(successMessage, "success");
        }
      } else {
        if (errorMessage) {
          this.$waveui.notify(errorMessage, "error");
        }
      }
    },
  },
};
</script>
 
<style>
</style>