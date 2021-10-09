<template>
  <v-row justify='center' align='center'>
    <v-col cols='12' sm='8' md='6'>
      <v-card>
        <v-card-title class='headline'>
          {{ title }}
        </v-card-title>
        <v-card-text>
          <p>

        </p>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>
<script>


export default {

  data() {
return {
      title: 'Details given by passenger for selected drive',
      username: this.$route.params.username,
      userDriveDescription: 'Ich nehme mein Velo mit'
  }
  }

}
</script>
