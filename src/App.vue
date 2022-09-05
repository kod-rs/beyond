<template>

  <TestNavigation></TestNavigation>

  <router-view>
  </router-view>

</template>

<style>
@import "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css";
/* @import "//cdn.datatables.net/1.12.1/css/jquery.dataTables.min.css"; */
@import "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.1/font/bootstrap-icons.css";
</style>

<script>

import TestNavigation from './components/navigation/TestNavigation.vue';

import { router } from './scripts/router';
import {
  INACTIVE_THRESHOLD,
  TIME_RESOLUTION
} from './scripts/constants';

import { apiCalls } from './scripts/api';
import { activate_tab_name_changer } from "./scripts/tab_name_changer";

export default {
  name: 'app',
  components: { TestNavigation },
  data() {
    return {
      isInactive: false,
      userActivityThrottlerTimeout: null,
      userActivityTimeout: null
    };
  },
  mounted() {
    this.importScript("https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js");
    this.importScript("https://cdn.jsdelivr.net/npm/chart.js@3.0.2/dist/chart.min.js");
    this.importScript("https://code.jquery.com/jquery-3.5.1.slim.min.js");
    // this.importScript("https://cdn.datatables.net/1.12.1/js/jquery.dataTables.min.js");


    activate_tab_name_changer();
  },

  methods: {
    importScript(path) {
      let scriptElement = document.createElement('script')
      scriptElement.setAttribute('src', path)
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
      if (window.location.href.endsWith('login')) {
        return;
      }
      apiCalls.logout();
      router.push('login');
      this.isInactive = true;
    }
  },

  beforeMount() {
    this.activateActivityTracker();
  },

  beforeUnmount() {
    this.deactivateActivityTracker();
    clearTimeout(this.userActivityTimeout);
    clearTimeout(this.userActivityThrottlerTimeout);
    window.sessionStorage.removeItem('user');
  }
};
</script>