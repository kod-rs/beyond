<template>
  <w-button class="px4" @click="dialog.show = true"> Open dialog </w-button>

  <w-dialog
    v-model="dialog.show"
    :fullscreen="dialog.fullscreen"
    :width="dialog.width"
    :persistent="dialog.persistent"
    :persistent-no-animation="dialog.persistentNoAnimation"
    title-class="primary-light1--bg white"
  >
    <AddContent></AddContent>
  </w-dialog>
</template>

<script>
import AddContent from "./AddContent.vue";
export default {
  data() {
    return {
      dialog: {
        show: false,
        fullscreen: false,
        persistent: false,
        persistentNoAnimation: false,
        width: 300,
      },
    };
  },
  components: { AddContent },
};
</script>

<style>
</style>