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

<v-divider></v-divider>

    <v-list>
        <v-list-item
          v-for="(item, i) in results"
          :key="i"
        >
          <v-list-item-action>
            <v-icon>mdi-account</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
            <v-list-item-subtitle v-text="item.description" />
            <v-list-item-subtitle v-text="item.goodies" />
            <v-btn color="primary">Anfragen</v-btn>
          </v-list-item-content>
        </v-list-item>
      </v-list>
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
            results: [],
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
    async fetch() {
        let userName = 'Kowalski';
        if (process.client) {
            userName = localStorage.getItem('username');
        }
        const response = await fetch('/api/GetRoute?name=' + userName);
        const route = await response.json();
        this.homeAddress = route.startAddress;
        this.workAddress = route.destinationAddress;
    },
    fetchOnServer: false,
    methods: {
        searchRoutes: async function () {
            if (process.client) {
                const userName = localStorage.getItem('username') || 'sebug';
                const response = await fetch(`/api/ProposedDrivers?username=${userName}`);
                const proposedDrivers = await response.json();

                this.results = proposedDrivers;
            }
        }
    }
};
</script>

