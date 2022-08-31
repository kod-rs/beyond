
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
        </div>





        <table class="table table-hover">
            <thead>
                <tr>
                    <th scope="col">Name</th>
                    <th scope="col">name changeable</th>
                    <th scope="col">marker color</th>
                    <th></th>
                    <th></th>
                </tr>


            </thead>
            <tbody>
                <!-- <div> -->
                <tr>
                    <td>a</td>
                    <td>a</td>
                    <td>a</td>
                    <td>a</td>
                    <td>a</td>
                </tr>

                <!-- </div> -->
                <tr v-for="portfolio in this.$store.getters.portfolios" :key="portfolio.id"
                    @click="selectRow(portfolio)" :class="{ 'table-primary': isSelected(portfolio.id) }">

                    <td scope="row">
                        {{ portfolio.name }}

                    </td>
                    <td scope="row">
                        <input class="form-control" type="text" id="name" :value="portfolio.name">

                    </td>
                    <td scope="row">
                        <!-- two portfolios can not have same colour -->

                        <select name="cars" id="cars">
                            <option value="volvo">blue</option>
                            <option value="saab">Saab</option>
                            <option value="mercedes">Mercedes</option>
                            <option value="audi">Audi</option>
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
            </tbody>
        </table>
    </div>
</template>
  
  <script>
  export default {
      name: "PortfolioList",
      methods: {
          selectRow(p) {
              this.$store.dispatch("selectPortfolio", p)
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
  