# Rasa Nlu Trainner API

## Run project
### Docker (recomended)

``docker-compose up --build``

### Via npm (or yarn)
*Node version: 10 or higher*

Inside folder server run:

``npm install``

or 

``yarn install``

Then run:

``npm start``

or

``yarn start``

The server will be avalaible in localhost on port 3030

Endpoints documented (Try out doesn't work)
https://api.tais.lappis.rocks/api-docs

## Generate jwtRS256 Key

To run this project is necessary to create a jwtRS256 key in the private foder. To create the key run the following commands on the `server/private/` folder:

``` sh
ssh-keygen -t rsa -b 4096 -m PEM -f jwtRS256.key
# Don't add passphrase
openssl rsa -in jwtRS256.key -pubout -outform PEM -out jwtRS256.key.pub
```
