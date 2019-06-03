const express = require('express')
const cookieParser = require('cookie-parser')
const bodyParser = require('body-parser')
const cors = require('cors')

const app = express()
const expressSwagger = require('express-swagger-generator')(app)

const intentRoute = require('./routes/intent')
const utterRoute = require('./routes/utter')
const storyRoute = require('./routes/story')
const projectRoute = require('./routes/project')
const sessionRoute = require('./routes/session')
const userRoute = require('./routes/user')
const domainRoute = require('./routes/domain')

/*
const whitelist = [process.env.URL_GITHUB_IO, process.env.URL_DOMAIN]
const corsOptions = {
  origin: (origin, callback) => {
    if (whitelist.indexOf(origin) !== -1) {
      callback(null, true)
    } else {
      callback(new Error('Not allowed by CORS'))
    }
  }
}
Only enable if is in production */
const options = {
  swaggerDefinition: {
    info: {
      version: '1.0.0',
      title: 'Rasa-nlu-trainer API',
      description: 'This is an API for rasa-nlu-trainer',
      contact: {
        name: 'Lappis UnB',
        url: 'https://fga.unb.br/lappis'
      },
      license: {
        name: 'MIT',
        url: 'http://opensource.org/licenses/MIT'
      }
    },
    produces: ['application/json', 'application/xml'],
    schemes: ['http', 'https']
  },
  basedir: __dirname,
  files: ['./routes/**/*.js']
}

expressSwagger(options)
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))
app.use(cookieParser())
app.use(cors(), intentRoute)
app.use(cors(), utterRoute)
app.use(cors(), storyRoute)
app.use(cors(), projectRoute)
app.use(cors(), sessionRoute)
app.use(cors(), userRoute)
app.use(cors(), domainRoute)
module.exports = app
