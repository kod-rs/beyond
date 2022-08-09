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

                                <!-- <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/img1.webp"
                                    alt="login form" class="img-fluid" style="border-radius: 1rem 0 0 1rem;" /> -->
                            </div>
                            <div class="col-md-6 col-lg-7 d-flex align-items-center">
                                <div class="card-body p-4 p-lg-5 text-black">

                                    <div class="d-flex align-items-center mb-3 pb-1">
                                        <i class="fas fa-cubes fa-2x me-3" style="color: #ff6219;"></i>
                                        <span class="h1 fw-bold mb-0">Logo
                                            <!-- <img src="login_logo.png" alt=""> -->
                                        </span>
                                    </div>
                                    <div v-if="error" class="alert alert-danger">{{ error }}</div>

                                    <form @submit.prevent="handleSubmit">


                                        <!-- <h5 class="fw-normal mb-3 pb-3" style="letter-spacing: 1px;">Sign into your
                                            account</h5> -->

                                        <div class="form-outline mb-4">
                                            <label class="form-label" for="form2Example17">Username</label>
                                            <input type="text" id="form2Example17" v-model="username"
                                                class="form-control form-control-lg"
                                                :class="{ 'is-invalid': submitted && !username }" />

                                            <div v-show="submitted && !username" class="invalid-feedback">
                                                Username is required</div>
                                        </div>

                                        <div class="form-outline mb-4">
                                            <label class="form-label" for="form2Example27">Password</label>
                                            <!-- <input type="password" id="form2Example27" v-model="password"
                                                class="form-control form-control-lg"  /> -->
                                            <input type="password" id="form2Example27" v-model="password"
                                                :class="{ 'is-invalid': submitted && !password }"
                                                class="form-control form-control-lg" />


                                            <div v-show="submitted && !password" class="invalid-feedback">
                                                Password is required</div>
                                        </div>

                                        <div class="pt-1 mb-4">

                                            <button class="btn btn-dark btn-lg btn-block"
                                                :disabled="loading">Login</button>

                                            <img v-show="loading"
                                                src="data:image/gif;base64,R0lGODlhEAAQAPIAAP///wAAAMLCwkJCQgAAAGJiYoKCgpKSkiH/C05FVFNDQVBFMi4wAwEAAAAh/hpDcmVhdGVkIHdpdGggYWpheGxvYWQuaW5mbwAh+QQJCgAAACwAAAAAEAAQAAADMwi63P4wyklrE2MIOggZnAdOmGYJRbExwroUmcG2LmDEwnHQLVsYOd2mBzkYDAdKa+dIAAAh+QQJCgAAACwAAAAAEAAQAAADNAi63P5OjCEgG4QMu7DmikRxQlFUYDEZIGBMRVsaqHwctXXf7WEYB4Ag1xjihkMZsiUkKhIAIfkECQoAAAAsAAAAABAAEAAAAzYIujIjK8pByJDMlFYvBoVjHA70GU7xSUJhmKtwHPAKzLO9HMaoKwJZ7Rf8AYPDDzKpZBqfvwQAIfkECQoAAAAsAAAAABAAEAAAAzMIumIlK8oyhpHsnFZfhYumCYUhDAQxRIdhHBGqRoKw0R8DYlJd8z0fMDgsGo/IpHI5TAAAIfkECQoAAAAsAAAAABAAEAAAAzIIunInK0rnZBTwGPNMgQwmdsNgXGJUlIWEuR5oWUIpz8pAEAMe6TwfwyYsGo/IpFKSAAAh+QQJCgAAACwAAAAAEAAQAAADMwi6IMKQORfjdOe82p4wGccc4CEuQradylesojEMBgsUc2G7sDX3lQGBMLAJibufbSlKAAAh+QQJCgAAACwAAAAAEAAQAAADMgi63P7wCRHZnFVdmgHu2nFwlWCI3WGc3TSWhUFGxTAUkGCbtgENBMJAEJsxgMLWzpEAACH5BAkKAAAALAAAAAAQABAAAAMyCLrc/jDKSatlQtScKdceCAjDII7HcQ4EMTCpyrCuUBjCYRgHVtqlAiB1YhiCnlsRkAAAOwAAAAAAAAAAAA==" />

                                        </div>

                                    </form>

                                    <div class="misc">
                                        <a class="small text-muted" href="#!">Forgot password?</a>
                                        <br>
                                        <!-- <p class="mb-5 pb-lg-2" style="color: #393f81;">Don't have an account? <a
                                                href="#!" style="color: #393f81;">Register here</a></p> -->
                                        <a href="#!" class="small text-muted">Terms of use</a>
                                        <br>
                                        <a href="#!" class="small text-muted">Privacy policy</a>

                                    </div>

                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>


<style>
#fmaswe {
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}
</style>


<script>
import { router } from '../../scripts/router';
import { apiCalls } from '../../scripts/api';

export default {
    data() {
        return {
            username: 'a',
            password: '',
            submitted: false,
            loading: false,
            returnUrl: '',
            error: ''
        }
    },
    created() {
        apiCalls.logout();
        this.returnUrl = this.$route.query.returnUrl || '/';
    },
    methods: {
        handleSubmit(e) {
            console.log("sub")
            this.submitted = true;
            const { username, password } = this;

            if (!(username && password)) {
                return;
            }
            this.loading = true;
            apiCalls.login(username, password).then(
                user => {
                    router.push(this.returnUrl);
                    this.$store.commit('setUsername', username);

                },
                error => {
                    this.error = "invalid credentials"
                    // this.error = error;
                    this.loading = false;
                }
            );
        }
    }
};
</script> 