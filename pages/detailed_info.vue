
<template>
  <v-container fluid>
    <v-row>
      <v-col class="text-center">
        <v-card elavation="5">
          
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
  export default {
  head: {
    script: [
      { hid: 'bingmaps', src: 'http://www.bing.com/api/maps/mapcontrol?callback=GetMap&key=' + process.env.BING_MAPS_KEY, defer: true }
    ]
  }
}
</script>