# BotFlow API
This repository is a Rest API for the [BotFlow](https://github.com/lappis-unb/BotFlow).

## Get started
We use [Docker](https://www.docker.com/) and [Docker-Compose](https://docs.docker.com/compose/) for development environment. You only need this two tools to run this project.

To start the django server and the mongo database, follow the instructions bellow:

```sh
cd BotFlowAPI
sudo docker-compose up --build
```

After a small slice of time the django server will be ready at http://localhost:8000/api/v1/

To stop the containers, run:

```
sudo docker-compose down
```

or, to remove the volumes (and erase the database):

```
sudo docker-compose down --volumes
```

If there is no previously made database, there will be created a default project with examples of utters, intents and stories. The content used to populate the database is contained in `src/api/fixtures/initial.json`. If no seed is necessary, edit `runserver.sh` to remove the seed script call:

```sh
#! /bin/bash

cd /src
python3 manage.py makemigrations
python3 manage.py migrate
# python3 manage.py shell < populate_models.py
python3 manage.py runserver 0.0.0.0:8000
```

## Architecture
All the persistent data is stored on a non relational database (mongo db), we choose this option because our data are like documents and make more sense store them as json.

Our models are, `project, story, intent, utter`, a `project` is an abstraction for a new bot project that will be managed by the BotFlow, the other abstractions are like the normal terminologies of a rasa bot.

## Usage
Since the API follows the REST architecture, those are the available endpoints:

### Projects
- GET, PUT /api/v1/projects
- GET, PUT, PATCH, DELETE /api/v1/projects/:project_id

### Intents
- GET, PUT /api/v1/projects/:project_id/intents
- GET, PUT, PATCH, DELETE /api/v1/projects/:project_id/intents/:intent_id
- GET /api/v1/projects/:project_id/intents/:intent_id/example

### Utters
- GET, PUT /api/v1/projects/:project_id/utters
- GET, PUT, PATCH, DELETE /api/v1/projects/:project_id/utters/:utter_id
- GET /api/v1/projects/:project_id/utters/:utter_id/example

### Stories
- GET, PUT /api/v1/projects/:project_id/stories
- GET, PUT, PATCH, DELETE /api/v1/projects/:project_id/stories/:story_id

To download the bot-readable content files, send a GET request to:
- /api/v1/files/:project_id/zip/

The used JSON format can be found in Django Rest Framework web interface: http://localhost:8000/api/v1/

## Lincese
The entire BotFlow platform is developed under the license [GPL3](https://github.com/lappis-unb/BotFlow/blob/master/LICENSE)
