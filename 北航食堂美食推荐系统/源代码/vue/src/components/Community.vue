<script lang="ts">
import {defineComponent} from 'vue'
import Waterfall from "@/components/Waterfall.vue";
import BottomBar from "@/components/BottomBar.vue";

export default defineComponent({
  name: "Community",
  components: {BottomBar, Waterfall}
})
</script>

<template>
  <Waterfall type="community" />
  <BottomBar active="community"/>
</template>

<style scoped>

</style>