# Architeture Rasa-nlu-trainner-api
## data
Folder that have conf file of ngnix to generate https protocol
## docker
Folder that have Dockerfile that creates images docker of production and development 
## Server

### Bin(Folder)

Auto generated files from express with config of server

- Port: 3030

### Config(Folder)

Config folder of project with:

#### connectDb.js

File that create secure connecton with mongodb(docker, if you want to use mongodb standlone, change the URI `mongodb:27017` for `locahost:27017`)

##### variables:
> - MONGO_USERNAME: username of mongodb(can be passed in docker-compose or mongdb.env file)
> - MONGO_PASSWORD: password of passed user(can be passed in docker-compose or mongdb.env file)
> - MONGO_DATABASE: database to connect(can be passed in docker-compose or mongdb.env file)

#### logger.js
File response to generate console of logs

### Models
Folder that stores mongo models of database, exported respective object Model

### Controllers
Folder that stores controllers with methods of create, get, update and delete of respective model(file of Models folder)

### Route
Folder that stores routes of project, each file corresponds one controller file

### Private
Folder that stores .key(secret) and .pub(public) keys of JWT(RS256)
- If is the first time that you ran project, you need to generate these keys, in private folder run:
> `sudo ssh-keygen -t rsa -b 4096 -m PEM -f jwtRS256.key && openssl rsa -in jwtRS256.key -pubout -outform PEM -out jwtRS256.key.pub`

### app.js
File that generate swagger documentation, and send routes(files in route folder) to app(server) with cors enabled

## init-letsencrypt.sh(production)
Shell script that genarete https protocol with nginx and lets-encrypt

## mongodb.env(production)
Env file that have environments variable to connect with mongodb

## docker-copmose.yml
YAML file that create docker containner in development mode
## production.yml
YAML file that create docker containner in production mode