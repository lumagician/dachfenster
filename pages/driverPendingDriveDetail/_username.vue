<template>
  <v-row justify='center' align='center'>
    <v-col cols='12' sm='8' md='6'>
      <v-card>
        <v-card-title class='headline'>
          {{ title }}
        </v-card-title>
        <v-card-text>
          <p>
            {{ driveDetail.days.join(', ') }} {{ driveDetail.regularity }} <br />
            <span class='highlightFromTo'> Abfahrt </span> {{ driveDetail.fromTime }} <br />
            <span class='highlightFromTo'> Von </span> {{ driveDetail.fromAddress }} <br /> <span
            class='highlightFromTo'> nach </span> {{ driveDetail.toAddress }} <br />
          </p>

          <v-divider></v-divider>

          <v-simple-table>
            <template v-slot:default>
              <thead>
              <tr>
                <th class='text-left'>
                  Nickname
                </th>
                <th class='text-left'>
                  User rating
                </th>
                <th class='text-center'>
                  Berechnete Fahrzeit
                </th>
                <th class='text-center'>

                </th>
              </tr>
              </thead>
              <tbody>
              <tr
                v-for='item in drives'
                :key='item.nickname'

              >
                <td @click='accept(item)'>{{ item.nickname }}</td>
                <td @click='accept(item)'>
                  <v-rating
                    v-bind:style="{ 'max-width': '10px' }"
                    size='5'
                    :value='item.rating'
                    small readonly
                  ></v-rating>
                </td>
                <td class='centered' @click='accept(item)'>{{ item.estimatedTimeInMinutes }} Minuten</td>
                <td class='centered' @click='showDetails(item)'><a>Beschreibung</a></td>
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
  data() {
    return {
      title: 'Pending drive detail',
      driveDetail: {
        days: ['Montag', 'Donnerstag'],
        regularity: 'wöchentlich',
        fromTime: '10:00',
        toTime: '10:50',
        fromAddress: 'Bern Wankdorf',
        toAddress: 'Bern Hauptbahnhof'
      },
      drives: [
        {
          nickname: 'Milou',
          rating: 3.5,
          estimatedTimeInMinutes: 35
        },
        {
          nickname: 'Max32',
          rating: 2.4,
          estimatedTimeInMinutes: 45
        },
        {
          nickname: 'Test',
          rating: 3.5,
          estimatedTimeInMinutes: 30
        },
        {
          nickname: 'Cardriver2',
          rating: 4.5,
          estimatedTimeInMinutes: 40
        }
      ],
      fromAddress: 'Guisanstr. 2, 3014 Bern',
      toAddress: 'Maritzstrasse 20, 3400 Burgdorf'

    }
  },
  methods: {
    showDetails: function(item) {
      if (process.client) {
        location.href = '/drivePassengerDetail?nickname='+item.nickname

      }
    },
    accept: function(item) {
      if (process.client) {
        var r = window.confirm("Accept this proposition?")
        if (r == true) {
          location.href = '/driver?username='+item.nickname
        } else {
          //NOP
        }

      }
    }
  }

}
</script>
