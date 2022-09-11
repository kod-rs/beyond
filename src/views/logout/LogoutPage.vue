<template>

    <BasePublicTemplate>

        <div class="d-flex align-items-center mb-3 pb-1">
            <i class="fas fa-cubes fa-2x me-3" style="color: #ff6219;"></i>
            <div class="h1 fw-bold mb-0">
                <div class="text-right">
                    Goodbye
                </div>
            </div>
        </div>

    </BasePublicTemplate>

</template>


<script>
import BasePublicTemplate from "@/components/BasePublicTemplate.vue";
import { router } from '../../router/router';
import { apiAuth } from '../../scripts/api/auth';

export default {
    data() {
        return {};
    },
    async created() {
        apiAuth.logout();
        this.returnUrl = this.$route.query.returnUrl || '/';
        await new Promise(r => setTimeout(r, 2000)).then(() => {
            router.push(this.returnUrl);

        });

    },
    components: { BasePublicTemplate }

};
</script> 