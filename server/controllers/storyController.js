const { Story } = require('../models/storyModel');

module.exports.createStory = async function createStory(req, res, next) {
  const jsonObject = req.body;
  jsonObject.projectName = req.params.projectName;
  try {
    const saveStory = await Story.collection.insertOne(jsonObject);
    res.json(saveStory.ops);
  } catch (err) {
    next(err);
  }
};

module.exports.getAllStories = async function getAllStories(req, res, next) {
  const { projectName } = req.params;
  try {
    const getStory = await Story.find({ projectName });
    res.json(getStory);
  } catch (err) {
    res.json(err);
    next(err);
  }
};

module.exports.updateStory = async function updateStory(req, res, next) {
  const { storyId } = req.params;
  try {
    const storyDoc = await Story.updateOne({ _id: storyId }, req.body);
    res.json(storyDoc);
  } catch (err) {
    res.json(err);
    next(err);
  }
};

module.exports.deleteStory = async function deleteStory(req, res, next) {
  const { storyId } = req.params;
  try {
    const storyDoc = await Story.deleteOne({ _id: storyId });
    res.json(storyDoc);
  } catch (err) {
    res.json(err);
    next(err);
  }
};
