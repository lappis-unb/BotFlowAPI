const { Intent } = require('../models/intentModel')

module.exports.createIntent = async function createIntent (req, res, next) {
  const jsonObject = req.body
  jsonObject.projectName = req.params.projectName
  try {
    const saveIntent = await Intent.collection.insertOne(jsonObject)
    res.json(saveIntent.ops)
  } catch (err) {
    res.json(err)
    next(err)
  }
}

module.exports.getAllIntents = async function getAllIntents (req, res, next) {
  const { projectName } = req.params
  try {
    const getIntent = await Intent.find({ projectName })
    res.json(getIntent)
  } catch (err) {
    res.json(err)
    next(err)
  }
}

module.exports.updateIntent = async function updateIntent (req, res, next) {
  const { intentId } = req.params
  try {
    const intentDoc = await Intent.updateOne({ _id: intentId }, req.body)
    res.json(intentDoc)
  } catch (err) {
    res.json(err)
    next(err)
  }
}

module.exports.deleteIntent = async function deleteIntent (req, res, next) {
  const { intentId } = req.params
  try {
    const intentDoc = await Intent.deleteOne({ _id: intentId })
    res.json(intentDoc)
  } catch (err) {
    res.json(err)
    next(err)
  }
}
