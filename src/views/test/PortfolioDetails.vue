<template>
    <div class="row">
        <div class="col col-lg-1">
            <button class="btn btn-secondary" @click="newPortfolio">New</button>
        </div>
        <div class="col">
            <form>
                <fieldset>
                    <legend>Details</legend>

                    <input type="hidden" id="id" :value="selectedPortfolio.id">

                    <div class="form-group">
                        <label for="name">Name</label>
                        <input class="form-control" type="text" id="name" :value="selectedPortfolio.name">
                    </div>

                    <div class="form-group">
                        <label for="name">Colour</label>
                        <br>
                        todo dropdown autocomplete / color picker
                    </div>


                    <button type="submit" class="btn btn-primary" @click.prevent="savePerson">Save</button>
                </fieldset>
            </form>
        </div>
    </div>
</template>
  
  <script>
  import { mapState } from "vuex";
  
  export default {
      name: "PortfolioDetails",
      methods: {
          newPortfolio() {
              const p = {
                  name: "New Portfolio",
              };
              this.$store.dispatch("addPortfolio", p);
          },
          savePerson(event) {
              const p = {
                  id: event.target.form["id"].value,
                  name: event.target.form["name"].value,
              };
              this.$store.dispatch("updatePortfolio", p);
          }
      },
      computed: {
          ...mapState({
              selectedPortfolio: state => state.selectedPortfolio
          })
      }
  };
  </script>