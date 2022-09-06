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
            <!-- @click="selectRow(portofolioName)" -->
            <div v-for="(portfolioPayload, id, index) in this.portfolios" :key="id"
                @click="selectRow(portfolioPayload)">
                {{ portfolioPayload }} : {{ id }} : {{ index }}

                <br>

                <div class="row">

                    <div class="col">
                        <input class="form-control" type="text" v-model="portfolioPayload.newName">
                    </div>

                    <!-- todo set modified for this also -->
                    <div class="col">
                        <div class="dropdown">
                            <button class="dropbtn">
                                {{ portfolioPayload.colour }}
                            </button>

                            <div class="dropdown-content">
                                <a @click="colorClicked(id, colourName)" href="#"
                                    v-for="(colourPayload, colourName) in this.colours" :key="colourName">

                                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24"
                                        width="24px" fill="#FF0000">
                                        <path d="M0 0h24v24H0z" fill="none" />
                                        <path :fill="colourPayload.hex"
                                            d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z" />
                                    </svg> {{ colourName }}
                                </a>

                            </div>
                        </div>
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
                        {{ locationPayload }} - {{ portfolioNameId }} - {{ index }}

                        <!-- <div class="col">
                            name
                        </div> -->
                        <!-- <div class="col">
                            section
                        </div>
                        <div class="col">
                            type
                        </div> -->
                    </div>

                </div>

                <hr>
                <br>

            </div>


        </div>


    </div>
</template>
  
<style>
.dropbtn {
    background-color: #4CAF50;
    color: white;
    padding: 16px;
    font-size: 16px;
    border: none;
    cursor: pointer;
}

.dropdown {
    position: relative;
    display: inline-block;
}

.dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
    z-index: 1;
}

.dropdown-content a {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
}

.dropdown-content a:hover {
    background-color: #f1f1f1
}

.dropdown:hover .dropdown-content {
    display: block;
}

.dropdown:hover .dropbtn {
    background-color: #3e8e41;
}
</style>

  <script>
import { apiCalls } from '../../scripts/api/comm';
import { apiLocations } from '../../scripts/api/location';
import Green from './Green.vue';


export default {
    name: "PortfolioList",
    data() {
        return {
            role: "",
            expandedGroup: [],
            colours: {},
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
        let res = await apiCalls.getPortoflios();
        if (res["auth"]["status"]) {
            console.log("status ok");
            this.colours = res["payload"]["colours"];
            this.role = res["payload"]["role"];
            this.portfolios = res["payload"]["portfolios"];
        }
    },
    methods: {
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

            console.log("todo save changes for", portfolioPayload);

            // trigger confirmation box
            let newColour = portfolioPayload.colour;
            let r = await apiCalls.createOrUpdatePortfolio(currentName, newName, newColour);
            console.log("saved or created", r);

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

            let r = await apiCalls.deletePortfolio(currentName);

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

            let r = await apiLocations.getLocationsFilterUsername(portfolioPayload.oldName);

            if (r["payload"]["status"]) {
                let p = r["payload"]["content"]

                console.table(p)
                this.locations[portfolioPayload.oldName] = p
                // console.table(this.locations)
            } else {
                // alert("error fetching")
                console.log("error fetch")
            }

            // console.log("select row", p)
            // this.$store.dispatch("selectPortfolio", p);
            // const key = p.name;
            // if (this.isExpanded(key)) {
            //     this.expandedGroup.splice(this.expandedGroup.indexOf(key), 1);
            // } else {
            //     this.expandedGroup.push(key);
            // }
        },
    },
    components: { Green }
};
</script>
  