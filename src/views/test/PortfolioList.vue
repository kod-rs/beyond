<template>
    <div>
        <div class="row align-items-center">
            <div class="col">
                <h1>Portfolio list</h1>
            </div>
            <div class="col col-lg-1">
                <button class="btn btn-secondary" @click="deleteRow"
                    :disabled="this.$store.getters.selectedPortfolio.id == -1">Delete</button>
            </div>

            <div>
                portfolio type for role: {{ this.role }}
            </div>

            <!-- <div>
                <input name="optionsRadios" id="optionsRadios1" v-model="srStatus">
            </div> -->
        </div>

        <div>

            <div class="container text-center" v-for="(portfolioPayload, portofolioName) in this.portfolios"
                :key="portofolioName" @click="selectRow(portofolioName)">

                <div class="row">
                    <div class="col">
                        <input class="form-control" type="text" id="name" :value="portofolioName">
                    </div>
                    <div class="col">
                        <div class="dropdown">
                            <button class="dropbtn">
                                {{ portfolio.colour }}
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
import { apiCalls } from '../../scripts/api';


export default {
    name: "PortfolioList",
    data() {
        return {
            role: "",
            expandedGroup: [],
            colours: {},
            portfolios: {}

        }
    }
    // , watch: {
    //     srStatus: function (val) {
    //         console.log("val c", val)
    //         // for (var i = 0; i < this.cases.length; i++) {
    //         //     if (this.cases[i].status == val) {
    //         //         this.activeCases.push(this.cases[i]);
    //         //         console.log("fired", val)
    //         //         // alert("Fired! " + val);
    //         //     }
    //         // }
    //     }
    // },
    ,
    async mounted() {
        console.log("moutned")
        let res = await apiCalls.getPortoflios();

        if (res["auth"]["status"]) {
            console.log("status ok")


            this.colours = res["payload"]["colours"];
            this.role = res["payload"]["role"];
            this.portfolios = res["payload"]["portfolios"];

            // const existingPortfolios = this.$store.getters.portfolios;

            // for (const [portfolioName, portfolioDetails] of Object.entries(portfolios)) {


            //     this.$store.dispatch("addPortfolio",
            //         {
            //             name: portfolioName,
            //             colour: portfolioDetails["colour"]
            //         }
            //     );

            // }



        }
    },
    methods: {
        isUpdated(portfolioName) {
            console.log(".updated", portfolioName)
            return true
        },
        savePortfolio(portfolioName) {
            console.log("todo save changes for", portfolioName);
        },
        deletePortfolio(portfolioName) {
            console.log("todo delete for", portfolioName);

            this.$store.dispatch(
                "deletePortfolio",
                portfolioName
            );

            // if (confirm('Are you sure?')) {
            //     // this.deleteRow();
            //     console.log('deleter.');
            // } else {
            //     // Do nothing!
            //     console.log('no delete.');
            // }
        },
        colorClicked(portfolioName, colourName) {
            console.log("clicked", colourName, "from", portfolioName)
            this.$store.dispatch("updatePortfolioColour", {
                "portfolioName": portfolioName,
                "colourName": colourName
            });
        },
        isExpanded(key) {
            return this.expandedGroup.indexOf(key) !== -1;
        },
        selectRow(p) {
            this.$store.dispatch("selectPortfolio", p);

            const key = p.name;

            if (this.isExpanded(key)) {
                this.expandedGroup.splice(this.expandedGroup.indexOf(key), 1);
            } else {
                this.expandedGroup.push(key);
            }

        },
        isSelected(id) {
            console.log(id)
            return false
            // return id == this.$store.getters.selectedPortfolio.id;
        },
        deleteRow() {
            this.$store.dispatch(
                "deletePortfolio",
                this.$store.getters.selectedPortfolio.id
            );
        }
    }
};
</script>
  