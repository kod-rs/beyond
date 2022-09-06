
<template>

    <div>

        <label :for="id">

            {{ id.charAt(0).toUpperCase() + id.slice(1) }}

        </label>
        <br>

        <input class="form-control" :value="modelValue" :key="id" :name="id"
            @input="$emit('update:modelValue', $event.target.value)" />
        <br>

        <div v-if="showValidationMessage">
            <br>
            <div class="alert alert-danger">
                {{ validationMessage }}
            </div>
        </div>

        <!-- todo -->
        <!-- <div v-if="submitted && !option.value" class="red">
            {{ option.key }} is required
        </div> -->


    </div>

</template>

<script>
export default {
    data() {
        return {
            showValidationMessage: false,
            re: undefined
        }
    },
    props: {
        modelValue: String,
        id: String,
        validationMessage: String,
        validationRegex: RegExp,

        initShowValidationMessage: Boolean,
    },
    mounted() {
        this.re = new RegExp(this.validationRegex, "g");
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

            return this.validationRegex.test(content);

        },
    },
}
</script>
    

