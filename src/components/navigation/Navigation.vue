<template>

    <TopNavigationBar />
    <ContentNavigationBar />

</template>

<script>
import ContentNavigationBar from './ContentNavigationBar.vue';
import TopNavigationBar from './TopNavigationBar.vue';
export default {
    components: { ContentNavigationBar, TopNavigationBar }
}
</script>

