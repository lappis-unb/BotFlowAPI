const { Project } = require('../models/projectModel')

module.exports.createProject = async function createProject (req, res, next) {
  const jsonObject = req.body
  try {
    const saveProject = await Project.collection.insertOne(jsonObject)
    res.json(saveProject.ops)
  } catch (err) {
    res.json(err)
    next(err)
  }
}

module.exports.updateProject = async function updateProject (req, res, next) {
  const { projectId } = req.params
  try {
    const projectDoc = await Project.updateOne({ _id: projectId }, req.body)
    res.json(projectDoc)
  } catch (err) {
    res.json(err)
    next(err)
  }
}

module.exports.deleteProject = async function deleteProject (req, res, next) {
  const { projectId } = req.params
  try {
    const projectDoc = await Project.deleteOne({ _id: projectId })
    res.json(projectDoc)
  } catch (err) {
    res.json(err)
    next(err)
  }
}