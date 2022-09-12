<template>
  <div class="container mt-2">
    <portfolio-list />
  </div>
</template>


<script>
import PortfolioList from "../../components/BasePortfolioList.vue";

export default {
  name: "PortfolioIndex",
  data() {
    return {};
  },
  components: {
    "portfolio-list": PortfolioList,
  },
};
</script> 
