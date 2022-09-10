<template>

    <div class="container mt-2">
        <hr>
        <portfolio-list />
        <hr>
        <portfolio-details />

        <hr>



        <div class="col">
            <div class="row">
                <input type="text" v-model="colourHex">
                <button @click="addColour">add colour</button>
                <hr>
            </div>

            <div class="row">
                <button @click="refresh">refresh</button>
                current state
                <br>
                <div v-for="i in colours" :key="i">
                    {{i}}
                </div>
                <hr>
            </div>

            <div class="row">
                <button @click="deleteAll">clear list</button>
                <hr>
            </div>
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
            colourHex: "#p",
            colours: ["a", "b"]
        }
    },
    components: {
        "portfolio-list": PortfolioList,
        "portfolio-details": PortfolioDetails
    },
    methods: {
        async deleteAll() {
            console.log("delete all");
            let r = await apiColour.deleteColour("a");
            console.log(r)
        },

        async refresh() {
            let r = await apiColour.getColourHistory("a");
            console.table(r["payload"]["value"])

            this.colours = [];
            for (const [key, value] of Object.entries(r["payload"]["value"])) {
                console.log(key, value, typeof (key));
                this.colours.push(value);
            }
        },

        async addColour() {
            console.log(this.colourHex)
            console.log("add c")
            let r = await apiColour.addColour("a", this.colourHex);
            console.log(r);

        }
    }
};

</script> 
