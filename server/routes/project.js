const express = require('express')

const app = express.Router()
const {
  createProject,
  updateProject,
  deleteProject
} = require('../controllers/projectController.js')

/**
 * @typedef Project
 * @property {string} nameProject.required
 * @property {string} descriptionProject.required
 */

/**
 * @typedef ReturnPut
 * @property {string} n.required
 * @property {string} nModified.required
 * @property {string} ok.required
 */

/**
 * @typedef ReturnDelete
 * @property {string} n.required
 * @property {string} deletedCount.required
 * @property {string} ok.required
 */

/**
 * @route POST /project
 * @group Project - Operations about project
 * @param {string} nameProject.path.required - name of project - eg: testeRasa
 * @param {string} descriptionProject.path.required - description of project - eg: rasa-nlu
 * @param {Project.model} project.body.required
 * @returns {Array.<ProjectReturnGet>} 200 - An array of object of project included
 * @returns {Error}  default - Unexpected error
 */

/**
 * @route PUT /project/{projectId}
 * @group Project - Operations about projects
 * @param {string} projectId.path.required - id of project - eg: 1c24gdq2135s
 * @param {Project.model} project.body.required
 * @returns {ReturnPut.model} 200 - An object of numbers of documents modified and if status is ok
 * @returns {Error}  default - Unexpected error
 */

/**
 * @route DELETE /project/{projectId}
 * @group Project - Operations about projects
 * @param {string} projectId.path.required - id of project - eg: 1c24gdq2135s
 * @returns {ReturnDelete.model} 200 - An object of numbers of documents deleted and if status is ok
 * @returns {Error}  default - Unexpected error
 */

app
  .route('/project')
  .post(createProject)
app
  .route('/project/{projectId}')
  .put(updateProject)
  .delete(deleteProject)

module.exports = app
