# dachfenster🚗🦒
Dieses Programm hilft dir, die perfekten Mitfahrgelegenheiten zu finden! 

Du kannst die App hier testen: https://icy-mushroom-08156d003.azurestaticapps.net

## built using open source software 

- [NuxtJS](https://nuxtjs.org/) as frontend framework
- [Vuetify](https://vuetifyjs.com/) as part of NuxtJS



## Run it yourself

Declare an environment variable containing the bing maps key:

In Windows:

    setx BING_MAPS_KEY ...

Or using the UI.

In Linux / Mac 

    export BING_MAPS_KEY=...
    
(you can put that in your .profile / .zshrc)

```bash
# install dependencies
$ npm ci

# serve with hot reload at localhost:3000
$ npm run dev
```

## To test functions locally

    . .venv/bin/activate
    func host start 