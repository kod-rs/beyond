<template>
    <div>
        <div>
            enter portfolio

        </div>

        <InputAutocomplete @input="userTypedLocation" ref="inputautocompletefield" :initItems="[]">

        </InputAutocomplete>

        <button @click="buttonClicked">search</button>

    </div>
</template>

<script>
import InputAutocomplete from './../form/InputAutocomplete.vue';
import countryNameJson from "/public/assets/layers/country_names.json";
import axios from 'axios';

export default {
    components: {
        InputAutocomplete
    },
    data() {
        return {
        }
    },
    methods: {
        buttonClicked() {
            let location = this.$refs.inputautocompletefield.getSearch();
            console.log("search for portfolio:", location)

        },
        userTypedLocation(location) {
            console.log("new portfolio typed", location);
        },
        async getLocations() {
            let r = await axios.get(countryNameJson);
            r = r.data;
            let c = Object.keys(r);
            this.$refs.inputautocompletefield.updateItems(c);
        },

    }
    ,
    mounted() {
        this.getLocations();

        this.$refs.inputautocompletefield.setPlaceholder("type portfolio");

    }
}
</script>