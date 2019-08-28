const { Story } = require('../models/storyModel')
const fs = require('fs')

module.exports.createStory = async function createStory (req, res, next) {
  const json_object = req.body
  json_object.project_name = req.params.project_name
  try {
    const save_story = await Story.collection.insertOne(json_object)
    res.json(save_story.ops)
  } catch (err) {
    next(err)
  }
}

module.exports.getAllStories = async function getAllStories (req, res, next) {
  const { project_name } = req.params
  try {
    const get_story = await Story.find({ project_name })
    res.json(get_story)
  } catch (err) {
    res.json(err)
    next(err)
  }
}

module.exports.updateStory = async function updateStory (req, res, next) {
  const { story_id } = req.params
  try {
    const story_doc = await Story.updateOne({ _id: story_id }, req.body)
    res.json(story_doc)
  } catch (err) {
    res.json(err)
    next(err)
  }
}

module.exports.deleteStory = async function deleteStory (req, res, next) {
  const { story_id } = req.params
  try {
    const story_doc = await Story.deleteOne({ _id: story_id })
    res.json(story_doc)
  } catch (err) {
    res.json(err)
    next(err)
  }
}

const buildStoryFile = function buildStoryFile (stories) {
  let storyfile = ''
  for (let i = 0; i < stories.length; i++) {
    storyfile += '## Story for ' + stories[i]['nameIntent'] + '\n'
    storyfile += '* ' + stories[i]['nameIntent'] + '\n'
    storyfile += '  - ' + stories[i]['nameUtter'] + '\n\n'
  }
  return storyfile
}

module.exports.generateStoryFile = async function generateStoryFile (req, res, next) {
  const { project_name } = req.params
  try {
    const get_story = await Story.find({ project_name })

    const storyFile = await buildStoryFile(get_story)
    if (!fs.existsSync('/' + project_name)) {
      fs.mkdirSync('/' + project_name)
    }
    if (!fs.existsSync('/' + project_name + '/data')) {
      fs.mkdirSync('/' + project_name + '/data')
    }
    const file = '/' + project_name + '/data/stories.md'

    fs.writeFile(file, storyFile, function (err) {
      if (err) {
        res.json({ success: false, message: err })
      }

      res.download(file)
    })
  } catch (err) {
    res.json({ success: false, message: err })
    next(err)
  }
}