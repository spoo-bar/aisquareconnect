<template>
  <div id="app">
    <Navbar />
    <div class="container">
      <template v-if="this.$store.state.loggedIn">
        <ProcessData />
      </template>
      <template v-else>
        <LoginForm />
      </template>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import LoginForm from './components/LoginForm.vue';
import Navbar from './components/Navbar.vue';
import ProcessData from './components/ProcessData.vue';

@Component({
  components: {
    LoginForm,
    Navbar,
    ProcessData,
  },
})
export default class App extends Vue {}
</script>

<style>
.container {
  margin-top: 100px;
}
</style>
