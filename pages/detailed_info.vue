
<template>
  <v-container fluid>
    <v-row>
      <v-col class="text-center">
        <v-card elavation="5">
          <div id='printoutPanel'></div>
          <div id="myMap" style="width: 100vw; height: 100vh"></div>
        </v-card>

        <v-card elavation="5">
          <img src="/v.png" alt="Vuetify.js" class="mb-5" />
        </v-card>
      </v-col>
      <v-col class="text-center">
        <v-card elavation="5">
          <img src="/v.png" alt="Vuetify.js" class="mb-5" />
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
    center: new Microsoft.Maps.Location(47.606209, -122.332071),
    zoom: 12,
  })
  Microsoft.Maps.loadModule('Microsoft.Maps.Directions', function () {
    var directionsManager = new Microsoft.Maps.Directions.DirectionsManager(map)
    // Set Route Mode to driving
    directionsManager.setRequestOptions({
      routeMode: Microsoft.Maps.Directions.RouteMode.driving,
    })
    var waypoint1 = new Microsoft.Maps.Directions.Waypoint({
      address: 'Redmond',
      location: new Microsoft.Maps.Location(
        47.67683029174805,
        -122.1099624633789
      ),
    })
    var waypoint2 = new Microsoft.Maps.Directions.Waypoint({
      address: 'Seattle',
      location: new Microsoft.Maps.Location(
        47.59977722167969,
        -122.33458709716797
      ),
    })
    directionsManager.addWaypoint(waypoint1)
    directionsManager.addWaypoint(waypoint2)
    // Set the element in which the itinerary will be rendered
    directionsManager.setRenderOptions({
      itineraryContainer: document.getElementById('printoutPanel'),
    })
    directionsManager.calculateDirections()
  })
};
}

export default {
  head: {
    script: [
      {
        hid: 'bingmaps',
        src:
          'http://www.bing.com/api/maps/mapcontrol?callback=GetMap&key=' +
          process.env.BING_MAPS_KEY,
        defer: true,
      },
    ],
  },
}
</script>
