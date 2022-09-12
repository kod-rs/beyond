<template>
  <div>
    <header>Header</header>
    <w-flex grow>
      <aside>Nav menu</aside>
      <main class="grow">
        Main content

        <hr />

        <hr />
        <hr />
        <hr />
        <hr />
        <hr />
        <hr />
      </main>
    </w-flex>
    <footer>Footer</footer>
  </div>
</template>

<style>
/* Demo styles - can be discarded. */
/* .w-app {
  padding: 4px;
  background-color: #fffeed;
}
header,
footer,
aside,
main {
  margin: 4px;
  padding: 12px;
  text-transform: uppercase;
  color: #666;
  border: 1px solid rgba(0, 0, 0, 0.07);
}
header,
footer {
  background-color: #e9f8fe;
  min-height: 60px;
}
aside {
  background-color: #fef2ff;
}
main {
  background-color: #efffed;
} */
</style>

<script>
export default {
  name: "TestPag",
  data() {
    return {
      data: [
        {
          id: 1,
          dessert: "Frozen yogurt",
          calories: 159,
          fat: 6,
          carbs: 24,
          protein: 4,
        },
        {
          id: 2,
          dessert: "Ice cream sandwich",
          calories: 237,
          fat: 9,
          carbs: 37,
          protein: 4.3,
        },
        {
          id: 3,
          dessert: "Eclair",
          calories: 262,
          fat: 16,
          carbs: 24,
          protein: 6,
        },
      ],
      thead: [
        "ID",
        "Dessert (100g serving)",
        "Calories",
        "Fat (g)",
        "Carbs (g)",
        "Protein (g)",
      ],
      tbody: ["id", "dessert", "calories", "fat", "carbs", "protein"],
    };
  },
  methods: {
    downoladImage() {
      let text = `<svg width="120" height="120" version="1.1" xmlns="http://www.w3.org/2000/svg">
            <path d="M0 0h24v24H0z" fill="none"/>
            <path fill="#F1FA2B" d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z" />
        </svg>`;

      const win = window.URL || window.webkitURL || window;

      let img = new Image();
      img.src = win.createObjectURL(
        new Blob([text], { type: "image/svg+xml" })
      );

      img.onload = () => {
        let canvas = document.createElement("canvas");
        canvas.width = 120;
        canvas.height = 120;
        canvas.getContext("2d").drawImage(img, 0, 0);

        let a = document.createElement("a");
        a.href = canvas.toDataURL("octet/stream");
        console.log(a.href);
        a.download = "img.png";
        a.click();

        win.revokeObjectURL(img.src);
        win.revokeObjectURL(a.href);
      };
    },
  },
  mounted() {
    console.log("m");
  },
};
</script> 
