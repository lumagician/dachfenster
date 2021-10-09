<template>
  <v-container fluid grid-list-md>
    <v-row class="d-flex">
      <v-col class="text-left">
        <v-card class="mb-6 pa-4" elavation="10">
          <v-row class="pl-5">
            <v-card-title>{{ username }}</v-card-title>
            <v-rating
              half-increments
              length="5"
              readonly
              size="20"
              :value="rating"
              class="mt-4"
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
        <v-card class="pa-2 pb-6" elavation="10">
          <div id="myMap" style="height: 50vh; margin-bottom: 30px"></div>
          <div id="printoutPanel" style="display: none"></div>
          <v-row
            class="px-10 text-center"
          >
            <v-card class="pa-2" color="blue" style="margin:auto">
              <v-card-text>Reisezeit</v-card-text>
              <h3>{{ rideDuration }}</h3>
            </v-card>
          </v-row>
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
  });
  Microsoft.Maps.loadModule('Microsoft.Maps.Directions', function () {
    var directionsManager = new Microsoft.Maps.Directions.DirectionsManager(map);
    // Set Route Mode to driving
    directionsManager.setRequestOptions({
      routeMode: Microsoft.Maps.Directions.RouteMode.driving,
      maxRoutes: 1,
    });
    for (let mapPoint of mapPoints) {
      let waypoint = new Microsoft.Maps.Directions.Waypoint({
        address: mapPoint.label,
        location: new Microsoft.Maps.Location(mapPoint.lat, mapPoint.long),
      });
      directionsManager.addWaypoint(waypoint);
    }
    // Set the element in which the itinerary will be rendered
    directionsManager.setRenderOptions({
      itineraryContainer: document.getElementById('printoutPanel'),
    });
    directionsManager.calculateDirections();
  })
}

export default {
  data: () => ({
    username: 'no user showed',
    rating: 0,
    tags: ['not a tag', 'not a tag'],
    rideDuration: '-',
  }),

  head: {
    script: [
      {
        hid: 'bingmaps',
        src:
          '//www.bing.com/api/maps/mapcontrol?key=' + process.env.BING_MAPS_KEY,
      },
    ],
  },

  async fetch() {
    if (process.client) {
      const urlSearchParams = new URLSearchParams(location.search);

      const passenger = urlSearchParams.get('passenger');
      const driver = urlSearchParams.get('driver');

      let fullJson;

      if (passenger && driver) {
        const response = await fetch(
          `/api/GetDriverPassengerMatch?driver=${driver}&passenger=${passenger}`
        );
        console.log(passenger);
        fullJson = await response.json();
        console.log(fullJson);
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
          }
        };
      }

      function convertHM(sec) {
        let hours = Math.floor(sec / 3600);
        let minutes = Math.floor((sec - hours * 3600) / 60);
        return (hours + 'h ' + minutes + 'min');
      }

      const PointA = fullJson.duration.DriverStartCoordinates.split(',');
      const PointB = fullJson.duration.PassengerStartCoordinates.split(',');
      const PointC = fullJson.duration.PassengerDestinationCoordinates.split(',');
      const PointD = fullJson.duration.DriverDestinationCoordinates.split(',');

      let discriptionSplit = null;
      let goodiesSplit = null;
      let mapPoints;

      console.log(convertHM(fullJson.duration.Duration - fullJson.driver.DurationWithoutPassenger))

      if (passenger == localStorage.getItem('username')) {
        this.username = fullJson.driver.RowKey;
        this.rating = fullJson.driver.Rating;
        discriptionSplit = fullJson.driver.Description.split(', ');
        goodiesSplit = fullJson.driver.Goodies.split(', ');
        mapPoints = [
          { label: 'Passagier Start', lat: PointB[0], long: PointB[1] },
          { label: 'Passagier Ende', lat: PointC[0], long: PointC[1] },
        ];
      } else if (driver == localStorage.getItem('username')) {
        this.username = fullJson.passenger.RowKey;
        this.rating = fullJson.passenger.Rating;
        this.rideDuration = convertHM(fullJson.duration.Duration);
        discriptionSplit = fullJson.passenger.Description.split(', ');
        goodiesSplit = fullJson.passenger.Goodies.split(', ');
        mapPoints = [
          { label: 'Fahrer Start', lat: PointA[0], long: PointA[1] },
          { label: 'Passagier Start', lat: PointB[0], long: PointB[1] },
          { label: 'Passagier Ende', lat: PointC[0], long: PointC[1] },
          { label: 'Fahrer End', lat: PointD[0], long: PointD[1] },
        ];
      }

      
      this.tags = discriptionSplit.concat(goodiesSplit);
      

      GetMap(mapPoints);
    }
  },
  fetchOnServer: false,
}
</script>