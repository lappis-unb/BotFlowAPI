const express = require('express');
const cookieParser = require('cookie-parser');
const bodyParser = require('body-parser');
const swaggerUi = require('swagger-ui-express');
const cors = require('cors');
const YAML = require('yamljs');

const swaggerDocument = YAML.load('./swagger-doc/swagger.yaml');
const intentRoute = require('./routes/intent');
const utterRoute = require('./routes/utter');
const storyRoute = require('./routes/story');
const projectRoute = require('./routes/project');

const app = express();
const whitelist = [process.env.URL_GITHUB_IO];
const corsOptions = {
  origin: (origin, callback) => {
    if (whitelist.indexOf(origin) !== -1) {
      callback(null, true);
    } else {
      callback(new Error('Not allowed by CORS'));
    }
  },
};

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));
app.use(cors(corsOptions), intentRoute);
app.use(cors(corsOptions), utterRoute);
app.use(cors(corsOptions), storyRoute);
app.use(cors(corsOptions), projectRoute);
module.exports = app;
