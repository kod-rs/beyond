<template>
  <br />
  <hr />
  <br />
  <hr />
  <br />
  <hr />
  <br />
  <hr />
  <br />
  <hr />
  <br />
  <hr />

  <div class="container-fluid">
    <ui-table
      v-model="selectedRows"
      fullwidth
      :data="data"
      :thead="thead"
      :tbody="tbody"
      :tfoot="tfoot"
      row-checkbox
      selected-key="id"
    >
      <template #th-dessert> Dessert </template>
      <template #dessert="{ data }">
        <div class="dessert">{{ data.dessert }}</div>
      </template>
      <template #actions="{ data }">
        <ui-icon @click="show(data)">description</ui-icon>
        <ui-icon @click="show(data)">edit</ui-icon>
        <ui-icon @click="show(data)">delete</ui-icon>
      </template>

      <ui-pagination
        v-model="page"
        :total="total"
        show-total
        @change="onPage"
      ></ui-pagination>
    </ui-table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      data: [],
      thead: [
        {
          value: "ID",
          sort: "asc",
          columnId: "id",
        },
        {
          slot: "th-dessert",
          class: "good",
          sort: "none",
          columnId: "dessert",
        },
        "Section",
        "Type",
        "Location",
        "Update",
        "Delete",
      ],
      tbody: [
        "id",
        {
          slot: "dessert",
        },
        {
          field: "calories",
          numeric: true,
          class: "test",
        },
        {
          field: "fat",
          fn: (data) => {
            return data.fat.toFixed(1);
          },
        },
        "carbs",
        {
          field: "protein",
          class: (data) => {
            return data.protein > 5 ? "red" : "green";
          },
        },
        {
          slot: "actions",
        },
      ],
      tfoot: [
        {
          field: "id",
          fnName: "count",
        },
        null,
        {
          field: "calories",
          fnName: "sum",
          align: "right",
          class: "test",
        },
        {
          field: "fat",
          fnName: "avg",
        },
        {
          field: "carbs",
          fnName: "max",
        },
        {
          field: "protein",
          fnName: "min",
        },
      ],
      selectedRows: [],
      page: 1,
      total: 12,
    };
  },
  async created() {
    this.data = [
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
    ];
    // let { data } = await this.$http.get("/api/getData");
    // this.data = { l1: { id: 1, dessert: "d", calories: 1 } };
  },
  methods: {
    show(data) {
      console.log(data);
    },
    onPage(page) {
      // your code
      console.log("on page", page);
    },
  },
};
</script>
