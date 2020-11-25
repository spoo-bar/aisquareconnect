<template>
  <div id="top-navbar">
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand href="#">Process CSV</b-navbar-brand>
    </b-navbar>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class Navbar extends Vue {}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
