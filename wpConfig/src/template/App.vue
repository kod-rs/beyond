<template>

  <!-- <div :class="]"> -->
  <!-- <img v-if="infoLogoURL !== ''" :src="infoLogoURL" class="logo" alt="" @error="$event.target.src = '/favicon.ico'"> -->
  <!-- // v-else show your material icon -->
  <!-- </div> -->
  <!-- <md-icon >{{ infoSubIcon }}</md-icon> -->

  <TestNavigation></TestNavigation>

  <router-view>
  </router-view>



</template>

<script>

import { router } from './../scripts/router';
import {
  INACTIVE_THRESHOLD,
  TIME_RESOLUTION
} from './../scripts/constants';

import { apiCalls } from './../scripts/api';
import { activate_tab_name_changer } from "./../scripts/tab_name_changer";

export default {
  name: 'app',

  data() {
    return {
      isInactive: false,
      userActivityThrottlerTimeout: null,
      userActivityTimeout: null
    };
  },
  mounted() {
    activate_tab_name_changer();
  },

  methods: {
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

  beforeDestroy() {
    this.deactivateActivityTracker();
    clearTimeout(this.userActivityTimeout);
    clearTimeout(this.userActivityThrottlerTimeout);
    window.sessionStorage.removeItem('user');
  }
};
</script>