# BotFlow API
This repository is an API of the BotFlow platform [https://github.com/lappis-unb/BotFlow](https://github.com/lappis-unb/BotFlow)

## How to Contribute
To contribute to our API just follow the steps below!

- First we will enable a local environment for work, so just follow the step by step described below:
    
* Check Prerequisites:

    It is necessary to have a Docker or Node8 machine installed and (Yarn or NPM)

    * [Docker](https://www.docker.com/)

    * [Node8](https://nodejs.org/es/blog/release/v8.0.0/)

    * [Yarn](https://yarnpkg.com/pt-BR/)

    * [Npm](https://www.npmjs.com/)


### Running project by using Docker (recomended)

``docker-compose up --build``


### Running project by using npm (or yarn)

*Node version: 10 or higher*

Inside folder server run:

``npm install``

or 

``yarn install``

Then run:

``npm start``

or

``yarn start``


Then the execution according to the choice of one of the previous operations, the platform will be available through access in:
    
`http://localhost:3030/`


## Access the API
Endpoints documented (Try out doesn't work)

Stable version of the API [Access here](https://botflow.api.lappis.rocks/api-docs)

## Generate jwtRS256 Key

To run this project is necessary to create a jwtRS256 key in the private folder. To create the key run the following commands on the `server/private/` folder:

``` sh
ssh-keygen -t rsa -b 4096 -m PEM -f jwtRS256.key
# Don't add passphrase
openssl rsa -in jwtRS256.key -pubout -outform PEM -out jwtRS256.key.pub
```

## Lincese
The entire BotFlow platform is developed under the license [GPL3](https://github.com/lappis-unb/BotFlow/blob/master/LICENSE)
