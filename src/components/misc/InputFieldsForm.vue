<template>

    <div>
        <div v-for="(f, index) in fields" :key="f">
            <InputField v-model="f.value" :id="index" :validationMessage="f.validationMessage"
                :showValidationMessage="f.initShowValidationMessage" :validationRegex="f.validationRegex" /> {{
                        f.value
                }}
        </div>

        {{ fields }}
    </div>

</template>

<script>
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
                    "validationRegex": /^(\w|,|\.| )*$/
                },
                "Type": {
                    "value": "",
                    "validationMessage": "Only letters, numbers, spaces, commas and dots accepted in the input",
                    "showValidationMessage": true,
                    "validationRegex": /^(\w|,|\.| )*$/
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

    methods: {



    },


}
</script>

