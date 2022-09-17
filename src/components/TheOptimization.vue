<template>
  <div>
    {{ locations }}
    <br />
    <hr />
    <button @click="performOptimization">optimize selected</button>
  </div>
</template>

<script>
export default {
  props: {
    locations: Object,
  },
  data() {
    return {};
  },
  methods: {
    performOptimization() {
      console.log("optimize with");
      console.log(this.locations);
      // todo make api call for this optimization and show message if optimization
    },
  },
};
</script>

<style>
</style>