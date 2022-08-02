<!-- <template>

    <form @submit.prevent="handleSubmit">
        <div v-for="(item, i) in modelFields" :key="item.id" class="form-group">
            <div class="form-group">
                <label :for=item>{{ item }}</label>
                <input type="text" v-model="modelFields[i]" :name=item class="form-control"
                    :class="{ 'is-invalid': submitted && !item }" />
                <div v-show="submitted && !item" class="invalid-feedback">
                    {{ item }} is required</div>
            </div>
            <br>

        </div>

        <div class="form-group">
            <label for="username">Username</label>
            <input type="text" v-model="username" name="username" class="form-control"
                :class="{ 'is-invalid': submitted && !username }" />
            <div v-show="submitted && !username" class="invalid-feedback">
                Username is required</div>
        </div>
        <br>
        <div class="form-group">
            <label htmlFor="password">Password</label>
            <input type="password" v-model="password" name="password" class="form-control"
                :class="{ 'is-invalid': submitted && !password }" />
            <div v-show="submitted && !password" class="invalid-feedback">
                Password is required</div>
        </div>

        <br>
        <div class="form-group">
            <button class="btn btn-primary btn-dark btn-lg btn-block" :disabled="loading">Login</button>

            <img v-show="loading"
                src="data:image/gif;base64,R0lGODlhEAAQAPIAAP///wAAAMLCwkJCQgAAAGJiYoKCgpKSkiH/C05FVFNDQVBFMi4wAwEAAAAh/hpDcmVhdGVkIHdpdGggYWpheGxvYWQuaW5mbwAh+QQJCgAAACwAAAAAEAAQAAADMwi63P4wyklrE2MIOggZnAdOmGYJRbExwroUmcG2LmDEwnHQLVsYOd2mBzkYDAdKa+dIAAAh+QQJCgAAACwAAAAAEAAQAAADNAi63P5OjCEgG4QMu7DmikRxQlFUYDEZIGBMRVsaqHwctXXf7WEYB4Ag1xjihkMZsiUkKhIAIfkECQoAAAAsAAAAABAAEAAAAzYIujIjK8pByJDMlFYvBoVjHA70GU7xSUJhmKtwHPAKzLO9HMaoKwJZ7Rf8AYPDDzKpZBqfvwQAIfkECQoAAAAsAAAAABAAEAAAAzMIumIlK8oyhpHsnFZfhYumCYUhDAQxRIdhHBGqRoKw0R8DYlJd8z0fMDgsGo/IpHI5TAAAIfkECQoAAAAsAAAAABAAEAAAAzIIunInK0rnZBTwGPNMgQwmdsNgXGJUlIWEuR5oWUIpz8pAEAMe6TwfwyYsGo/IpFKSAAAh+QQJCgAAACwAAAAAEAAQAAADMwi6IMKQORfjdOe82p4wGccc4CEuQradylesojEMBgsUc2G7sDX3lQGBMLAJibufbSlKAAAh+QQJCgAAACwAAAAAEAAQAAADMgi63P7wCRHZnFVdmgHu2nFwlWCI3WGc3TSWhUFGxTAUkGCbtgENBMJAEJsxgMLWzpEAACH5BAkKAAAALAAAAAAQABAAAAMyCLrc/jDKSatlQtScKdceCAjDII7HcQ4EMTCpyrCuUBjCYRgHVtqlAiB1YhiCnlsRkAAAOwAAAAAAAAAAAA==" />
        </div>
        <br>
        <div v-if="error" class="alert alert-danger">{{ error }}</div>
    </form>


</template>

<script>

</script> -->


<template>

    location add form

    <form @submit.prevent="handleSubmit">
        section
        <input type="text" v-model="section" name="section" class="form-control" />
        type
        <input type="text" v-model="type" name="type" class="form-control" />
        latitude
        <input type="text" v-model="latitude" name="latitude" class="form-control" />
        longitude
        <input type="text" v-model="longitude" name="longitude" class="form-control" />



        <button class="btn btn-primary btn-dark btn-lg btn-block">add</button>
    </form>



</template>




<script>
import { router } from '../_helpers';
import { userService } from '../_services';

export default {
    data() {
        return {
            section: '',
            type: '',
            latitude: '',
            longitude: ''
        }
    },
    methods: {
        handleSubmit(e) {
            console.log("hello submit")
            // this.submitted = true;
            const { section, type, latitude, longitude } = this;



            if (!(section && type && latitude && longitude)) {
                console.log("form not filled")
                return;
            }
            // this.loading = true;
            userService.addLocation(section, type, latitude, longitude).then(
                t => {
                    this.accepted = true
                    alert("added")
                },
                error => {
                    console.log("error", error)
                }
            );
        }
    }
};
</script> 