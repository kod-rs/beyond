<template>
    <div>
        <div>
            enter location

        </div>

        <InputAutocomplete :ph="fromTimeWindow" @input="userTypedLocation" ref="inputautocompletefield" :initItems="[]">

        </InputAutocomplete>

        <button @click="buttonClicked">search</button>

    </div>
</template>

<script>
import InputAutocomplete from './../form/InputAutocomplete.vue';
import countryNameJson from "./../../assets/layers/country_names.json";
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
            console.log("search for location:", location)

        },
        userTypedLocation(location) {
            console.log("new location typed")
            console.log(location)
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

        this.$refs.inputautocompletefield.setPlaceholder("type location");

    }
}
</script>