<template>

    <div>
        <div v-for="(f, index) in fields" :key="f">
            <InputField :reset="f.reset" :placeholder="index" v-model="f.value" :id="index"
                :validationMessage="f.validationMessage" :showValidationMessage="f.initShowValidationMessage"
                :validationRegex="f.validationRegex" :autocompleteContent="f.autocomplete" />

        </div>

        <!-- {{ fields }} -->
    </div>

</template>

<script>
import { apiPortfolio } from '@/scripts/api/portfolio';
import InputField from './InputField.vue';

export default {
    components: {
        InputField
    },
    data() {
        return {
            fields: {
                "Section": {
                    "value": "",
                    "validationMessage": "Only letters, numbers, spaces, commas and dots accepted in the input",
                    "showValidationMessage": false,
                    "validationRegex": /^(\w|,|\.| )*$/,
                    "reset": false,
                    "autocomplete": undefined
                },
                "Type": {
                    "value": "",
                    "validationMessage": "Only letters, numbers, spaces, commas and dots accepted in the input",
                    "showValidationMessage": true,
                    "validationRegex": /^(\w|,|\.| )*$/,
                    "reset": false,
                    "autocomplete": undefined

                },

                // todo create new portfolio if entered does not exist
                // check if manager and show error mesage else ask for confirmation
                "Portfolio": {
                    "value": "",
                    "validationMessage": "Only letters, numbers, spaces, commas and dots accepted in the input",
                    "showValidationMessage": true,
                    "validationRegex": /^(\w|,|\.| )*$/,
                    "reset": false,
                    "autocomplete": undefined,
                },

                // "Latitude": {
                //     "value": "",
                //     "validationMessage": "Only coordinates (float)",
                //     "showValidationMessage": false,
                //     "validationRegex": /^[+-]?\d+(\.\d+)?$/
                // },
                // "Longitude": {
                //     "value": "",
                //     "validationMessage": "Only coordinates (float)",
                //     "showValidationMessage": false,
                //     "validationRegex": /^[+-]?\d+(\.\d+)?$/
                // },
            },


        }
    },
    async created() {
        this.fields["Portfolio"]["autocomplete"] = await this.getDataFromApi()
    },
    methods: {
        async getDataFromApi() {
            let r = await apiPortfolio.getPortoflios();

            if (r["auth"]["status"]) {
                let pl = r["payload"]["portfolios"];

                let c = new Set(Object.keys(pl));
                console.log(c);

                return c;
                // this.$refs.inputautocompletefield.updateItems(c);
            }

            return undefined;

            // let t = new Set();
            // t.add("aaa");
            // t.add("bvvv");
            // t.add("cccc");
            // console.log(typeof (t));
            // return t;

            // this.loading = true
            // axios.get('/youApiUrl')
            //     .then(response => {
            //         this.loading = false
            //         this.rows = response.data
            //     })
            //     .catch(error => {
            //         this.loading = false
            //         console.log(error)
            //     })
        }
    },
    mounted() {
        // let t = new Set();
        // t.add("aaa");
        // t.add("bvvv");
        // t.add("cccc");

    },

    // methods: {
    //     async getPortfolioAutocomplete() {

    //     }


    // },


}
</script>

