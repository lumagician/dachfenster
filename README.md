# dachfenster🚗🦒
Dieses Programm hilft dir, die perfekten Mitfahrgelegenheiten zu finden! 

Du kannst die App hier testen: https://icy-mushroom-08156d003.azurestaticapps.net




# Devpost Stuff
## Inspiration

## What it does


## How we built it

We first asked ourselves what are needs of users that would use this app for 
## built using open source software 

- [NuxtJS](https://nuxtjs.org/) as frontend framework
- [Vuetify](https://vuetifyjs.com/) as part of NuxtJS
- [Azure static apps](https://azure.microsoft.com/de-de/services/app-service/static/) for hosting our app   
- [Azure tables](https://azure.microsoft.com/de-de/services/storage/tables/) as storage
- [GitHub actions](https://docs.github.com/en/actions) for continuous integration

## Challenges we ran into

What would a user find useful, which additional information, which compromises to keep the ui simple to use on an everyday basis. 
How to help potential users overcome the hurdle of not knowing what kind of  
## Accomplishments that we're proud of
We hacked non-stop and were able to produce a working, scalable app that distinguishes itself with feature that we believe makes car sharing easier and more attractive.
We had a very good team spirit. 

## What we learned
We could immerse ourselves in the problematic of care sharing, which is an increasingly relevant subject especially in the context of raising environmental awareness. 
Indeed, we found interesting to wrap our heads around how to make car sharing possibilities more attractive. Also, we could learn new technologies and 
to verify their efficiency for solving real use cases. In addition, it was a great opportunity to think about design and applying some techniques of design thinking. 
## What's next for Dachfenster
Take a good rest first, and then we will see :) 

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
