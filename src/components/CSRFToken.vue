<template>
    <!-- <input type="hidden" name="csrf-token" value={{}} /> -->

    <!-- one way binding -->
    <!-- <input name="csrf-token" :value=content /> -->

    <!-- two way binding -->
    <input name="csrf-token" v-model=content />
    <br>

</template>

<script>
import { userService } from '../_services';

export default {
    data() {
        return {
            content: ''
        }
    },
    async mounted() {
        this.$store.commit('increment')
        console.log(this.$store.state.count)
        console.log("-")
        const CSRFPayload = await userService.getCSRFAuthData();

        if (CSRFPayload["status"]) {
            this.content = CSRFPayload["synchronizer_token"]

        } else {
            // error generating, user will not be able to submit form
            this.content = ""
        }
    }
};
</script>
