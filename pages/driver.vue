<template>
  <v-row justify='center' align='center'>
    <v-col cols='12' sm='8' md='6'>
      <v-card>
        <v-card-title class='headline'>
          {{ title }}
        </v-card-title>
          </v-card> <v-card>
        <v-card-text>
          <v-btn color='primary' v-on:click='openShareView'>Sharen</v-btn>
          <div style='padding-top: 2rem'></div>
          <span class="highlightFromTo">Akzeptierte Fahrten:</span>
          <v-simple-table>
            <template v-slot:default>
              <thead>
              <tr>
                <th class='text-left'>
                  Zeit
                </th>
                <th class='text-center'>
                  Berechnete Fahrzeit
                </th>
                <th class='text-center'>
                  Nickname
                </th>
              </tr>
              </thead>
              <tbody>
              <tr
                v-for='item in acceptedDrives'
                :key='item.dateString'
                @click='selectAcceptedRow(item.passengerNickname)'
              >
                <td>{{ item.dateString }}</td>
                <td class='centered'>{{ item.estimatedTimeInMinutes }} Minuten</td>
                <td class='centered'>{{ item.passengerNickname }} </td>
              </tr>
              </tbody>
            </template>
          </v-simple-table>
          <v-divider style='padding-top: 1.3rem'></v-divider>
          <span class="highlightFromTo">Pendente Fahrten:</span>
          <v-simple-table>
            <template v-slot:default>
              <thead>
              <tr>
                <th class='text-left'>
                  Zeit
                </th>
                <th class='text-center'>
                  Berechnete Fahrzeit
                </th>
                <th class='text-center'></th>
              </tr>
              </thead>
              <tbody>
              <tr
                v-for='item in pendingDrives'
                :key='item.dateString'
                @click='selectPendingRow()'
              >
                <td>{{ item.dateString }}</td>
                <td class='centered'>{{ item.estimatedTimeInMinutes }} Minuten</td>
                <td class='centered'><span v-if="item.requestExists">
                  <a>Vorschläge</a>
                </span> </td>
              </tr>
              </tbody>
            </template>
          </v-simple-table>
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
      title: 'Driver Home',
      results: [],
      acceptedDrives: [
        {
          dateString: 'Montag, Dienstag wöchentlich um 8:00',
          estimatedTimeInMinutes: 20,
          passengerNickname: 'alex'
        },
        {
          dateString: 'Mittwoch wöchentlich um 16:00',
          estimatedTimeInMinutes: 30,
          passengerNickname: 'marty'
        }
      ],
      pendingDrives: [
        {
          dateString: 'Montag, Dienstag wöchentlich um 8:00',
          estimatedTimeInMinutes: 20,
          requestExists: true
        },
        {
          dateString: 'Mittwoch wöchentlich um 16:00',
          estimatedTimeInMinutes: 45,
          requestExists: false
        }
      ]
    }

  },
  fetchOnServer: false,
  async fetch() {
      let userName = 'Kowalski';
      if (process.client) {
          userName = localStorage.getItem('username');
      }
      const response = await fetch('/api/DriverPendingRoutes?username=' + userName);
      const route = await response.json();
      console.log(route);
  },
  methods: {
    selectAcceptedRow(nickname) {
      if (process.client) {
      let username = localStorage.getItem('username');
        location.href =  `/detailed_info?driver=${username}&passenger=${nickname}`
      }
    },
    selectPendingRow() {
      if (process.client) {
        let username = localStorage.getItem('username');
        location.href = `/driverPendingDriveDetail?username=${username}`
      }
    },
    searchRoutes: async function() {
      if (process.client) {
        const userName = localStorage.getItem('username') || 'sebug'
        const response = await fetch(`/api/ProposedDrivers?username=${userName}`)
        const proposedDrivers = await response.json()

        this.results = proposedDrivers
      }
    },
    openShareView() {
      if (process.client) {
        location.href = '/driveShare'
      }
    }
  }
}
</script>

