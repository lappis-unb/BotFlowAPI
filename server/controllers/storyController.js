const { Story } = require('../models/storyModel')
const fs = require('fs');

module.exports.createStory = async function createStory (req, res, next) {
  const jsonObject = req.body
  jsonObject.projectName = req.params.projectName
  try {
    const saveStory = await Story.collection.insertOne(jsonObject)
    res.json(saveStory.ops)
  } catch (err) {
    next(err)
  }
}

module.exports.getAllStories = async function getAllStories (req, res, next) {
  const { projectName } = req.params
  try {
    const getStory = await Story.find({ projectName })
    res.json(getStory)
  } catch (err) {
    res.json(err)
    next(err)
  }
}

module.exports.updateStory = async function updateStory (req, res, next) {
  const { storyId } = req.params
  try {
    const storyDoc = await Story.updateOne({ _id: storyId }, req.body)
    res.json(storyDoc)
  } catch (err) {
    res.json(err)
    next(err)
  }
}

module.exports.deleteStory = async function deleteStory (req, res, next) {
  const { storyId } = req.params
  try {
    const storyDoc = await Story.deleteOne({ _id: storyId })
    res.json(storyDoc)
  } catch (err) {
    res.json(err)
    next(err)
  }
}

const buildStoryFile = function buildStoryFile(stories){
  var storyfile = ""
  for (let i = 0; i < stories.length; i++) {
    storyfile += "## Story for " + stories[i]["nameIntent"] + "\n";
    storyfile += "* " + stories[i]["nameIntent"] + "\n";
    storyfile += "  - " + stories[i]["nameUtter"] + "\n\n";
  }
  return storyfile
}

module.exports.generateStoryFile = async function generateStoryFile(req, res, next) {
  const { projectName } = req.params
  try {
    const getStory = await Story.find({ projectName })

    const storyFile = await buildStoryFile(getStory);
    if (!fs.existsSync("/" + projectName)) {
      fs.mkdirSync("/" + projectName);
    }
    if (!fs.existsSync("/" + projectName + "/data")) {
      fs.mkdirSync("/" + projectName + "/data");
    }
    const file = "/" + projectName + "/data/stories.md"

    fs.writeFile(file, storyFile, function (err) {
      if (err) {
        res.json({ success: false, message: err })
      }

      res.json({success: true, message: "The story file was saved!"})
    });
  } catch (err) {
    res.json({ success: false, message: err })
    next(err)
  }
}
