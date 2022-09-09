<template>
    <div>
        <div class="row align-items-center">
            <div class="col">
                <h1>Portfolio manager</h1>
            </div>

            <!-- todo role check config file -->
            <div v-if="this.role !== 'manager'" class="col col-lg-1">

                <button v-if="!this.isTempCreated" class="btn btn-primary" @click="createRow">Add</button>
                <button v-else class="btn btn-secondary" disabled>Add</button>

            </div>

        </div>

        <hr>
        notifications

        <!-- todo if multiple changes happen show one below another -->
        <Green ref="green">
        </Green>

        <hr>

        <div>
            <br>
            <!--  @click="selectRow(portfolioPayload)" -->
            <div v-for="(portfolioPayload, id, index) in this.portfolios" :key="id">
                {{ portfolioPayload }} : {{ id }} : {{ index }}

                <br>

                <div class="row">

                    <div class="col">
                        <input class="form-control" type="text" v-model="portfolioPayload.newName">
                    </div>

                    <div class="col">
                        {{portfolioPayload.colourHex}}
                    </div>

                    <div class="col">
                        <input type="color" class="form-control form-control-color" id="exampleColorInput"
                            v-model="portfolioPayload.colourHex">
                    </div>
                    <div class="col">
                        <button @click="revertcolourshow(portfolioPayload.oldName)">revert</button>
                    </div>


                    <div class="col">

                        <button v-if="portfolioPayload.newName !== portfolioPayload.oldName"
                            @click="savePortfolio(portfolioPayload)" class="btn btn-primary">Save</button>
                        <button v-else class="btn btn-secondary" disabled>Save</button>

                    </div>

                    <div class="col">


                        <!-- todo role check config file -->
                        <div class="col col-lg-1">
                            <div v-if="this.role !== 'manager'">

                                <button @click="deletePortfolio(portfolioPayload)"
                                    class="btn btn-primary">Delete</button>

                            </div>
                            <div v-else>

                                <button v-if="!this.isContentCleared" class="btn btn-primary"
                                    @click="clearContentPortfolio(portfolioPayload)">
                                    Clear content
                                </button>
                                <button v-else class="btn btn-secondary" disabled>Clear content</button>


                            </div>

                        </div>



                    </div>


                </div>
                <div v-show="portfolioPayload.isExpanded">

                    <div class="row"
                        v-for="(locationPayload, portfolioNameId, index) in this.locations[portfolioPayload.oldName]"
                        :key="portfolioNameId">
                        <div class="col">
                            {{locationPayload}}
                        </div>

                        <div class="col">
                            {{portfolioNameId}}
                        </div>
                        <div class="col">
                            {{index}}
                        </div>

                    </div>

                </div>

                <hr>
                <br>

            </div>


        </div>


    </div>
</template>
  

<script>
import { apiPortfolio } from '@/scripts/api/portfolio';
import { apiLocation } from '../../scripts/api/location';
import Green from './Green.vue';
import { apiColour } from '../../scripts/api/colour';


export default {
    name: "PortfolioList",
    data() {
        return {
            role: "",
            expandedGroup: [],
            portfolios: {},
            isTempCreated: false,
            timer: 1,
            customContent: "customContent",
            autoSave: false,
            isContentCleared: false,
            locations: {}
        };
    },

    async mounted() {
        console.log("moutned");
        let res = await apiPortfolio.getPortoflios();
        if (res["auth"]["status"]) {
            console.log("status ok");
            this.role = res["payload"]["role"];
            this.portfolios = res["payload"]["portfolios"];
        }
    },
    methods: {
        async revertcolourshow(portfolioName) {
            console.log("revert colour, show history");

            let res = await apiColour.getColourHistory(portfolioName);
            if (res["auth"]["status"]) {
                console.log("status ok");
                let colourHistory = res["payload"]["value"];
                console.table(colourHistory);
            }

        },
        clearContentPortfolio(portfolioPayload) {
            console.log("clear content", portfolioPayload)
        },

        createRow() {

            console.log("create row");
            if (this.isTempCreated) {
                return
            }

            let currentSize = Object.keys(this.portfolios).length;
            console.log("current size", currentSize)

            this.portfolios[currentSize] = {
                "newName": "",
                "oldName": "",
                "colour": "placeholder",
                "isExpanded": false,
                // "locations"

            };
            this.isTempCreated = true;

        },
        async savePortfolio(portfolioPayload) {
            let currentName = portfolioPayload.oldName;
            let newName = portfolioPayload.newName;
            console.log(newName === "")
            if (newName === "") {
                console.log("new name is empty")
                return
            }

            if (!currentName && newName !== "") {
                // can create new
                this.isTempCreated = false;
            }

            let r = await apiPortfolio.createOrUpdatePortfolio(currentName, newName, portfolioPayload.colourHex);

            if (r["payload"]["status"]) {
                this.$refs.green.setContent("saved changes for " + newName);
                this.$refs.green.show();

            } else {
                console.log("error saving")
            }



        },
        async deletePortfolio(portfolioPayload) {

            if (portfolioPayload.newName === "") {
                //  assumption: trying to delete new portfolio
                console.log("new name is empty")
                return
            }

            if (!confirm('Are you sure you want to delete ' + portfolioPayload.newName + '?')) {
                return
            }

            let currentName = portfolioPayload.oldName;

            let r = await apiPortfolio.deletePortfolio(currentName);

            if (r["payload"]["status"]) {
                delete this.portfolios[currentName];

                this.$refs.green.setContent("deleted " + currentName);
                this.$refs.green.show();

            } else {
                alert("error deleting")
                console.log("error delete")
            }

        },
        colorClicked(portfolioName, colourName) {
            this.portfolios[portfolioName]["colour"] = colourName;
        },
        async selectRow(portfolioPayload) {
            portfolioPayload.isExpanded = !portfolioPayload.isExpanded;

            let r = await apiLocation.getLocationsFilterUsername(portfolioPayload.oldName);

            if (r["payload"]["status"]) {
                // let p = 

                // console.table(p)
                this.locations[portfolioPayload.oldName] = r["payload"]["content"]
            } else {
                // alert("error fetching")
                console.log("error fetch")
            }

        },
    },
    components: { Green }
};
</script>
  