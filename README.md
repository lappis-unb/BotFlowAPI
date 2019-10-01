# BotFlow API
This repository is a Rest API for the BotFlow platform [https://github.com/lappis-unb/BotFlow](https://github.com/lappis-unb/BotFlow)

## Get started
We use [Docker](https://www.docker.com/) and [Docker-Compose](https://docs.docker.com/compose/) for development environment. You only need this two tools to run this project.

To start the django server and the mongo database, follow the instructions bellow:

```
$ cd BotFlowAPI
$ sudo docker-compose up --build
```

After a small slice of time the django server will be ready at http://localhost:8000/api/v1/


## Usage
To download the bot-readable content files, send a GET request to:
- /api/v1/files/:project_id/zip/

## Lincese
The entire BotFlow platform is developed under the license [GPL3](https://github.com/lappis-unb/BotFlow/blob/master/LICENSE)
