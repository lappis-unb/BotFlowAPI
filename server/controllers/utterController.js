const { Utter } = require('../models/utterModel')

module.exports.createUtter = async function createUtter(req, res, next) {
  const json_object = req.body
  json_object.project_name = req.params.project_name

  let regex = (/^(([A-Z]|[a-z]|[0-9]|_)*)$/)
  let name = json_object.name

  if (regex.test(name)) {
    try {
      const save_utter = await Utter.collection.insertOne(json_object)
      res.json(save_utter.ops)
    } catch (err) {
      next(err)
    }
  } else {
    res.status(400).json({
      message: "Utter name shouldn't have special characters or spaces"
    })
  }
}

module.exports.getAllUtters = async function getAllUtters(req, res, next) {
  const { project_name } = req.params
  try {
    const get_utter = await Utter.find({ project_name })
    res.json(get_utter)
  } catch (err) {
    res.json(err)
    next(err)
  }
}

module.exports.updateUtter = async function updateUtter(req, res, next) {
  const { utter_id } = req.params
  var regex = /^(([A-Z]|[a-z]|[0-9]|_)*)$/;
  var name = req.body.name;

  if (regex.test(name)) {
    try {
      const utter_doc = await Utter.updateOne({ _id: utter_id }, req.body)
      res.json(utter_doc)
    } catch (err) {
      res.json(err)
      next(err)
    }
  } else {
    res.status(400).json({
      message: "Utter name shouldn't have special characters or spaces"
    })
  }
}

module.exports.deleteUtter = async function deleteUtter(req, res, next) {
  const { utter_id } = req.params
  try {
    const utter_doc = await Utter.deleteOne({ _id: utter_id })
    res.json(utter_doc)
  } catch (err) {
    res.json(err)
    next(err)
  }
}
