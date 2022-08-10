<template>
    <section class="vh-100" style="background-image: url('login_bg.jpg');">
        <div class="container py-5 h-100">
            <div class="row d-flex justify-content-center align-items-center h-100">
                <div class="col col-xl-10">
                    <div class="card" style="border-radius: 1rem;">
                        <div class="row g-0">
                            <div class="col-md-6 col-lg-5 d-none d-md-block">


                                <img src="login_profile.jpg" alt="login form" class="img-fluid"
                                    style="border-radius: 1rem 0 0 1rem;" />

                            </div>
                            <div class="col-md-6 col-lg-7 d-flex align-items-center">
                                <div class="card-body p-4 p-lg-5 text-black">

                                    <div class="d-flex align-items-center mb-3 pb-1">
                                        <i class="fas fa-cubes fa-2x me-3" style="color: #ff6219;"></i>
                                        <div class="h1 fw-bold mb-0">
                                            <div class="text-right">
                                                Goodbye
                                            </div>
                                        </div>
                                    </div>
                                    <div v-if="error" class="alert alert-danger">{{ error }}</div>



                                </div>
                            </div>


                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>




<script>
import { router } from '../../scripts/router';
import { apiCalls } from '../../scripts/api';

export default {
    data() {

    },
    async created() {
        apiCalls.logout();
        this.returnUrl = this.$route.query.returnUrl || '/';
        await new Promise(r => setTimeout(r, 2000)).then(r => {
            router.push(this.returnUrl);

        });

    },

};
</script> 