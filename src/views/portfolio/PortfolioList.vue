<template>
    <div>
        <div class="row align-items-center">
            <div class="col">
                <h1>Portfolio manager</h1>
            </div>

            <div v-if="this.role !== roleBuildingManagerString" class="col col-lg-1">

                <button v-if="!this.isTempCreated" class="btn btn-primary" @click="createRow">Add</button>
                <button v-else class="btn btn-secondary" disabled>Add</button>

            </div>

        </div>

        <div v-for="t in tmp" :key="t">
            {{t}}
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
            <div v-for="portfolioPayload in this.portfolios" :key="portfolioPayload">
                {{portfolioPayload}}
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
                            v-model="portfolioPayload.colourHex" @change="updateEditorColor(portfolioPayload)">
                    </div>

                    <div class="col">
                        <button
                            v-if="portfolioPayload.newName !== portfolioPayload.oldName || portfolioPayload.metaUpdated"
                            @click="savePortfolio(portfolioPayload)" class="btn btn-primary">Save</button>
                        <button v-else class="btn btn-secondary" disabled>Save</button>
                    </div>

                    <div class="col">
                        <router-link :to="{ name: 'history' }">History</router-link>

                        <!-- <button class="btn btn-primary">
                            History
                        </button> -->
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
// import { apiColour } from '../../scripts/api/colour';

export default {
    name: "PortfolioList",
    data() {
        return {
            expandedGroup: [],
            portfolios: {},
            isTempCreated: false,
            timer: 1,
            customContent: "customContent",
            autoSave: false,
            isContentCleared: false,
            locations: {},

            portfolioNamePlaceholder: "todo",
            portfolioColourPlaceholder: "todo",

            role: "",
            roleBuildingManagerString: process.env.VUE_APP_ROLE_BUILDING_MANAGER,


            tmp: ["a", "b", "c"]
        };
    },

    async mounted() {
        await this.loadPortfolios();
    },
    methods: {
        async updateEditorColor(portfolioPayload) {
            // .oldName, portfolioPayload.colourHex
            // let r = await apiColour.getColourHistory(portfolioPayload.oldName);
            // let lastVal = undefined;
            // for (const [key, value] of Object.entries(r["payload"]["value"])) {
            //     console.log(key, value, typeof (key));
            //     lastVal = value;
            //     break;
            // }

            // if (lastVal === portfolioPayload.colourHex) {
            //     console.log("same colour picked")
            // } else {
            // console.log("new colour")
            portfolioPayload.metaUpdated = true
            // }

        },
        async loadPortfolios() {
            let res = await apiPortfolio.getPortoflios();
            if (res["auth"]["status"]) {
                this.role = res["payload"]["role"];

                this.portfolios = Object.values(res["payload"]["portfolios"]);

                this.portfolios.forEach(item => {
                    return { ...item, "isCreated": true }
                });

            }
        },
        clearContentPortfolio(portfolioPayload) {
            console.log("clear content", portfolioPayload)
        },
        // getAdditionalPortfolioFields() {
        //     return {
        //         "isCreated": false
        //     }
        // },
        createRow() {
            // todo  append row to top

            // if (this.isTempCreated) {
            //     return
            // }

            // let currentSize = Object.keys(this.portfolios).length;

            this.portfolios.push({
                "newName": this.portfolioNamePlaceholder,
                "oldName": this.portfolioNamePlaceholder,
                "colour": this.portfolioColourPlaceholder,
                "isExpanded": false,
                "isCreated": false
            });
            this.isTempCreated = true;

        },
        // async patchPortfolio(portfolioPayload) {

        // }
        async trueSavePortfolio(portfolioPayload) {
            console.log("save");

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
        async trueUpdatePortfolio(portfolioPayload) {
            console.log("update");

            let r = await apiPortfolio.patchPortoflios(portfolioPayload.oldName, portfolioPayload.newName, portfolioPayload.colourHex);

            if (r["payload"]["status"]) {
                this.$refs.green.setContent("saved changes for " + portfolioPayload.newName);
                this.$refs.green.show();

            } else {
                console.log("error saving")
            }
        },
        async savePortfolio(portfolioPayload) {
            console.table("is cre", portfolioPayload.isCreated)

            if (!portfolioPayload.isCreated) {
                await this.trueSavePortfolio(portfolioPayload);
                portfolioPayload.isCreated = true;

            } else {
                await this.trueUpdatePortfolio(portfolioPayload);
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

                // this.portfolios = this.portfolios.filter(data => data.oldName == currentName);
                let index = this.portfolios.indexOf(currentName);
                if (index !== -1) {
                    this.portfolios.splice(index, 1);
                }


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
  