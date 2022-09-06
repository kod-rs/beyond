<template>

    <PublicBase>
        <LoginForm></LoginForm>
        <Links></Links>
    </PublicBase>

</template>


<script>
import LoginForm from "../../components/login/LoginForm.vue";
import PublicBase from "../../components/login/PublicBase.vue";
import Links from "@/components/login/Links.vue";

export default {
    data() {
        return {};
    },
    components: { LoginForm, PublicBase, Links }
};
</script> 
