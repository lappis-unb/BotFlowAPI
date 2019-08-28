const { Intent } = require('../models/intentModel')

module.exports.createIntent = async function createIntent (req, res, next) {
  const json_object = req.body
  json_object.project_name = req.params.project_name
  try {
    const save_intent = await Intent.collection.insertOne(json_object)
    res.json(save_intent.ops)
  } catch (err) {
    res.json(err)
    next(err)
  }
}

module.exports.getAllIntents = async function getAllIntents (req, res, next) {
  const { project_name } = req.params
  try {
    const get_intent = await Intent.find({ project_name })
    res.json(get_intent)
  } catch (err) {
    res.json(err)
    next(err)
  }
}

module.exports.updateIntent = async function updateIntent (req, res, next) {
  const { intent_id } = req.params
  try {
    const intent_doc = await Intent.updateOne({ _id: intent_id }, req.body)
    res.json(intent_doc)
  } catch (err) {
    res.json(err)
    next(err)
  }
}

module.exports.deleteIntent = async function deleteIntent (req, res, next) {
  const { intent_id } = req.params
  try {
    const intent_doc = await Intent.deleteOne({ _id: intent_id })
    res.json(intent_doc)
  } catch (err) {
    res.json(err)
    next(err)
  }
}
