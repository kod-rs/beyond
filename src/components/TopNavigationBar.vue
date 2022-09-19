<template>
  <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
    <div class="container-fluid">
      <TopNavigationBarName></TopNavigationBarName>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarCollapse"
        aria-controls="navbarCollapse"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarCollapse">
        <ul class="navbar-nav me-auto mb-2 mb-md-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'portfolio' }"
              >Portfolio</router-link
            >
            <!-- <a class="nav-link" href="#">Link</a> -->
          </li>
        </ul>

        <router-link class="nav-link" :to="{ name: 'portfolio' }"
          >Portfolio</router-link
        >

        <router-link :to="{ name: 'login' }">test_login</router-link> |
        <!-- <router-link :to="{ name: 'portfolio' }">manage portfolio</router-link> -->
        | <router-link :to="{ name: 'test' }">test_test</router-link> |
        <router-link :to="{ name: 'history' }">todo_history</router-link> |
      </div>

      <TopNavigationBarUser></TopNavigationBarUser>
    </div>
  </nav>
</template>

<script>
import TopNavigationBarName from "./TopNavigationBarName.vue";
import TopNavigationBarUser from "./TopNavigationBarUser.vue";
export default {
  data() {
    return {};
  },
  components: { TopNavigationBarName, TopNavigationBarUser },
};
</script>

<style>
</style>
