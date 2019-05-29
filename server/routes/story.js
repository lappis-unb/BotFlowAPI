const express = require('express')

const app = express.Router()
const {
  createStory,
  getAllStories,
  updateStory,
  deleteStory,
  generateStoryFile
} = require('../controllers/storyController.js')

/**
 * @typedef Story
 * @property {string} nameIntent.required
 * @property {string} nameUtter.required
 */

/**
 * @typedef StoryReturnGet
 * @property {string} _id.required
 * @property {string} nameIntent.required
 * @property {string} nameUtter.required
 * @property {string} projectName.required
 */

/**
 * @typedef ReturnPut
 * @property {string} n.required
 * @property {string} nModified.required
 * @property {string} ok.required
 */

/**
 * @typedef ReturnDelete
 * @property {string} n.required
 * @property {string} deletedCount.required
 * @property {string} ok.required
 */

/**
 * This function comment is parsed by doctrine
 * @route GET /{projectName}/story
 * @group Story - Operations about stories
 * @param {string} projectName.path.required - name of project - eg: testeRasa
 * @returns {Array.<StoryReturnGet>} 200 - An array of stories info
 * @returns {Error}  default - Unexpected error
 */

/**
 * @route POST /{projectName}/story
 * @group Story - Operations about stories
 * @param {string} projectName.path.required - name of project - eg: testeRasa
 * @param {Story.model} story.body.required
 * @returns {Array.<StoryReturnGet>} 200 - An array of object of story included
 * @returns {Error}  default - Unexpected error
 */

/**
 * @route PUT /story/{storyId}
 * @group Story - Operations about stories
 * @param {string} storyId.path.required - id of utter - eg: 1c24gdq2135s
 * @param {Story.model} story.body.required
 * @returns {ReturnPut.model} 200 - An object of numbers of documents modified and if status is ok
 * @returns {Error}  default - Unexpected error
 */

/**
 * @route DELETE /story/{storyId}
 * @group Story - Operations about stories
 * @param {string} storyId.path.required - id of utter - eg: 1c24gdq2135s
 * @returns {ReturnDelete.model} 200 - An object of numbers of documents deleted and if status is ok
 * @returns {Error}  default - Unexpected error
 */

app
  .route('/:projectName/story')
  .post(createStory)
  .get(getAllStories)
app
  .route('/story/:storyId')
  .put(updateStory)
  .delete(deleteStory)

app
  .route('/:projectName/story/generate_file')
  .get(generateStoryFile)

module.exports = app
