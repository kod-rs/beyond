
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
        </div>

        <table class="table table-hover">
            <thead>
                <tr>
                    <th scope="col">Name</th>
                    <!-- <th scope="col">name changeable</th> -->
                    <th scope="col">marker color</th>
                    <th></th>
                    <th></th>
                </tr>


            </thead>
            <tbody v-for="portfolio in this.$store.getters.portfolios" :key="portfolio.id" @click="selectRow(portfolio)"
                :class="{ 'table-primary': isSelected(portfolio.id) }">

                <tr>

                    <td scope="row">
                        <input class="form-control" type="text" id="name" :value="portfolio.name">
                    </td>

                    <td scope="row">
                        <!-- two portfolios can not have same colour -->

                        <div class="dropdown">
                            <button class="dropbtn">
                                {{ portfolio.colour }}
                            </button>

                            <div class="dropdown-content">

                                <a href="#" v-for="c in this.colours" :key="c" :value="c.name">

                                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24"
                                        width="24px" fill="#FF0000">
                                        <path d="M0 0h24v24H0z" fill="none" />
                                        <path :fill="c.hex"
                                            d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z" />
                                    </svg> {{ c.name }}
                                </a>


                                <a href="#">
                                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24"
                                        width="24px" fill="#FF0000">
                                        <path d="M0 0h24v24H0z" fill="none" />
                                        <path fill="#FF0000"
                                            d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z" />
                                    </svg> red
                                </a>

                            </div>
                        </div>


                    </td>

                    <td scope='row'>
                        <button class="btn btn-secondary">Save changes</button>
                    </td>

                    <td scope='row'>
                        <button class="btn btn-secondary">Delete</button>
                    </td>

                    <hr>
                    <br>


                </tr>
                <tr v-show="isExpanded(portfolio.name)">
                    <!-- {{ group.desc }} -->
                    bbbbbbbbbbbbbbbbbbbb
                </tr>
                <!-- <tr>
                    fff
                    <td>a</td>

                    <td>a</td>
                </tr> -->
            </tbody>
        </table>
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
            colours: {}

        }
    },
    async mounted() {
        console.log("moutned")
        let res = await apiCalls.getPortoflios();
        //   console.log(res);

        if (res["auth"]["status"]) {
            console.log("status ok")

            this.colours = res["payload"]["colours"];
            this.role = res["payload"]["role"];
            const portfolios = res["payload"]["portfolios"];




            // const existingPortfolios = this.$store.getters.portfolios;

            for (const [portfolioName, portfolioDetails] of Object.entries(portfolios)) {


                this.$store.dispatch("addPortfolio",
                    {
                        name: portfolioName,
                        colour: portfolioDetails["colour"]
                    }
                );

            }



        }
    },
    methods: {
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
            return id == this.$store.getters.selectedPortfolio.id;
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
  