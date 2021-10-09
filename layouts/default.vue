<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant="miniVariant"
      :clipped="clipped"
      fixed
      app
    >
      <v-list>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
      :clipped-left="clipped"
      fixed
      app
    >
      <v-btn
        icon
        @click.stop="miniVariant = !miniVariant"
      >
        <v-icon>mdi-{{ `chevron-${miniVariant ? 'right' : 'left'}` }}</v-icon>
      </v-btn>
      <v-toolbar-title v-text="title" />
      <v-spacer />
      <v-btn>fr</v-btn>
      <span v-if="userName">Hello, {{ userName }}</span>
      <v-btn icon nuxt to="/login">
        <v-icon>mdi-account</v-icon>
      </v-btn>
    </v-app-bar>
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
    <v-footer
      :absolute="!fixed"
      app
    >
      <span>&copy; {{ new Date().getFullYear() }} La Girafe</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data () {
    let userName = '';
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      items: [
        {
          icon: 'mdi-apps',
          title: 'Wilkommen',
          to: '/'
        },
        {
          icon: 'mdi-thumb-up',
          title: 'Passagier',
          to: '/passenger'
        },
        {
          icon: 'mdi-share',
          title: 'Fahrt sharen',
          to: '/driveShare'
        }
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'Dachfenster',
      userName: userName
    }
  }
};
</script>
