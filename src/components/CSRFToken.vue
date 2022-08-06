<template>
    <!-- <input type="hidden" name="csrf-token" value={{}} /> -->
    <!-- <input name="csrf-token" :value=content /> -->
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
        const CSRFPayload = await userService.getCSRFAuthData();

        if (CSRFPayload["status"]) {
            this.content = CSRFPayload["synchronizer_token"]

        } else {
            // error generating
            this.content = ""
        }
    }
};
</script>
