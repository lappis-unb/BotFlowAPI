const { Project } = require('../models/projectModel')

module.exports.createProject = async function createProject (req, res, next) {
  const json_object = req.body
  try {
    const save_project = await Project.collection.insertOne(json_object)
    res.json(save_project.ops)
  } catch (err) {
    res.json(err)
    next(err)
  }
}

module.exports.updateProject = async function updateProject (req, res, next) {
  const { project_id } = req.params
  try {
    const project_doc = await Project.updateOne({ _id: project_id }, req.body)
    res.json(project_doc)
  } catch (err) {
    res.json(err)
    next(err)
  }
}

module.exports.deleteProject = async function deleteProject (req, res, next) {
  const { project_id } = req.params
  try {
    const project_doc = await Project.deleteOne({ _id: project_id })
    res.json(project_doc)
  } catch (err) {
    res.json(err)
    next(err)
  }
}