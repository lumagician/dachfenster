<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <v-card>
        <v-card-title class="headline">
	{{ title }}
        </v-card-title>
        <v-card-text>
	<p>Von {{ homeAddress.street }}, {{ homeAddress.zipCode }} {{ homeAddress.city }} <br />
    Nach {{ workAddress.street }}, {{ workAddress.zipCode }} {{ workAddress.city }}
    </p>
    <v-btn color="primary" v-on:click="searchRoutes">Suchen</v-btn>
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
            title: 'Passagier - Mitfahrgelegenheiten',
            results: 'None',
            homeAddress: {
                street: 'Guisanstr. 2',
                zipCode: '3014',
                city: 'Bern'
            },
            workAddress: {
                street: 'Maritzstrasse 20',
                zipCode: '3400',
                city: 'Burgdorf'
            }
        };
    },
    methods: {
        searchRoutes: async function () {
            const resultPromise = new Promise((resolve, reject) => {
                setTimeout(() => {
                    resolve('24 results found.');
                }, 5 * 1000);
            });
            this.results = await resultPromise;
        }
    }
};
</script>

