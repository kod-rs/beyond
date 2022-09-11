<template>
  <w-table
    :headers="table.headers"
    :items="table.items"
    fixed-headers
    :loading="loading"
    style="height: 200px"
  >
  </w-table>
</template>

<script>
export default {
  data: () => ({
    table: {
      headers: [
        { label: "ID", key: "id" },
        { label: "First name", key: "firstName" },
        { label: "Last name", key: "lastName" },
      ],
      items: [
        { id: 1, firstName: "Floretta", lastName: "Sampson" },
        { id: 2, firstName: "Nellie", lastName: "Lynn" },
        { id: 3, firstName: "Rory", lastName: "Bristol" },
        { id: 4, firstName: "Daley", lastName: "Elliott" },
        { id: 5, firstName: "Virgil", lastName: "Carman" },
        { id: 6, firstName: "Baldwin", lastName: "Morison" },
        { id: 7, firstName: "Beckah", lastName: "Mann" },
        { id: 8, firstName: "Davie", lastName: "Forester" },
        { id: 9, firstName: "Andi", lastName: "Montgomery" },
        { id: 10, firstName: "Magnolia", lastName: "Kirk" },
        { id: 11, firstName: "Hamilton", lastName: "Mallory" },
        { id: 12, firstName: "Sheree", lastName: "Castle" },
        { id: 13, firstName: "Rebekah", lastName: "Eason" },
        { id: 14, firstName: "Maude", lastName: "Hayley" },
        { id: 15, firstName: "Josie", lastName: "Richard" },
      ],
    },
    loading: true, // Set this to false when the data is loaded.
  }),

  mounted() {
    setTimeout(() => {
      this.loading = false;
    }, 3000);
  },
};
</script>

<style>
</style>