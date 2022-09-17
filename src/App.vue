<template>
  <div>
    <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Beyond</a>
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
              <a class="nav-link" href="#">Link</a>
            </li>
            <li class="nav-item">
              <a
                class="nav-link disabled"
                href="#"
                tabindex="-1"
                aria-disabled="true"
                >Disabled</a
              >
            </li>
          </ul>

          <router-link :to="{ name: 'login' }">login</router-link> |
          <router-link :to="{ name: 'index' }">home</router-link> |
          <router-link :to="{ name: 'addlocation' }">Create</router-link> |
          <router-link :to="{ name: 'portfolio' }"
            >manage portfolio</router-link
          >
          | <router-link :to="{ name: 'test' }">test</router-link> |
          <router-link :to="{ name: 'history' }">history</router-link> |
          <router-link :to="{ name: 'settings' }">settings</router-link> |
          <router-link to="/logout">Logout</router-link> |

          <form class="d-flex">
            <input
              class="form-control me-2"
              type="search"
              placeholder="Search"
              aria-label="Search"
            />
            <button class="btn btn-outline-success" type="submit">
              Search
            </button>
          </form>
        </div>
      </div>
    </nav>

    <div class="nonscrollable">
      <router-view> </router-view>
    </div>
  </div>
</template>

<style>
html,
body {
  margin: 0;
  height: 100%;
  overflow: hidden;
}

/* Show it is fixed to the top */
body {
  min-height: 75rem;
  /* padding-top: 4.5rem; */
  padding-top: 3.5rem;
}

@import "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css";
@import "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.1/font/bootstrap-icons.css";
@import "https://cdn.jsdelivr.net/npm/@mdi/font@5.8.55/css/materialdesignicons.min.css";
@import "https://use.fontawesome.com/releases/v5.2.0/css/all.css";
@import "balm-ui/dist/balm-ui.css";
</style>

<script>
import { router } from "./router/router";
import { INACTIVE_THRESHOLD, TIME_RESOLUTION } from "./scripts/constants";

import { activate_tab_name_changer } from "./scripts/tab_name_changer";
import { apiAuth } from "./scripts/api/auth";
// import TestNavigation from "./components/TestNavigation.vue";

export default {
  name: "app",
  // components: { TestNavigation },
  data() {
    return {
      isPublic: sessionStorage.getItem("user") !== null,
      isInactive: false,
      userActivityThrottlerTimeout: null,
      userActivityTimeout: null,
      type: 1,
    };
  },
  mounted() {
    this.importScript(
      "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
    );
    this.importScript(
      "https://cdn.jsdelivr.net/npm/chart.js@3.0.2/dist/chart.min.js"
    );
    this.importScript("https://code.jquery.com/jquery-3.5.1.slim.min.js");
    // this.importScript("https://cdn.datatables.net/1.12.1/js/jquery.dataTables.min.js");

    activate_tab_name_changer();
  },

  methods: {
    setIsPublic() {},
    importScript(path) {
      let scriptElement = document.createElement("script");
      scriptElement.setAttribute("src", path);
      document.head.appendChild(scriptElement);
    },

    activateActivityTracker() {
      window.addEventListener("mousemove", this.userActivityThrottler);
      window.addEventListener("scroll", this.userActivityThrottler);
      window.addEventListener("keydown", this.userActivityThrottler);
      window.addEventListener("resize", this.userActivityThrottler);
    },

    deactivateActivityTracker() {
      window.removeEventListener("mousemove", this.userActivityThrottler);
      window.removeEventListener("scroll", this.userActivityThrottler);
      window.removeEventListener("keydown", this.userActivityThrottler);
      window.removeEventListener("resize", this.userActivityThrottler);
    },

    resetUserActivityTimeout() {
      clearTimeout(this.userActivityTimeout);

      this.userActivityTimeout = setTimeout(() => {
        this.userActivityThrottler();
        this.inactiveUserAction();
      }, INACTIVE_THRESHOLD);
    },

    userActivityThrottler() {
      if (this.isInactive) {
        this.isInactive = false;
      }

      if (!this.userActivityThrottlerTimeout) {
        this.userActivityThrottlerTimeout = setTimeout(() => {
          this.resetUserActivityTimeout();
          clearTimeout(this.userActivityThrottlerTimeout);
          this.userActivityThrottlerTimeout = null;
        }, TIME_RESOLUTION);
      }
    },

    inactiveUserAction() {
      if (window.location.href.endsWith("login")) {
        return;
      }
      apiAuth.logout();
      router.push("login");
      this.isInactive = true;
    },
  },

  beforeMount() {
    this.activateActivityTracker();
  },

  beforeUnmount() {
    this.deactivateActivityTracker();
    clearTimeout(this.userActivityTimeout);
    clearTimeout(this.userActivityThrottlerTimeout);
    window.sessionStorage.removeItem("user");
  },
};
</script>