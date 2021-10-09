<template>
  <v-row justify='center' align='center'>
    <v-col cols='12' sm='8' md='6'>
      <v-card>
        <v-card-title class='headline'>
          {{ title }}
        </v-card-title>
        <v-card-text>
          <p>
            {{userDriveDescription}}
          </p>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>
<script>


export default {
 async fetch() {
   if (process.client) {
     const urlSearchParams = new URLSearchParams(location.search)

     const nickname = urlSearchParams.get('nickname')
     this.title = 'Details given by ' + nickname + ' for selected drive'
   }
 },
  fetchOnServer: false,
  data() {
    return {
      title: 'Details given by for selected drive',
      userDriveDescription: 'Ich nehme mein Velo mit'
    }
  }

}
</script>
