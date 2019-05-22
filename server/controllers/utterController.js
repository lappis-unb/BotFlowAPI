const { Utter } = require('../models/utterModel');

module.exports.createUtter = async function createUtter(req, res, next) {
  const jsonObject = req.body;
  jsonObject.projectName = req.params.projectName;
  try {
    const saveUtter = await Utter.collection.insertOne(jsonObject);
    res.json(saveUtter.ops);
  } catch (err) {
    next(err);
  }
};

module.exports.getAllUtters = async function getAllUtters(req, res, next) {
  const { projectName } = req.params;
  try {
    const getUtter = await Utter.find({ projectName });
    res.json(getUtter);
  } catch (err) {
    res.json(err);
    next(err);
  }
};

module.exports.updateUtter = async function updateUtter(req, res, next) {
  const { utterId } = req.params;
  try {
    const utterDoc = await Utter.updateOne({ _id: utterId }, req.body);
    res.json(utterDoc);
  } catch (err) {
    res.json(err);
    next(err);
  }
};

module.exports.deleteUtter = async function deleteUtter(req, res, next) {
  const { utterId } = req.params;
  try {
    const utterDoc = await Utter.deleteOne({ _id: utterId });
    res.json(utterDoc);
  } catch (err) {
    res.json(err);
    next(err);
  }
};
