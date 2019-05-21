const express = require('express');
const cors = require('cors');

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

const app = express.Router();
const {
  createIntent,
  getAllIntents,
  updateIntent,
  deleteIntent,
} = require('../controllers/intentController');

const {
  createUtter,
  getAllUtters,
  updateUtter,
  deleteUtter,
} = require('../controllers/utterController');

const {
  createStory,
  getAllStories,
  updateStory,
  deleteStory,
} = require('../controllers/storyController.js');

const { getAllCollections, insertAllCollections } = require('../controllers/projectControler');

// Insert/get all collection endpoints
app.post('/:projectName/upload', cors(corsOptions), insertAllCollections);
app.get('/:projectName/info', cors(corsOptions), getAllCollections);

// Intents endpoints
app
  .route('/:projectName/intent', cors(corsOptions))
  .post(createIntent)
  .get(getAllIntents);
app
  .route('/intent/:intentId', cors(corsOptions))
  .put(updateIntent)
  .delete(deleteIntent);

// Utters endpoints
app
  .route('/:projectName/utter', cors(corsOptions))
  .post(createUtter)
  .get(getAllUtters);
app
  .route('/utter/:utterId', cors(corsOptions))
  .put(updateUtter)
  .delete(deleteUtter);

// Stories endpoints
app
  .route('/:projectName/story', cors(corsOptions))
  .post(createStory)
  .get(getAllStories);
app
  .route('/story/:storyId', cors(corsOptions))
  .put(updateStory)
  .delete(deleteStory);

module.exports = app;
