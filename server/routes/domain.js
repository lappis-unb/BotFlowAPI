const express = require('express')

const app = express.Router()
const {
    createStory,
    getAllStories,
    updateStory,
    deleteStory,
    generateStoryFile
} = require('../controllers/storyController.js')


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