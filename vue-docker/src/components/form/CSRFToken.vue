<template>
    <input type="hidden" :value="content" @change="updateMyValue" />
    <br>

</template>

<script>

import { apiCalls } from '../../scripts/api';

export default {
    data() {
        return {
            content: '',
        }
    },
    async mounted() {

        const CSRFPayload = await apiCalls.getCSRFAuthData();

        if (CSRFPayload["status"]) {
            this.content = CSRFPayload["synchronizer_token"]
            this.$store.commit('setSynchronizerToken', this.content)

        } else {
            this.content = ""
            this.$store.commit('setSynchronizerToken', '')
            alert("Error while generating. You will not be able to submit form, contact admin")
        }
    },
    methods: {
        updateMyValue(event) {
            this.content = event.target.value.trim()
            this.$store.commit('setSynchronizerToken', this.content)
        }
    }
};
</script>
