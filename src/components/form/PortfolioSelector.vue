<template>
    <div>
        <div>
            enter portfolio

        </div>

        <InputAutocomplete @input="userTypedLocation" ref="inputautocompletefield" :initItems="[]">

        </InputAutocomplete>


    </div>
</template>

<script>
import InputAutocomplete from './../form/InputAutocomplete.vue';
import { apiPortfolio } from '../../scripts/api/portfolio';

export default {
    components: {
        InputAutocomplete
    },
    data() {
        return {
        }
    },
    methods: {
        getSearch() {
            return this.$refs.inputautocompletefield.getSearch();

        },

        userTypedLocation(location) {
            console.log("new portfolio typed", location);
        },
        async getLocations() {
            let r = await apiPortfolio.getPortoflios();

            if (r["auth"]["status"]) {
                let pl = r["payload"]["portfolios"];

                let c = Object.keys(pl);
                this.$refs.inputautocompletefield.updateItems(c);
            }
        },

    }
    ,
    mounted() {
        this.getLocations();

        this.$refs.inputautocompletefield.setPlaceholder("type portfolio");

    }
}
</script>