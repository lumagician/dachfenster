# dachfenster🚗🦒
Dieses Programm hilft dir, die perfekten Mitfahrgelegenheiten zu finden! 

Du kannst die App hier testen: https://icy-mushroom-08156d003.azurestaticapps.net



# Devpost Stuff
## Inspiration
As extensive research has showed, car sharing has a big potential for reducing our environmental impact as well as to offer convenient ways to travel.
Here we aimed not only at producing a pragmatic design, we wanted to provide features which actually make car sharing an agreeable experience that 
adds value for users. For example, users can be interested in not having to drive alone but instead in sharing their trip with 
someone matching their personality or having same needs of punctuality depending on the journey.

## What it does
We have built a progressive web app that enables to optimize the way of drivers and passengers to trade their respective needs for car sharing and enables to find the best match based on other soft factors.


## How we built it

We first asked ourselves what are needs of users that use a car sharing app. We discussed features the app should have to 
be more attractive and designed various alternative mockups before converging on our current design. 

## Built using open source software and modern SaaS 

- [NuxtJS](https://nuxtjs.org/) as frontend framework
- [Vuetify](https://vuetifyjs.com/) as part of NuxtJS
- [Azure static apps](https://azure.microsoft.com/de-de/services/app-service/static/) for hosting our app   
- [Azure tables](https://azure.microsoft.com/de-de/services/storage/tables/) as storage
- [GitHub actions](https://docs.github.com/en/actions) for continuous integration

## Challenges we ran into

What would a user find useful, which additional information, which compromises to keep the ui simple to use on an everyday basis? 
How to help potential users to overcome the hurdle of not knowing what kind of expectation the driver or passenger may have?

## Accomplishments that we're proud of
We hacked non-stop and were able to produce a working, scalable app that distinguishes itself with features that we believe makes car sharing easier and more attractive.
We had a very good team spirit. 

## What we learned
We could immerse ourselves in the problematic of car sharing, which is an increasingly relevant subject especially in the context of raising environmental awareness. 
Indeed, we found it interesting to wrap our heads around how to make car sharing possibilities more attractive. Also, we could learn new technologies and 
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
