<template>
  <v-container  class="d-flex justify-center">
    <v-card class="center pa-5" width="400px">
    <v-card-title>LOGIN</v-card-title>
    <v-form>
      <v-text-field v-model="username" label="Username"></v-text-field>
      <v-text-field label="Password" type="password"></v-text-field>
      <v-btn v-on:click="validateLoginCreds">login</v-btn>
    </v-form>
  </v-card>
  </v-container>
</template>

<script>
export default {
  setup() {},
  data() {
    return {
      username: '',
    }
  },
  methods: {
    validateLoginCreds: async function () {
      if (process.client) {
        localStorage.setItem('username', this.username)
      }
    },
  },
}
</script>