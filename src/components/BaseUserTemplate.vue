<template>
  <div id="">
    <w-app>
      <header>f</header>
      <w-flex grow>
        <aside>
          Nav menu
          <slot></slot>
        </aside>
        <main class="grow">
          Main content
          <slot></slot>
        </main>
      </w-flex>
      <footer>
        Footer
        <slot></slot>
      </footer>
    </w-app>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  components: {},
};
</script>

<style>
/* Demo styles - can be discarded. */
.w-app {
  padding: 4px;
  background-color: #fffeed;
}
footer,
aside,
main {
  margin: 4px;
  padding: 12px;
  text-transform: uppercase;
  color: #666;
  border: 1px solid rgba(0, 0, 0, 0.07);
}
footer {
  background-color: #e9f8fe;
  min-height: 60px;
}

header {
  /* margin: 4px; */
  /* padding: 12px; */
  /* text-transform: uppercase; */
  /* color: #666; */
  /* border: 1px solid rgba(0, 0, 0, 0.07); */
  /* background-color: #e9f8fe; */
  min-height: 60px;
}

aside {
  background-color: #422844;
}
main {
  background-color: #efffed;
}
</style>