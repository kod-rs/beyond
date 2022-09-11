<template>
  <div>
    <div class="row align-items-center">
      <div class="col">
        <h1>Portfolio manager</h1>
      </div>

      <div v-if="this.role !== roleBuildingManagerString" class="col col-lg-1">
        <button
          v-if="!this.isTempCreated"
          class="btn btn-primary"
          @click="createRow"
        >
          Add
        </button>
        <button v-else class="btn btn-secondary" disabled>Add</button>
      </div>
    </div>

    <hr />
    notifications

    <!-- todo if multiple changes happen show one below another -->
    <Green ref="green"> </Green>

    <hr />

    <div>
      <br />
      <div v-for="portfolioPayload in this.portfolios" :key="portfolioPayload">
        <div class="row">
          {{ portfolioPayload }}
        </div>

        <div class="row">
          <div class="col">
            <input
              type="text"
              class="form-control"
              v-model="portfolioPayload.newName"
              placeholder="Portfolio name"
            />
            <!-- @input="" -->
          </div>

          <div class="col">
            <input
              type="color"
              class="form-control form-control-color"
              v-model="portfolioPayload.newColour"
            />
          </div>

          <div v-if="portfolioPayload.isInDb" class="col">
            <button
              v-if="
                isNewName(portfolioPayload) || isNewColour(portfolioPayload)
              "
              @click="updatePortfolio(portfolioPayload)"
              class="btn btn-primary"
            >
              Update
            </button>

            <button v-else class="btn btn-secondary" disabled>Update</button>
          </div>
          <div v-else class="col">
            <button
              v-if="
                isNewName(portfolioPayload) && isNewColour(portfolioPayload)
              "
              @click="createPortfolio(portfolioPayload)"
              class="btn btn-primary"
            >
              Create
            </button>

            <button v-else class="btn btn-secondary" disabled>Create</button>
          </div>

          <div class="col">
            <router-link :to="{ name: 'history' }">History</router-link>

            <!-- <button class="btn btn-primary">
                            History
                        </button> -->
          </div>

          <div class="col">
            <div v-if="this.role !== roleBuildingManagerString">
              <button
                @click="deletePortfolio(portfolioPayload)"
                class="btn btn-primary"
              >
                Delete
              </button>
            </div>
            <div v-else>
              <button
                v-if="!this.isContentCleared"
                class="btn btn-primary"
                @click="clearContentPortfolio(portfolioPayload)"
              >
                Clear content
              </button>
              <button v-else class="btn btn-secondary" disabled>
                Clear content
              </button>
            </div>
          </div>

          <div class="col">
            <button
              @click="selectRow(portfolioPayload)"
              class="btn btn-primary"
            >
              expand
            </button>

            <!--  @click="selectRow(portfolioPayload)" -->
          </div>
        </div>

        <div v-show="portfolioPayload.isExpanded">
          <div
            class="row"
            v-for="(locationPayload, portfolioNameId, index) in this.locations[
              portfolioPayload.oldName
            ]"
            :key="portfolioNameId"
          >
            <div class="col">
              {{ locationPayload }}
            </div>

            <div class="col">
              {{ portfolioNameId }}
            </div>
            <div class="col">
              {{ index }}
            </div>
          </div>
        </div>

        <hr />
        <br />
      </div>
    </div>

    <div>
      <div class="col">
        <input
          type="color"
          class="form-control form-control-color"
          v-model="tmp"
        />
      </div>
    </div>
  </div>
</template>
  

<script>
import { apiPortfolio } from "@/scripts/api/portfolio";
import { apiLocation } from "../../scripts/api/location";
import Green from "./Green.vue";
// import { apiColour } from '../../scripts/api/colour';

export default {
  name: "PortfolioList",
  data() {
    return {
      tmp: "#e01b24",
      portfolios: {},
      isTempCreated: false,
      isContentCleared: false,
      locations: {},

      portfolioNamePlaceholder: "todo",
      portfolioColourPlaceholder: "todo",

      role: "",

      roleBuildingManagerString: process.env.VUE_APP_ROLE_BUILDING_MANAGER,
      autoSave: false,
    };
  },

  async mounted() {
    await this.loadPortfolios();
  },
  methods: {
    castPortfolio(name, colour, isExpanded, isInDb) {
      return {
        newName: name,
        oldName: name,

        newColour: colour,
        oldColour: colour,

        isExpanded: isExpanded,
        isInDb: isInDb,
      };
    },
    async loadPortfolios() {
      let res = await apiPortfolio.getPortoflios();
      if (res["auth"]["status"]) {
        this.role = res["payload"]["role"];

        this.portfolios = Object.values(res["payload"]["portfolios"]);

        this.portfolios = this.portfolios.map((item) => {
          return this.castPortfolio(
            item.name,
            item.colour,
            item.isExpanded,
            true
          );
        });

        this.$waveui.notify("Portfolios loaded successfully!", "success");
      }

      // this.$waveui.notify("Location added successfully!", "success");
      // this.$waveui.notify("Location adding failed!", "error");
    },
    clearContentPortfolio(portfolioPayload) {
      console.log("todo clear content", portfolioPayload);
    },
    isNewColour(portfolioPayload) {
      return portfolioPayload.oldColour !== portfolioPayload.newColour;
    },
    isNewName(portfolioPayload) {
      return portfolioPayload.oldName !== portfolioPayload.newName;
    },
    createRow() {
      // todo check if append row to top

      this.portfolios.push(
        this.castPortfolio(
          this.portfolioNamePlaceholder,
          this.portfolioColourPlaceholder,
          false,
          false
        )
      );

      this.isTempCreated = true;
    },
    isPortfolioNameValid(name) {
      return name && name.trim() !== "";
    },
    showMessage(content) {
      this.$refs.green.setContent(content);
      this.$refs.green.show();
    },

    async createPortfolio(portfolioPayload) {
      console.log("creating portfolio");

      // todo check in backend if newname != oldname && newcolour != old

      if (!this.isPortfolioNameValid(portfolioPayload.newName)) {
        console.log("portfolio name is not valid");
        return false;
      }

      // can create new
      this.isTempCreated = false;

      let r = await apiPortfolio.createPortfolio(
        portfolioPayload.newName,
        portfolioPayload.newColour
      );

      if (r["payload"]["status"]) {
        this.showMessage("new portfolio created " + portfolioPayload.newName);
      } else {
        console.log("error saving");
      }

      portfolioPayload.isInDb = true;
    },
    async updatePortfolio(portfolioPayload) {
      console.log("update");

      let params = {};

      if (this.isNewName(portfolioPayload)) {
        params["name"] = portfolioPayload.newName;
      }

      if (this.isNewColour(portfolioPayload)) {
        params["colour"] = portfolioPayload.newColour;
      }

      console.log(params);
      let r = await apiPortfolio.patchPortoflios(
        portfolioPayload.oldName,
        params
      );

      if (r["payload"]["status"]) {
        this.showMessage("updated changes for " + portfolioPayload.newName);
      } else {
        console.log("error saving");
      }
    },
    async deletePortfolio(portfolioPayload) {
      if (portfolioPayload.newName === "") {
        //  assumption: trying to delete new portfolio
        console.log("new name is empty");
        return;
      }

      if (
        !confirm(
          "Are you sure you want to delete " + portfolioPayload.newName + "?"
        )
      ) {
        return;
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
        alert("error deleting");
        console.log("error delete");
      }
    },
    async selectRow(portfolioPayload) {
      portfolioPayload.isExpanded = !portfolioPayload.isExpanded;

      let r = await apiLocation.getLocationsFilterUsername(
        portfolioPayload.oldName
      );

      if (r["payload"]["status"]) {
        // let p =

        // console.table(p)
        this.locations[portfolioPayload.oldName] = r["payload"]["content"];
      } else {
        // alert("error fetching")
        console.log("error fetch");
      }
    },
  },
  components: { Green },
};
</script>
  