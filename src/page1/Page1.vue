

<template>

    <div>
        test crud

        <form @submit.prevent="handleSubmit">
            <div class="form-group">
                <label for="id">id</label>
                <input type="text" v-model="id" name="id" class="form-control"
                    :class="{ 'is-invalid': submitted && !id }" />
                <div v-show="submitted && !id" class="invalid-feedback">id is required</div>
            </div>

            <div class="form-group">
                <label for="newValue">new value</label>
                <input type="text" v-model="newValue" name="newValue" class="form-control"
                    :class="{ 'is-invalid': submitted && !newValue }" />
                <div v-show="submitted && !newValue" class="invalid-feedback">newValue is required</div>
            </div>

            <div class="form-group">
                <button class="btn btn-primary" :disabled="loading">save</button>
                <img v-show="loading"
                    src="data:image/gif;base64,R0lGODlhEAAQAPIAAP///wAAAMLCwkJCQgAAAGJiYoKCgpKSkiH/C05FVFNDQVBFMi4wAwEAAAAh/hpDcmVhdGVkIHdpdGggYWpheGxvYWQuaW5mbwAh+QQJCgAAACwAAAAAEAAQAAADMwi63P4wyklrE2MIOggZnAdOmGYJRbExwroUmcG2LmDEwnHQLVsYOd2mBzkYDAdKa+dIAAAh+QQJCgAAACwAAAAAEAAQAAADNAi63P5OjCEgG4QMu7DmikRxQlFUYDEZIGBMRVsaqHwctXXf7WEYB4Ag1xjihkMZsiUkKhIAIfkECQoAAAAsAAAAABAAEAAAAzYIujIjK8pByJDMlFYvBoVjHA70GU7xSUJhmKtwHPAKzLO9HMaoKwJZ7Rf8AYPDDzKpZBqfvwQAIfkECQoAAAAsAAAAABAAEAAAAzMIumIlK8oyhpHsnFZfhYumCYUhDAQxRIdhHBGqRoKw0R8DYlJd8z0fMDgsGo/IpHI5TAAAIfkECQoAAAAsAAAAABAAEAAAAzIIunInK0rnZBTwGPNMgQwmdsNgXGJUlIWEuR5oWUIpz8pAEAMe6TwfwyYsGo/IpFKSAAAh+QQJCgAAACwAAAAAEAAQAAADMwi6IMKQORfjdOe82p4wGccc4CEuQradylesojEMBgsUc2G7sDX3lQGBMLAJibufbSlKAAAh+QQJCgAAACwAAAAAEAAQAAADMgi63P7wCRHZnFVdmgHu2nFwlWCI3WGc3TSWhUFGxTAUkGCbtgENBMJAEJsxgMLWzpEAACH5BAkKAAAALAAAAAAQABAAAAMyCLrc/jDKSatlQtScKdceCAjDII7HcQ4EMTCpyrCuUBjCYRgHVtqlAiB1YhiCnlsRkAAAOwAAAAAAAAAAAA==" />
            </div>
            <div v-if="error" class="alert alert-danger">{{ error }}</div>
        </form>

        <li v-for="(item, index) in items">
            {{ "a" }} - {{ index }} - {{ item }}
        </li>

    </div>
</template>

<script>
import { router } from '../_helpers';
import { userService } from '../_services';

export default {
    data() {
        return {
            id: '',
            newValue: '',
            submitted: false,
            loading: false,
            error: '',
            items: []
        }
    },
    created() {
        this.error = "current: "
        this.items = [{ message: 'Foo' }, { message: 'Bar' }]
    },
    methods: {
        handleSubmit(e) {
            this.submitted = true;
            const { id, newValue } = this;

            // stop here if form is invalid
            if (!(id && newValue)) {
                return;
            }
            this.error = "saving"

            userService.createOrUpdate(id, newValue).then(
                r => {
                    console.log("crud done")
                    this.error = r["payload"]["result"]
                },


                error => {
                    this.error = "error"
                    // this.error = error;
                    this.loading = false;
                }
            );


            this.loading = false;


        }
    }
};
</script>