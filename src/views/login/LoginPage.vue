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
import { getMixedColors } from "../../scripts/common";

export default {
    data() {
        return {};
    },
    components: { LoginForm, PublicBase, Links },
    mounted() {
        console.log(getMixedColors(2))
    }
};
</script> 
