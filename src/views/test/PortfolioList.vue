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

        <Green ref="green">
        </Green>

        <hr>

        <div>
            <br>
            <!-- @click="selectRow(portofolioName)" -->
            <div v-for="(portfolioPayload, id, index) in this.portfolios" :key="id">
                {{ portfolioPayload }} : {{ id }} : {{ index }}

                <br>

                <div class="row">

                    <div class="col">
                        <input class="form-control" type="text" v-model="portfolioPayload.newName">
                    </div>
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

                        <!-- todo make disableable -->
                        <button @click="savePortfolio(portfolioPayload)" class="btn btn-secondary">Save</button>

                    </div>

                    <div class="col">

                        <button @click="deletePortfolio(portfolioName)" class="btn btn-secondary">Delete</button>

                    </div>

                </div>


                <hr>
                <br>

            </div>

            <!-- <div class="container text-center" v-for="(portfolioPayload, portfolioName) in this.portfolios"
                :key="portfolioName" @click="selectRow(portfolioName)">

                <div class="row">
                    <div class="col">
                        <input class="form-control" type="text" id="name" :value="portofolioName">
                    </div>
                    <div class="col">
                        <div class="dropdown">
                            <button class="dropbtn">
                                {{ portfolioPayload }}
                            </button>

                            <div class="dropdown-content">
                                <a @click="colorClicked(portfolio.name, colourName)" href="#"
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
                        <button @click="deletePortfolio(portfolio.name)" class="btn btn-secondary">Delete</button>

                    </div>

                </div>

                <div v-show="isUpdated(portfolio.name)">
                    <div class="alert alert-success" role="alert">
                        updated & saved, todo what?
                    </div>
                </div>

                <div v-show="isExpanded(portfolio.name)">
                    bbbbbbbbbbbbbbbbbbbbbbbbb</div>

                <hr>
                <br>

            </div> -->
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
import { apiCalls } from '../../scripts/api';
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
            customContent: "customContent"
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
        console.log("portf", this.portfolios);
    },
    methods: {
        createGreenRef(portfolioName) {
            console.log("new for ", portfolioName)
            return "green-" + portfolioName.replaceAll(" ", "-");
        },
        createRow() {
            console.log("create row");
            // todo check if empty exist 
            let currentSize = Object.keys(this.portfolios).length;
            console.log("current size", currentSize)

            this.portfolios[currentSize] = { "name": "ph name", "colour": "placeholder" };
            this.isTempCreated = true;
            // let currentName = this.portfolios[index].name;

            // write to db
        },
        // isUpdated(portfolioName) {
        //     console.log(".updated", portfolioName)
        //     return true
        // },
        async savePortfolio(portfolioPayload) {
            // let portfolioName = portfolioPayload.name;
            console.log("todo save changes for", portfolioPayload);

            // trigger confirmation box
            let currentName = portfolioPayload.oldName;
            // console.log("current name", currentName);
            let newName = portfolioPayload.newName;
            let newColour = portfolioPayload.colour;
            // console.log(newName, newColour);


            let r = await apiCalls.createOrUpdatePortfolio(currentName, newName, newColour);
            console.log("saved or created", r);

            this.$refs.green.setContent("saved changes for " + newName);
            this.$refs.green.show();


            // this.timer = 0;
            // this.timer = 2;
            // this.customContent = "saved changes for" + portfolioName;
            // this.timer = 0;
            // this.timer = 2;

            // let name = this.createGreenRef(portfolioName);
            // console.log("name", name);
            // this.$refs[name].show();
        },
        // deletePortfolio(portfolioName) {
        //     console.log("todo delete for", portfolioName);
        //     this.$store.dispatch(
        //         "deletePortfolio",
        //         portfolioName
        //     );
        //     // if (confirm('Are you sure?')) {
        //     //     // this.deleteRow();
        //     //     console.log('deleter.');
        //     // } else {
        //     //     // Do nothing!
        //     //     console.log('no delete.');
        //     // }
        // },
        colorClicked(portfolioName, colourName) {
            this.portfolios[portfolioName]["colour"] = colourName;
        },
        // isExpanded(key) {
        //     return this.expandedGroup.indexOf(key) !== -1;
        // },
        // selectRow(p) {
        //     this.$store.dispatch("selectPortfolio", p);
        //     const key = p.name;
        //     if (this.isExpanded(key)) {
        //         this.expandedGroup.splice(this.expandedGroup.indexOf(key), 1);
        //     } else {
        //         this.expandedGroup.push(key);
        //     }
        // },
        // isSelected(id) {
        //     console.log(id)
        //     return false
        //     // return id == this.$store.getters.selectedPortfolio.id;
        // },
        // deleteRow() {
        //     this.$store.dispatch(
        //         "deletePortfolio",
        //         this.$store.getters.selectedPortfolio.id
        //     );
        // }
    },
    components: { Green }
};
</script>
  