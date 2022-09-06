<template>

    <input v-if="this.$store.state.appMode == 'development'" :value="content" @change="updateMyValue" />
    <input v-else type="hidden" :value="content" @change="updateMyValue" />

    <br>

</template>

<script>

import { apiCsrf } from '../../scripts/api/csrf';

export default {
    data() {
        return {
            content: '',
        }
    },
    async mounted() {
        const CSRFPayload = await apiCsrf.getCSRFAuthData();

        if (CSRFPayload["auth"]["status"]) {
            this.content = CSRFPayload["synchronizer_token"]
            this.$store.commit('setSynchronizerToken', this.content)

        } else {
            this.content = ""
            this.$store.commit('setSynchronizerToken', '')

            alert("error generating SynchronizerToken, you will not be able to submit form, contact admin")
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
