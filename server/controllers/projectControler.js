const { Intent } = require('../models/intentModel')
const { Utter } = require('../models/utterModel')
const { Story } = require('../models/storyModel')

module.exports.getAllCollections = async function getAllCollections (req, res, next) {
  const { projectName } = req.params
  const jsonObject = {}
  try {
    jsonObject.intents = await Intent.find({ projectName })
    jsonObject.utters = await Utter.find({ projectName })
    jsonObject.stories = await Story.find({ projectName })
    res.json(jsonObject)
  } catch (err) {
    res.json(err)
    next(err)
  }
}

module.exports.insertAllCollections = async function insertAllCollections (req, res, next) {
  const { projectName } = req.params
  const { intents, utters, stories } = req.body
  intents.map((intent) => {
    const newIntent = intent
    newIntent.projectName = projectName
    return newIntent
  })
  utters.map((utter) => {
    const newUtter = utter
    newUtter.projectName = projectName
    return newUtter
  })
  stories.map((story) => {
    const newStory = story
    newStory.projectName = projectName
    return newStory
  })
  const jsonObject = {}
  try {
    jsonObject.intents = await Intent.collection.insertMany(intents)
    jsonObject.intents = jsonObject.intents.ops
    jsonObject.utters = await Utter.collection.insertMany(utters)
    jsonObject.utters = jsonObject.utters.ops
    jsonObject.stories = await Story.collection.insertMany(stories)
    jsonObject.stories = jsonObject.stories.ops
    res.json(jsonObject)
  } catch (err) {
    res.json(err)
    next(err)
  }
}
