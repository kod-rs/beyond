<template>

  <div id="app">

    <router-view>
    </router-view>

  </div>

</template>

<style>
</style>

<script>

import { router } from '../_helpers';
import {
  INACTIVE_THRESHOLD,
  TIME_RESOLUTION
} from '../_helpers/constants';

import { userService } from '../_services';


export default {
  name: 'app',

  data() {
    return {
      isInactive: false,
      userActivityThrottlerTimeout: null,
      userActivityTimeout: null
    };
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
      userService.logout();
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