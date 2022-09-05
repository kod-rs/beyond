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
// import { apiCalls } from '../../scripts/api';
import "bootstrap/dist/css/bootstrap.css";
// import SavedModal from '../../components/modals/SavedModal.vue'

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
        // console.log("moutned")
        // let res = await apiCalls.getPortoflios();
        // console.log(res);

        // if (res["auth"]["status"]) {
        //     console.log("status ok")

        //     const role = res["payload"]["role"];
        //     const portfolios = res["payload"]["portfolios"];
        //     console.log("role", role);
        //     console.log("portfolios", portfolios)
        // }

    }

};

// export default {
//     data() {
//         return {
//             userType: 'building_manager',
//             name: 'ffff',
//             editField: ''
//         };
//     },
//     mounted() {
//         console.log('type', this.userType)
//     },
//     methods: {
//         focusField(name) {
//             this.editField = name;
//         },
//         blurField() {
//             this.editField = '';
//         },
//         showField(name) {
//             return (this.name == '' || this.editField == name)
//         }
//     }

// };
</script> 
