import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    loggedIn: false,
    accessToken: '',
    backendUrl: 'http://127.0.0.1:5000',
  },
  mutations: {
    setLoggedInStatus(state, status) {
      state.loggedIn = status;
    },
    setAccessToken(state, accessToken) {
      state.accessToken = accessToken;
    },
  },
  actions: {
  },
  modules: {
  },
});
