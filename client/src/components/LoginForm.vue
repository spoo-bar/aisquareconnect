<template>
  <div id="login-form">
    <b-card>
      <b-form>
      <b-form-group
        id="input-group-1"
        label="Username:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="username"
          required
          placeholder="Enter username"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Password:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="password"
          required
          type="password"
          placeholder="Enter password"
        ></b-form-input>
      </b-form-group>

      <b-button variant="primary" @click="login">Submit</b-button>
    </b-form>
    </b-card>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import axios from 'axios';

@Component
export default class LoginForm extends Vue {
  private username = 'user';

  private password = 'password';

  login() {
    const loginUrl = `${this.$store.state.backendUrl}/login`;
    axios.post(loginUrl, {
      username: this.username,
      password: this.password,
    }).then((response) => {
      const accessToken = response.data.access_token;
      this.$store.commit('setAccessToken', accessToken);
      this.$store.commit('setLoggedInStatus', true);
    }).catch((error) => {
      console.log(error);
    });
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
