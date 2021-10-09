<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <v-card>
        <v-card-title class="headline">
	{{ title }}
        </v-card-title>
        <v-card-text>
          <button class='fieldFromTo'>Von</button>
          <input type='text' name='street' id='fromAdress' v-model='homeAddress' class='inputValueFromTo inputValue'><br>
          <button class='fieldFromTo'>Nach</button>
          <input type='text' name='street' id='toAdress' v-model='workAddress' class='inputValueFromTo inputValue'>
<br >

    <v-btn style='margin-top:2rem;' color="primary" v-on:click="searchRoutes">Suchen</v-btn>


    <v-list>
        <v-list-item
          v-for="(item, i) in results"
          :key="i"
        >
          <v-list-item-avatar>
            <v-icon>mdi-account</v-icon>
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
            <v-list-item-subtitle>

              {{ item.description }}, {{ item.goodies }}
            </v-list-item-subtitle>
          </v-list-item-content>
          <v-list-item-action>
            <v-btn color="primary" v-on:click="selectRow">Anfragen</v-btn>
          </v-list-item-action>
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
            homeAddress: 'Guisanstr. 2, 3014 Bern',
            workAddress: 'Maritzstrasse 20, 3400 Burgdorf'
        };
    },
    async fetch() {
        let userName = 'Kowalski';
        if (process.client) {
            userName = localStorage.getItem('username');
        }
        const response = await fetch('/api/GetRoute?name=' + userName);
        const route = await response.json();
        this.homeAddress = `${route.startAddress.street}, ${route.startAddress.zipCode} ${route.startAddress.city}`;
        this.workAddress = `${route.destinationAddress.street}, ${route.destinationAddress.zipCode} ${route.destinationAddress.city}`;
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
        },
        selectRow: function (item) {
          this.$router.push({ name: 'passengerRequestSent', params: { driver: item.title } })
        }
    }
};
</script>

