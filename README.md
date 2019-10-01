# BotFlow API
This repository is a Rest API for the [BotFlow](https://github.com/lappis-unb/BotFlow).

## Get started
We use [Docker](https://www.docker.com/) and [Docker-Compose](https://docs.docker.com/compose/) for development environment. You only need this two tools to run this project.

To start the django server and the mongo database, follow the instructions bellow:

```
$ cd BotFlowAPI
$ sudo docker-compose up --build
```

After a small slice of time the django server will be ready at http://localhost:8000/api/v1/

## Architecture
All the persistent data is stored on a non relational database (mongo db), we choose this option because our data are like documents and make more sense store them as json.

Our models are, `project, story, intent, utter`, a `project` is an abstraction for a new bot project that will be managed by the BotFlow, the other abstractions are like the normal terminologies of a rasa bot.

## Usage
To download the bot-readable content files, send a GET request to:
- /api/v1/files/:project_id/zip/

## Lincese
The entire BotFlow platform is developed under the license [GPL3](https://github.com/lappis-unb/BotFlow/blob/master/LICENSE)
