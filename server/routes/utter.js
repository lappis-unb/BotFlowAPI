const express = require('express')

const app = express.Router()
const {
  createUtter,
  getAllUtters,
  updateUtter,
  deleteUtter
} = require('../controllers/utterController')

/**
 * @typedef Text
 * @property {string} utterText.required
 * @property {integer} order.required
 */

/**
 * @typedef Utter
 * @property {Array.<Text>} utters.required
 * @property {string} nameUtter.required
 */

/**
 * @typedef UtterReturnGet
 * @property {string} _id.required
 * @property {Array.<Text>} utters.required
 * @property {string} nameUtter.required
 * @property {string} projectName.required
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
 * This function comment is parsed by doctrine
 * @route GET project/{projectId}/utter
 * @group Utter - Operations about utters
 * @param {string} projectName.path.required - name of project - eg: testeRasa
 * @returns {Array.<UtterReturnGet>} 200 - An array of utters info
 * @returns {Error}  default - Unexpected error
 */

/**
 * @route POST project/{projectId}/utter
 * @group Utter - Operations about utters
 * @param {string} projectName.path.required - name of project - eg: testeRasa
 * @param {Utter.model} utter.body.required
 * @returns {Array.<UtterReturnGet>} 200 -  An array of object of utter included
 * @returns {Error}  default - Unexpected error
 */

/**
 * @route PUT project/{projectId}/utter/{utterId}
 * @group Utter - Operations about utters
 * @param {string} utterId.path.required - id of utter - eg: 1c24gdq2135s
 * @param {Utter.model} utter.body.required
 * @returns {ReturnPut.model} 200 - An object of numbers of documents modified and if status is ok
 * @returns {Error}  default - Unexpected error
 */

/**
 * @route DELETE project/{projectID}/utter/{utterId}
 * @group Utter - Operations about utters
 * @param {string} utterId.path.required - id of utter - eg: 1c24gdq2135s
 * @returns {ReturnDelete.model} 200 - An object of numbers of documents deleted and if status is ok
 * @returns {Error}  default - Unexpected error
 */

app
  .route('project/:projectId/utter')
  .post(createUtter)
  .get(getAllUtters)
app
  .route('project/projectId/utter/:utterId')
  .put(updateUtter)
  .delete(deleteUtter)

module.exports = app
