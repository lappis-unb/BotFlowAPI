const express = require('express');

const app = express.Router();
const {
  createIntent,
  getAllIntents,
  updateIntent,
  deleteIntent,
} = require('../controllers/intentController');

app
  .route('/:projectName/intent')
  .post(createIntent)
  .get(getAllIntents);
app
  .route('/intent/:intentId')
  .put(updateIntent)
  .delete(deleteIntent);

module.exports = app;
