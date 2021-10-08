
<template>
  <v-container fluid grid-list-md>
    <v-row>
      <v-col class="text-left">
        <v-card elavation="5" style="margin-bottom: 25px">
          <div id="myMap" style="width: 40vw; height: 50vh"></div>
          <div id="printoutPanel" style="display: none"></div>
        </v-card>
        <v-card elavation="5">
          <v-card-text>
            Bin eine Giraffe => brauche ein Dachfenster
          </v-card-text>
        </v-card>
      </v-col>
      <v-col class="text-left">
        <v-card elavation="5">
          <v-card-title> La Giraffe </v-card-title>
          <v-rating
            half-increments
            length="5"
            readonly
            size="20"
            value="5"
          ></v-rating>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>


<script>
if (process.client) {
  window.GetMap = function GetMap() {
    var map = new Microsoft.Maps.Map(document.getElementById('myMap'), {
      /* No need to set credentials if already passed in URL */
      center: new Microsoft.Maps.Location(51.477778, -0.001389),
      zoom: 16,
    })
    Microsoft.Maps.loadModule('Microsoft.Maps.Directions', function () {
      var directionsManager = new Microsoft.Maps.Directions.DirectionsManager(
        map
      )
      // Set Route Mode to driving
      directionsManager.setRequestOptions({
        routeMode: Microsoft.Maps.Directions.RouteMode.driving,
      })
      var waypoint1 = new Microsoft.Maps.Directions.Waypoint({
        address: 'Driver Start',
        location: new Microsoft.Maps.Location(46.879114, 7.620547),
      })
      var waypoint2 = new Microsoft.Maps.Directions.Waypoint({
        address: 'Passenger Start',
        location: new Microsoft.Maps.Location(46.926458, 7.564239),
      })
      var waypoint3 = new Microsoft.Maps.Directions.Waypoint({
        address: 'Passenger End',
        location: new Microsoft.Maps.Location(46.947371, 7.438867),
      })
      var waypoint4 = new Microsoft.Maps.Directions.Waypoint({
        address: 'Driver End',
        location: new Microsoft.Maps.Location(46.925377, 7.416773),
      })
      directionsManager.addWaypoint(waypoint1)
      directionsManager.addWaypoint(waypoint2)
      directionsManager.addWaypoint(waypoint3)
      directionsManager.addWaypoint(waypoint4)
      // Set the element in which the itinerary will be rendered
      directionsManager.setRenderOptions({
        itineraryContainer: document.getElementById('printoutPanel'),
      })
      directionsManager.calculateDirections()
    })
  }
}

export default {
  head: {
    script: [
      {
        hid: 'bingmaps',
        src:
          '//www.bing.com/api/maps/mapcontrol?callback=GetMap&key=' +
          process.env.BING_MAPS_KEY,
        defer: true,
      },
    ],
  },
}
</script>
