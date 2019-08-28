const { Intent } = require('../models/intentModel')
const { Utter } = require('../models/utterModel')
const { Story } = require('../models/storyModel')

module.exports.getAllCollections = async function getAllCollections (req, res, next) {
  const { project_name } = req.params
  const json_object = {}
  try {
    json_object.intents = await Intent.find({ project_name })
    json_object.utters = await Utter.find({ project_name })
    json_object.stories = await Story.find({ project_name })
    res.json(json_object)
  } catch (err) {
    res.json(err)
    next(err)
  }
}

module.exports.insertAllCollections = async function insertAllCollections (req, res, next) {
  const { project_name } = req.params
  const { intents, utters, stories } = req.body
  intents.map((intent) => {
    const newIntent = intent
    newIntent.project_name = project_name
    return newIntent
  })
  utters.map((utter) => {
    const newUtter = utter
    newUtter.project_name = project_name
    return newUtter
  })
  stories.map((story) => {
    const newStory = story
    newStory.project_name = project_name
    return newStory
  })
  const json_object = {}
  try {
    json_object.intents = await Intent.collection.insertMany(intents)
    json_object.intents = json_object.intents.ops
    json_object.utters = await Utter.collection.insertMany(utters)
    json_object.utters = json_object.utters.ops
    json_object.stories = await Story.collection.insertMany(stories)
    json_object.stories = json_object.stories.ops
    res.json(json_object)
  } catch (err) {
    res.json(err)
    next(err)
  }
}
