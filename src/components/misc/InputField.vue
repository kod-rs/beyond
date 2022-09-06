
<template>

    <div>

        <label :for="id">

            {{ id.charAt(0).toUpperCase() + id.slice(1) }}

        </label>
        <br>

        <input :value="modelValue" :key="id" :name="id" @input="$emit('update:modelValue', $event.target.value)" />
        <br>

        <div v-if="showValidationMessage">
            <br>
            <div class="alert alert-danger">
                {{ validationMessage }}
            </div>
        </div>

    </div>

</template>

<script>
export default {
    data() {
        return {
            showValidationMessage: false,
        }
    },
    props: {
        modelValue: String,
        id: String,
        validationMessage: String,
        validationRegex: String,

        initShowValidationMessage: Boolean,
    },
    mounted() {

        this.showValidationMessage = this.initShowValidationMessage

    },
    watch: {
        modelValue(newValue) {
            this.showValidationMessage = !this.validateInput(newValue)
        }
    },

    emits: ['update:modelValue'],
    methods: {

        validateInput(content) {

            if (content === "") {
                return false;
            }

            let re = /^(\w|,|\.| )*$/;
            return re.test(content);

        },
    },
}
</script>
    

