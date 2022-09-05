<template>


    <div id="app" class="container mt-2">

        <!-- <SavedModal v-show="showModal" @close-modal="showModal = false" /> -->
        <hr>
        <portfolio-list />
        <hr>
        <portfolio-details />
    </div>



    <!-- <div v-if="userType === 'building_manager'">
        building_manager
        <br>
        <hr>
        portfolio, click to edit

        <div class="field">
            <span class="field-value" v-show="!showField('name')" @click="focusField('name')">{{ name }}</span>
            <input v-model="name" v-show="showField('name')" id="user-name" type="text" class="field-value form-control"
                @focus="focusField('name')" @blur="blurField">
        </div>


    </div>
    <div v-else-if="userType === 'aggregator'">
        aggregator
        <br>
        <hr>
        <button>
            create new portfolio

        </button>
    </div>
    <div v-else-if="userType === 'aggregator_and_building_manager'">
        aggregator and building_manager
        <br>
        <hr>
        <button>
            create new portfolio

        </button>
    </div> -->


</template>


<script>

import PortfolioList from "./PortfolioList.vue";
import PortfolioDetails from "./PortfolioDetails.vue";
import "bootstrap/dist/css/bootstrap.css";
import store from '../../scripts/store';

export default {
    name: "TestPag",
    store,
    data() {
        return {
            // showModal: true,
        }
    },
    components: {
        // "SavedModal": SavedModal,
        "portfolio-list": PortfolioList,
        "portfolio-details": PortfolioDetails
    },
    async mounted() {

    }

};

</script> 
