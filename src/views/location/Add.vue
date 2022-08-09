<template>


    <div id="root">

        <Navigation />


        <main class="mt-5 pt-3">
            <div class="container-fluid">

                <div class="row">
                    add new
                    <br>
                    <hr>
                    <div class="hidden-csrf"><CSRFToken ref="csrftokenelement"/></div>
                    <form @submit.prevent="handleSubmit">


                        <div v-for="option in formData" :value="option.value">
                            {{ option.key.charAt(0).toUpperCase() + option.key.slice(1) }}
                            <span v-if="option.key == 'section' || option.key == 'type'">
                                <span class="hint" @mouseover="hover = true" @mouseleave="hover = false">?</span>
                                <span v-if="hover" class="hinttext">Only letters, numbers, spaces, commas and dots
                                    accepted in the input</span>
                            </span>

                            <input type="text" v-model="option.value" :name="option.key" class="form-control" />
                            <br>

                        </div>

                        <button class="btn btn-primary btn-dark btn-lg btn-block">add</button>
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
                { key: 'section', value: 'A' },
                { key: 'type', value: 'B' },
                { key: 'latitude', value: '2' },
                { key: "longitude", value: "3" }
            ]
        }
    },
    methods: {
        async handleSubmit() {

            let formContent = {};

            for (const element of this.formData) {

                if (element.value) {
                    formContent[element.key] = element.value

                } else {
                    return
                }
            }

            const csrfToken = this.$store.state.synchronizerToken

            await apiCalls.addLocation(formContent["section"], formContent["type"], formContent["latitude"], formContent["longitude"], csrfToken).then(
                t => {
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

.hinttext {
    background: #e3e3e3;
    color: #6e6e6e;
    display: inline;
    text-align: center;
}

.hidden-csrf {
    display: none;
}
</style>