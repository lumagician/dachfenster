<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <v-card>
        <v-card-title class="headline">
	{{ fahrtSuchen }}
        </v-card-title>
        <v-card-text>
	<p>Von nach</p>
    <button v-on:click="searchRoutes">Suchen</button>
    <p>{{ results }}</p>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>
<script>
export default {
    setup() {
        
    },
    data() {
        return {
            fahrtSuchen: 'Fahrt suchen',
            results: 'None'
        };
    },
    methods: {
        searchRoutes: function () {
            this.results = '3 results found';
        }
    }
};
</script>

