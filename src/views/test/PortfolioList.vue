
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

                        <select name="cars" id="cars">
                            <option :value="portfolio.colour">{{ portfolio.colour }}</option>

                            <option v-for="c in this.colours" :key="c" :value="c">
                                {{ c }}
                            </option>
                        </select>
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
  