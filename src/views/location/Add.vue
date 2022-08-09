<template>

    <div id="root">

        <Navigation />

        <main class="mt-5 pt-3">
            <div class="container-fluid">

                <div class="row">
                    add new
                    <br>
                    <hr>
                    <div v-if="error" class="alert alert-danger">{{ error }}</div>

                    <form @submit.prevent="handleSubmit">
                        <CSRFToken ref="csrftokenelement" />

                        <div v-for="option in formData" :value="option.value">
                            {{ option.key.charAt(0).toUpperCase() + option.key.slice(1) }}
                            <span v-if="option.key == 'section' || option.key == 'type'">
                                <span class="hint" @mouseover="option.hovered = true"
                                    @mouseleave="option.hovered = false">?</span>
                                <span v-if="option.hovered" class="hint_text"> {{ option.msg }}</span>
                            </span>

                            <input type="text" v-model="option.value" :name="option.key" class="form-control" />

                            <div v-if="submitted && !option.value" class="red">
                                {{ option.key }} is required
                            </div>

                            <br>

                        </div>

                        <button class="btn btn-primary btn-dark btn-lg btn-block" :disabled="loading">add</button>

                        <img v-show="loading"
                            src="data:image/gif;base64,R0lGODlhEAAQAPIAAP///wAAAMLCwkJCQgAAAGJiYoKCgpKSkiH/C05FVFNDQVBFMi4wAwEAAAAh/hpDcmVhdGVkIHdpdGggYWpheGxvYWQuaW5mbwAh+QQJCgAAACwAAAAAEAAQAAADMwi63P4wyklrE2MIOggZnAdOmGYJRbExwroUmcG2LmDEwnHQLVsYOd2mBzkYDAdKa+dIAAAh+QQJCgAAACwAAAAAEAAQAAADNAi63P5OjCEgG4QMu7DmikRxQlFUYDEZIGBMRVsaqHwctXXf7WEYB4Ag1xjihkMZsiUkKhIAIfkECQoAAAAsAAAAABAAEAAAAzYIujIjK8pByJDMlFYvBoVjHA70GU7xSUJhmKtwHPAKzLO9HMaoKwJZ7Rf8AYPDDzKpZBqfvwQAIfkECQoAAAAsAAAAABAAEAAAAzMIumIlK8oyhpHsnFZfhYumCYUhDAQxRIdhHBGqRoKw0R8DYlJd8z0fMDgsGo/IpHI5TAAAIfkECQoAAAAsAAAAABAAEAAAAzIIunInK0rnZBTwGPNMgQwmdsNgXGJUlIWEuR5oWUIpz8pAEAMe6TwfwyYsGo/IpFKSAAAh+QQJCgAAACwAAAAAEAAQAAADMwi6IMKQORfjdOe82p4wGccc4CEuQradylesojEMBgsUc2G7sDX3lQGBMLAJibufbSlKAAAh+QQJCgAAACwAAAAAEAAQAAADMgi63P7wCRHZnFVdmgHu2nFwlWCI3WGc3TSWhUFGxTAUkGCbtgENBMJAEJsxgMLWzpEAACH5BAkKAAAALAAAAAAQABAAAAMyCLrc/jDKSatlQtScKdceCAjDII7HcQ4EMTCpyrCuUBjCYRgHVtqlAiB1YhiCnlsRkAAAOwAAAAAAAAAAAA==" />


                    </form>
                </div>

            </div>
        </main>

    </div>

</template>

<script>
import { apiCalls } from '../../scripts/api';

export default {
    data() {
        return {
            hover: false,
            formData: [
                { key: 'section', value: 'A', msg: "Only letters, numbers, spaces, commas and dots accepted in the input", hovered: false },
                { key: 'type', value: 'B', msg: "Only letters, numbers, spaces, commas and dots accepted in the input", hovered: false },
                { key: 'latitude', value: '2' },
                { key: "longitude", value: "3" }
            ]
        }
    },
    methods: {
        async handleSubmit() {
            this.submitted = true;
            this.error = ""

            let formContent = {};

            for (const element of this.formData) {

                if (element.value) {
                    formContent[element.key] = element.value

                } else {
                    this.error = "fields not filled"
                    return
                }
            }

            const csrfToken = this.$store.state.synchronizerToken

            await apiCalls.addLocation(formContent["section"], formContent["type"], formContent["latitude"], formContent["longitude"], csrfToken).then(
                _ => {
                    alert("added")
                },
                error => {
                    console.log("error", error)
                }
            );

            this.formData.forEach(i => {
                i.value = ""
            });

            this.$router.go()

            this.submitted = false;
        }
    }
};
</script> 


<style>
.hint {
    background: #e3e3e3;
    border-radius: 50%;
    color: #6e6e6e;
    display: inline-block;
    font-weight: bold;
    text-align: center;
    width: 1.2vw;
    height: 1.2vw;
}

.hint_text {
    background: #e3e3e3;
    color: #6e6e6e;
    display: inline;
    text-align: center;
}
</style>