<template>
    <div>
        <p>map placeholder</p>
        <!-- <h1>Hi {{user.firstName}}!</h1> -->

        <p>this is  index</p>

        <em v-if="users.loading">Loading users...</em>
        <ul v-if="users.length">
            <li v-for="user in users" :key="user.id">
                {{user.firstName + ' ' + user.lastName}}
            </li>
        </ul>
        <p>
            <router-link to="/login">Logout</router-link>
        </p>
    </div>
</template>

<script>
import { userService } from '../_services';

export default {
    data () {
        return {
            user: {},
            users: []
        }
    },
    created () {
        this.user = JSON.parse(localStorage.getItem('user'));
        this.users.loading = true;
        userService.getAll().then(users => this.users = users);
    }
};
</script>