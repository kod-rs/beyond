<template>
  <w-button @click="showDialog"> Open dialog </w-button>

  <w-dialog
    v-model="dialog.show"
    :fullscreen="dialog.fullscreen"
    :width="dialog.width"
    :persistent="dialog.persistent"
    :persistent-no-animation="dialog.persistentNoAnimation"
    title-class="primary-light1--bg white"
  >
    <AddContent @added="addOk"></AddContent>
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
  methods: {
    addOk() {
      console.log("addd ok");
      this.dialog.show = false;
    },
    showDialog() {
      this.dialog.show = true;
    },
  },
  components: { AddContent },
};
</script>

<style>
</style>