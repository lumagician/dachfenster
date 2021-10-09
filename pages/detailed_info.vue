<template>
  <v-container fluid grid-list-md>
    <v-row class="d-flex">
      <v-col class="text-left">
        <v-card class="mb-6 pa-2 pb-6" elavation="10">
          <div id="myMap" style="height: 50vh; margin-bottom: 30px"></div>
          <div id="printoutPanel" style="display: none"></div>
          <v-row
            class="px-10 text-center"
            style="display: flex; justify-content: space-between"
          >
            <v-card class="pa-2" color="blue">
              <v-card-text> Ride Duration</v-card-text>
              <h3>{{ rideDuration }}</h3>
            </v-card>
            <v-card class="pa-2" color="green">
              <v-card-text>Estimated Start</v-card-text>
              <h3>{{ startTime }}</h3>
            </v-card>
            <v-card class="pa-2" color="green">
              <v-card-text>Estimated Arrival</v-card-text>
              <h3>{{ arrival }}</h3>
            </v-card>
          </v-row>
        </v-card>
        <v-card class="pa-2" elavation="10">
          <v-card-text>
            {{ discription }}
          </v-card-text>
        </v-card>
      </v-col>
      <v-col class="text-left">
        <v-card class="mb-6 pa-2 pb-6" elavation="10">
          <v-row class="pl-5">
            <v-card-title>{{ username }}</v-card-title>
            <v-rating
              half-increments
              length="5"
              readonly
              size="20"
              :value="rating"
              class="mt-3"
            ></v-rating>
          </v-row>
          <div class="pa-4">
            <v-chip-group active-class="primary--text" column>
              <v-chip v-for="tag in tags" :key="tag">
                {{ tag }}
              </v-chip>
            </v-chip-group>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>


<script>

function GetMap(mapPoints) {
    var map = new Microsoft.Maps.Map(document.getElementById('myMap'), {
      /* No need to set credentials if already passed in URL */
      center: new Microsoft.Maps.Location(51.477778, -0.001389),
      zoom: 15,
    })
    Microsoft.Maps.loadModule('Microsoft.Maps.Directions', function () {
      var directionsManager = new Microsoft.Maps.Directions.DirectionsManager(
        map
      )
      // Set Route Mode to driving
      directionsManager.setRequestOptions({
        routeMode: Microsoft.Maps.Directions.RouteMode.driving,
        maxRoutes: 1,
      })
      for(let mapPoint of mapPoints) {
        let waypoint = new Microsoft.Maps.Directions.Waypoint({
        address: mapPoint.label,
        location: new Microsoft.Maps.Location(mapPoint.lat, mapPoint.long),
      });
      directionsManager.addWaypoint(waypoint)
      }
      // Set the element in which the itinerary will be rendered
      directionsManager.setRenderOptions({
        itineraryContainer: document.getElementById('printoutPanel'),
      })
      directionsManager.calculateDirections()
    })
  }

export default {

  data: () => ({
    username: 'La Giraffe',
    rating: 4.5,
    discription: 'Bin eine Giraffe => brauche ein Dachfenster',
    tags: ['Small Talk', 'Nerd', 'Giraffe', 'Politik'],
    rideDuration: '1h 24min',
    startTime: '08:20',
    arrival: '09:44',
  }),
  
  head: {
    script: [
      {
        hid: 'bingmaps',
        src:
          '//www.bing.com/api/maps/mapcontrol?key=' +
          process.env.BING_MAPS_KEY,
      },
    ],
  },

  async fetch() {
    if (process.client) {
      const urlSearchParams = new URLSearchParams(location.search)

      const passenger = urlSearchParams.get('passenger')
      const driver = urlSearchParams.get('driver')

      let fullJson;

      if (passenger && driver) {
        const response = await fetch(
          `/api/GetDriverPassengerMatch?driver=${driver}&passenger=${passenger}`
        )
        console.log(response)
        fullJson = await response.json()
        console.log(fullJson)
      } else {
        fullJson = {
          driver: {
            PartitionKey: 'testing',
            RowKey: 'Kowalski',
            Description: 'Pünktlich, Nett',
            DestinationAddressCity: 'Thun',
            DestinationAddressStreet: 'Frutigenstrasse 46C',
            DestinationAddressZipCode: '3600',
            DurationWithoutPassenger: 2223,
            Goodies: 'Braucht Parkplatz',
            HasCar: true,
            Rating: 4,
            StartAddressCity: 'Köniz',
            StartAddressStreet: 'Blinzernfeldweg 14',
            StartAddressZipCode: '3098',
          },
          passenger: {
            PartitionKey: 'testing',
            RowKey: 'sebug',
            Description: 'Fussballer, Coder',
            DestinationAddressCity: 'Burgdorf',
            DestinationAddressStreet: 'Maritzstrasse 20',
            DestinationAddressZipCode: '3400',
            Goodies: 'Bringt Kaffee und Gipfeli',
            HasCar: false,
            Rating: 3.5,
            StartAddressCity: 'Bern',
            StartAddressStreet: 'Guisanplatz 2',
            StartAddressZipCode: '3014',
          },
          duration: {
            PartitionKey: 'testing',
            RowKey: 'Kowalski_sebug',
            Driver: 'Kowalski',
            DriverDestinationCoordinates: '46.7478,7.62584',
            DriverStartCoordinates: '46.92148,7.42136',
            Duration: 4781,
            Passenger: 'sebug',
            PassengerDestinationCoordinates: '47.06562,7.61428',
            PassengerStartCoordinates: '46.95872,7.464',
          },
        };
      }
      const discriptionSplit = fullJson.passenger.Description.split(', ');
      const goodiesSplit = fullJson.passenger.Goodies.split(', ');

      const PointA = fullJson.duration.DriverStartCoordinates.split(',')
      const PointB = fullJson.duration.PassengerStartCoordinates.split(',')
      const PointC = fullJson.duration.PassengerDestinationCoordinates.split(',')
      const PointD = fullJson.duration.DriverDestinationCoordinates.split(',')
      const mapPoints = [{label: 'Driver Start', lat: PointA[0], long: PointA[1]},
      {label: 'Passenger Start', lat: PointB[0], long: PointB[1]},
      {label: 'Passenger End', lat: PointC[0], long: PointC[1]},
      {label: 'Driver End', lat: PointD[0], long: PointD[1]}]

      this.username = fullJson.passenger.RowKey;
      this.tags = discriptionSplit.concat(goodiesSplit);
      this.rating = fullJson.passenger.Rating;

      GetMap(mapPoints);
      
    }
  },
  fetchOnServer: false
}
</script>