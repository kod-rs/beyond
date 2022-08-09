<template>
    <!-- <input type="hidden" name="csrf-token" value={{}} /> -->

    <!-- one way binding -->
    <!-- <input name="csrf-token" :value=content /> -->

    <!-- two way binding -->
    <!-- <input name="csrf-token" v-model=content onchange=changed() /> -->
    <input :value="content" @change="updateMyValue" />
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

            alert("error generating, you will not be able to submit form, contact admin")
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
