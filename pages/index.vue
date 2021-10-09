<template>
  <v-row justify='center' align='center'>
    <v-col cols='12' sm='8' md='6'>
      <v-card class='logo py-4 d-flex justify-center'>
        <LaGirafeLogo />
      </v-card>
      <v-card>
        <v-card-title class='headline'>
          Dachfenster - Fahr mit
        </v-card-title>
        <v-card-text>
          <p>Hast du es satt, alleine zur Arbeit zu fahren? Finde auf Dachfenster eine
            Mitfahrgelegenheit. Aber zuallererst, was bist du?
          </p>
        </v-card-text>

        <v-card-actions class="justify-center">
          <v-btn
            color='primary'
            nuxt
            to='/passenger'
          >
            Ich bin Passagier
          </v-btn>
          <v-btn
            color='primary'
            nuxt
            to='/inspire'
          >
            Ich bin Fahrer
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>
