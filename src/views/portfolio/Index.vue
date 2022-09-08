<template>

    <div class="container mt-2">
        <hr>
        <portfolio-list />
        <hr>
        <portfolio-details />

        <hr>

        <button @click="addColour">add colour</button>


        <div class="col">
            <input type="color" class="form-control form-control-color" v-model="colourHex">
        </div>
    </div>

</template>


<script>

import PortfolioList from "./PortfolioList.vue";
import PortfolioDetails from "./PortfolioDetails.vue";
import { apiColour } from '../../scripts/api/colour';

export default {
    name: "TestPag",
    data() {
        return {
            colourHex: "#3584e4"
        }
    },
    components: {
        "portfolio-list": PortfolioList,
        "portfolio-details": PortfolioDetails
    },
    methods: {
        async addColour() {
            console.log(this.colourHex)
            console.log("add c")
            let r = await apiColour.addColour("a", this.colourHex);
            console.log(r);

        }
    }
};

</script> 
