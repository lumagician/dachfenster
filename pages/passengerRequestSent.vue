<template>
  <v-row>
    <v-col class="text-center">
        <v-icon x-large class="primary">
            mdi-account-check
        </v-icon>
      <blockquote class="blockquote">
        You have successfully requested a ride share with {{ driver }}. We'll let you
        know once they have made their decision.
      </blockquote>
    </v-col>
  </v-row>
</template>
<script>
export default {
    setup() {
        
    },
    data() {
        return {
            driver: ''
        };
    },
    async fetch() {
        let driverName = '';
        if (process.client) {
            const urlSearchParams = new URLSearchParams(location.search);

            driverName = urlSearchParams.get('driver');
        }
        this.driver = driverName;
    },
    fetchOnServer: false
};
</script>


