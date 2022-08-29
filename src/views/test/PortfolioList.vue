
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
                </tr>
            </thead>
            <tbody>
                <tr v-for="portfolio in this.$store.getters.portfolios" :key="portfolio.id"
                    @click="selectRow(portfolio)" :class="{ 'table-primary': isSelected(portfolio.id) }">
                    <td scope="row">
                        {{ portfolio.name }}
                    </td>
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
              this.$store.dispatch("selectPortfolio", p);
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
  