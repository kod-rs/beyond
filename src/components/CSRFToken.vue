<template>
    <input hidden :value="content" @change="updateMyValue" />
</template>

<script>

import { apiCsrf } from '../scripts/api/csrf';

export default {
    data() {
        return {
            content: '',
        }
    },
    async mounted() {
        const r = await apiCsrf.getCSRFAuthData();
        if (r["auth"]["status"]) {

            this.content = r["payload"]["synchronizer_token"]
            this.$store.commit('setSynchronizerToken', this.content)

        } else {

            this.content = ""
            this.$store.commit('setSynchronizerToken', '')

            alert("error generating SynchronizerToken, you will not be able to submit form, contact admin")
        }
    },
    methods: {
        async refresh() {
            const r = await apiCsrf.getCSRFAuthData();
            if (r["auth"]["status"]) {

                this.content = r["payload"]["synchronizer_token"]
                this.$store.commit('setSynchronizerToken', this.content)

            } else {

                this.content = ""
                this.$store.commit('setSynchronizerToken', '')

                alert("error generating SynchronizerToken, you will not be able to submit form, contact admin")
            }

        },

        updateMyValue(event) {
            this.content = event.target.value.trim()
            this.$store.commit('setSynchronizerToken', this.content)
        }
    }
};
</script>
