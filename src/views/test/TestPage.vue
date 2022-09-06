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
// import "bootstrap/dist/css/bootstrap.css";
// import store from '../../scripts/store';

export default {
    name: "TestPag",
    // store,
    data() {
        return {
        }
    },
    components: {
        "portfolio-list": PortfolioList,
        "portfolio-details": PortfolioDetails
    }
    // ,
    // async mounted() {
    // }

};

</script> 
