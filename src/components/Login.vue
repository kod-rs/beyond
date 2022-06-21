<template>

  <div>

    <br>
        beyond 

    <form id="app" @submit="checkForm" action="/dashboard" method="post">
        
        <p v-if="errors.length">
            
            <b>{{errorHeader}}</b>
            
            <ul>
                <li v-for="error in errors" v-bind:key="error">{{ error }}</li>
            </ul>
       
        </p>


        <p>
            <p>
                Hello {{ username }}
            </p>
            
            <input type="text" v-model="username" placeholder="Username" />

        </p>

        <p>
           <input type="text" name="password" id="password" v-model="password" placeholder="Password">
        </p>

        <p>
            <input type="submit" value="Submit">  
        </p>

    </form>

    <!-- <router-link to="/dashboard">
    </router-link>  -->


  </div>
</template>

<script>

    export default {
    
        data() {
        
            return {
                errorHeader: "",
                errors:[],
                username:'',
                password:null,
                role: null,
        
                subject: "",
                msgBody: "",
            
            }
        },


        methods:{


            checkForm:function(e) {
            if(this.username && this.password) return true;

            this.errors = [];
            if(!this.username) this.errors.push("Username can not be empty.");
            if(!this.password) this.errors.push("Password can not be empty.");
            
            if (this.errors.length > 1) {
                this.errorHeader = "Please correct the following errors:"
            } else if (this.errors.length == 1) {
                this.errorHeader = "Please correct the following error:"
            } else {
                this.errorHeader = ""
            }
            
            e.preventDefault();
            }
        }
    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#app {
    background-color: lightblue;
}

</style>



