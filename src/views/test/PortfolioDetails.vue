<template>
    <div class="row">
        tmp
    </div>
    <!-- <div class="row">
        <div class="col col-lg-1">
            <button class="btn btn-secondary" @click="newPortfolio">New</button>
        </div>
    </div> -->
    <!-- <div class="row"> -->
    <!-- <br>

        <hr>
        <br> -->
    <!-- </div> -->
    <!-- <div class="row">
        <div class="col">
            <form>
                <fieldset>
                    <legend>new Portfolio Details</legend>

                    <div class="form-group">
                        <label for="name">Name</label>
                        <input class="form-control" type="text" id="name" :value="selectedPortfolio.name">
                    </div>
                    <hr>
                    <div class="form-group">
                        <label for="name">Colour</label>
                        <br>
                        todo dropdown autocomplete / color picker
                        <br>
                        <input type="text" v-model="this.colour">
                    </div>


                    <button type="submit" class="btn btn-primary" @click.prevent="savePerson">Save</button>
                </fieldset>
            </form>
        </div>

    </div> -->



</template>
  
  <script>
  import { mapState } from "vuex";
  
  export default {
      name: "PortfolioDetails",
      data() {
          return {
              colour: "tmp color placeholder"
          }
      }
      ,
      methods: {
          newPortfolio() {
              const p = {
                  name: "New Portfolio",
                  colour: "tmp new colour"
  
              };
              this.$store.dispatch("addPortfolio", p);
          },
          savePerson(event) {
              const p = {
                  id: event.target.form["id"].value,
                  name: event.target.form["name"].value
                  //   colour: "tmp new colour"
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