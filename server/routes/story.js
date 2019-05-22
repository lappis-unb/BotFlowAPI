const express = require('express');

const app = express.Router();
const {
  createStory,
  getAllStories,
  updateStory,
  deleteStory,
} = require('../controllers/storyController.js');

app
  .route('/:projectName/story')
  .post(createStory)
  .get(getAllStories);
app
  .route('/story/:storyId')
  .put(updateStory)
  .delete(deleteStory);

module.exports = app;
