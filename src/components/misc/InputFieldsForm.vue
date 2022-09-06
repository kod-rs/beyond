<template>

    <div>
        <h1>tmp</h1>
        <div v-for="(f, index) in fields" :key="f">
            <InputField v-model="f.value" :id="index" :validationMessage="f.validationMessage"
                :showValidationMessage="f.initShowValidationMessage" :customValidationRegex="f.validationRegex" /> {{
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
                    "validationRegex": ""
                },
                "Type": {
                    "value": "",
                    "validationMessage": "Only letters, numbers, spaces, commas and dots accepted in the input",
                    "showValidationMessage": true,
                    "validationRegex": ""
                },
                "Latitude": {
                    "value": "",
                    "validationMessage": "float",
                    "showValidationMessage": false,
                    "validationRegex": ""
                },
                "Longitude": {
                    "value": "",
                    "validationMessage": "float",
                    "showValidationMessage": false,
                    "validationRegex": ""
                },
            },


        }
    },

    methods: {



    },


}
</script>

