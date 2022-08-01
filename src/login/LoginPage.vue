<!-- <template>
    <div>
        <div class="alert alert-info">
            alert
        </div>
        <h2>Login</h2>
        <form @submit.prevent="handleSubmit">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" v-model="username" name="username" class="form-control"
                    :class="{ 'is-invalid': submitted && !username }" />
                <div v-show="submitted && !username" class="invalid-feedback">Username is required</div>
            </div>
            <div class="form-group">
                <label htmlFor="password">Password</label>
                <input type="password" v-model="password" name="password" class="form-control"
                    :class="{ 'is-invalid': submitted && !password }" />
                <div v-show="submitted && !password" class="invalid-feedback">Password is required</div>
            </div>
            <div class="form-group">
                <button class="btn btn-primary" :disabled="loading">Login</button>
                <img v-show="loading"
                    src="data:image/gif;base64,R0lGODlhEAAQAPIAAP///wAAAMLCwkJCQgAAAGJiYoKCgpKSkiH/C05FVFNDQVBFMi4wAwEAAAAh/hpDcmVhdGVkIHdpdGggYWpheGxvYWQuaW5mbwAh+QQJCgAAACwAAAAAEAAQAAADMwi63P4wyklrE2MIOggZnAdOmGYJRbExwroUmcG2LmDEwnHQLVsYOd2mBzkYDAdKa+dIAAAh+QQJCgAAACwAAAAAEAAQAAADNAi63P5OjCEgG4QMu7DmikRxQlFUYDEZIGBMRVsaqHwctXXf7WEYB4Ag1xjihkMZsiUkKhIAIfkECQoAAAAsAAAAABAAEAAAAzYIujIjK8pByJDMlFYvBoVjHA70GU7xSUJhmKtwHPAKzLO9HMaoKwJZ7Rf8AYPDDzKpZBqfvwQAIfkECQoAAAAsAAAAABAAEAAAAzMIumIlK8oyhpHsnFZfhYumCYUhDAQxRIdhHBGqRoKw0R8DYlJd8z0fMDgsGo/IpHI5TAAAIfkECQoAAAAsAAAAABAAEAAAAzIIunInK0rnZBTwGPNMgQwmdsNgXGJUlIWEuR5oWUIpz8pAEAMe6TwfwyYsGo/IpFKSAAAh+QQJCgAAACwAAAAAEAAQAAADMwi6IMKQORfjdOe82p4wGccc4CEuQradylesojEMBgsUc2G7sDX3lQGBMLAJibufbSlKAAAh+QQJCgAAACwAAAAAEAAQAAADMgi63P7wCRHZnFVdmgHu2nFwlWCI3WGc3TSWhUFGxTAUkGCbtgENBMJAEJsxgMLWzpEAACH5BAkKAAAALAAAAAAQABAAAAMyCLrc/jDKSatlQtScKdceCAjDII7HcQ4EMTCpyrCuUBjCYRgHVtqlAiB1YhiCnlsRkAAAOwAAAAAAAAAAAA==" />
            </div>
            <div v-if="error" class="alert alert-danger">{{ error }}</div>
        </form>
    </div>
</template>

<script>
import { router } from '../_helpers';
import { userService } from '../_services';

export default {
    data() {
        return {
            username: '',
            password: '',
            submitted: false,
            loading: false,
            returnUrl: '',
            error: ''
        }
    },
    created() {
        userService.logout();
        this.returnUrl = this.$route.query.returnUrl || '/';
    },
    methods: {
        handleSubmit(e) {
            this.submitted = true;
            const { username, password } = this;

            // stop here if form is invalid
            if (!(username && password)) {
                return;
            }
            this.loading = true;
            userService.login(username, password).then(
                user => router.push(this.returnUrl),
                error => {
                    this.error = "invalid credentials"
                    // this.error = error;
                    this.loading = false;
                }
            );
        }
    }
};
</script> -->

<template>

    <div id="main">
        <div id="fmaswe" style="background-image: url('electricity-3137843.jpg');">
            <!-- <section class="vh-100" style="background-color: #9A616D;"> -->
            <section class="vh-100">
                <div class="container py-5 h-100">
                    <div class="row d-flex justify-content-center align-items-center h-100">
                        <div class="col col-xl-10">
                            <div class="card" style="border-radius: 1rem;">
                                <div class="row g-0">
                                    <div class="col-md-6 col-lg-5 d-none d-md-block">
                                        <img src="cable-217169.jpg" alt="login form" class="img-fluid"
                                            style="border-radius: 1rem 0 0 1rem;" />
                                    </div>
                                    <div class="col-md-6 col-lg-7 d-flex align-items-center">
                                        <div class="card-body p-4 p-lg-5 text-black">

                                            <div class="d-flex align-items-center mb-3 pb-1">
                                                <i class="fas fa-cubes fa-2x me-3" style="color: #ff6219;"></i>
                                                <span class="h1 fw-bold mb-0">
                                                    <img src="logo.png" alt="">
                                                </span>
                                            </div>

                                            <h5 class="fw-normal mb-3 pb-3" style="letter-spacing: 1px;">Sign into
                                                your account</h5>

                                            <form @submit.prevent="handleSubmit">
                                                <div class="form-group">
                                                    <label for="username">Username</label>
                                                    <input type="text" v-model="username" name="username"
                                                        class="form-control"
                                                        :class="{ 'is-invalid': submitted && !username }" />
                                                    <div v-show="submitted && !username" class="invalid-feedback">
                                                        Username is required</div>
                                                </div>
                                                <div class="form-group">
                                                    <label htmlFor="password">Password</label>
                                                    <input type="password" v-model="password" name="password"
                                                        class="form-control"
                                                        :class="{ 'is-invalid': submitted && !password }" />
                                                    <div v-show="submitted && !password" class="invalid-feedback">
                                                        Password is required</div>
                                                </div>
                                                <div class="form-group">
                                                    <button class="btn btn-primary btn-dark btn-lg btn-block"
                                                        :disabled="loading">Login</button>


                                                    <img v-show="loading"
                                                        src="data:image/gif;base64,R0lGODlhEAAQAPIAAP///wAAAMLCwkJCQgAAAGJiYoKCgpKSkiH/C05FVFNDQVBFMi4wAwEAAAAh/hpDcmVhdGVkIHdpdGggYWpheGxvYWQuaW5mbwAh+QQJCgAAACwAAAAAEAAQAAADMwi63P4wyklrE2MIOggZnAdOmGYJRbExwroUmcG2LmDEwnHQLVsYOd2mBzkYDAdKa+dIAAAh+QQJCgAAACwAAAAAEAAQAAADNAi63P5OjCEgG4QMu7DmikRxQlFUYDEZIGBMRVsaqHwctXXf7WEYB4Ag1xjihkMZsiUkKhIAIfkECQoAAAAsAAAAABAAEAAAAzYIujIjK8pByJDMlFYvBoVjHA70GU7xSUJhmKtwHPAKzLO9HMaoKwJZ7Rf8AYPDDzKpZBqfvwQAIfkECQoAAAAsAAAAABAAEAAAAzMIumIlK8oyhpHsnFZfhYumCYUhDAQxRIdhHBGqRoKw0R8DYlJd8z0fMDgsGo/IpHI5TAAAIfkECQoAAAAsAAAAABAAEAAAAzIIunInK0rnZBTwGPNMgQwmdsNgXGJUlIWEuR5oWUIpz8pAEAMe6TwfwyYsGo/IpFKSAAAh+QQJCgAAACwAAAAAEAAQAAADMwi6IMKQORfjdOe82p4wGccc4CEuQradylesojEMBgsUc2G7sDX3lQGBMLAJibufbSlKAAAh+QQJCgAAACwAAAAAEAAQAAADMgi63P7wCRHZnFVdmgHu2nFwlWCI3WGc3TSWhUFGxTAUkGCbtgENBMJAEJsxgMLWzpEAACH5BAkKAAAALAAAAAAQABAAAAMyCLrc/jDKSatlQtScKdceCAjDII7HcQ4EMTCpyrCuUBjCYRgHVtqlAiB1YhiCnlsRkAAAOwAAAAAAAAAAAA==" />
                                                </div>
                                                <div v-if="error" class="alert alert-danger">{{ error }}</div>
                                            </form>


                                            <!-- <form @submit.prevent="handleSubmit"> -->



                                            <!-- <div class="form-outline mb-4">
                                                    <input type="email" id="form2Example17"
                                                        class="form-control form-control-lg" />
                                                    <label class="form-label" for="form2Example17">Email address</label>
                                                </div>

                                                <div class="form-outline mb-4">
                                                    <input type="password" id="form2Example27" class="form-control
                                                    form-control-lg" />
                                                    <label class="form-label" for="form2Example27">Password</label>
                                                </div> -->

                                            <!-- <div class="pt-1 mb-4">
                                                <button class="btn btn-dark btn-lg btn-block"
                                                    type="button">Login</button>
                                            </div> -->


                                            <!-- </form> -->

                                            <div>
                                                <a class="small text-muted" href="#!" style="color: #204375;">Forgot
                                                    password?</a>
                                                <p class="mb-5 pb-lg-2" style="color: #204375;">Don't have an
                                                    account? <a href="#!" style="color: #204375;">Register here</a>
                                                </p>
                                                <a href="#!" class="small text-muted">Terms of use.</a>
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

        </div>


    </div>

</template>

<style>
#main {
    border-style: dotted;
    /* width: 100%;
    height: inherit; */
    /* height: max-content; */
    /* border-color: 1px solid black;
    ; */
}

#fmaswe {
    /* background-image: url("./assets/electricity-3137843.jpg"); */
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}
</style>


<script>
import { router } from '../_helpers';
import { userService } from '../_services';

export default {
    data() {
        return {
            username: '',
            password: '',
            submitted: false,
            loading: false,
            returnUrl: '',
            error: ''
        }
    },
    created() {
        userService.logout();
        this.returnUrl = this.$route.query.returnUrl || '/';
    },
    methods: {
        handleSubmit(e) {
            this.submitted = true;
            const { username, password } = this;

            // stop here if form is invalid
            if (!(username && password)) {
                return;
            }
            this.loading = true;
            userService.login(username, password).then(
                user => router.push(this.returnUrl),
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