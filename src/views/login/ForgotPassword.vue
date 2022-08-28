<template>

    <PublicBase>
        <ForgotPasswordForm></ForgotPasswordForm>
        <Links></Links>
    </PublicBase>

</template>


<script>
import PublicBase from "../../components/login/PublicBase.vue";
import ForgotPasswordForm from "@/components/login/ForgotPasswordForm.vue";
import Links from "@/components/login/Links.vue";

export default {
    data() {
        return {};
    },
    components: { PublicBase, ForgotPasswordForm, Links }
};
</script> 
