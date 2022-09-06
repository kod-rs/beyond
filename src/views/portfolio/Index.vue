<template>

    <div class="container mt-2">
        <hr>
        <portfolio-list />
        <hr>
        <portfolio-details />
    </div>

</template>


<script>

import PortfolioList from "./PortfolioList.vue";
import PortfolioDetails from "./PortfolioDetails.vue";

export default {
    name: "TestPag",
    data() {
        return {
        }
    },
    components: {
        "portfolio-list": PortfolioList,
        "portfolio-details": PortfolioDetails
    }
};

</script> 
