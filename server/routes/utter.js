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
 * @property {string} text.required
 */
/**
 * @typedef UtterText
 * @property {Array.<Text>} utterText.required
 */

/**
 * @typedef Utter
 * @property {Array.<UtterText>} utters.required
 * @property {string} nameUtter.required
 */

/**
 * @typedef UtterReturnGet
 * @property {string} _id.required
 * @property {Array.<UtterText>} utters.required
 * @property {string} nameUtter.required
 * @property {string} project_name.required
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
 * @route GET /{project_name}/utter
 * @group Utter - Operations about utters
 * @param {string} project_name.path.required - name of project - eg: testeRasa
 * @returns {Array.<UtterReturnGet>} 200 - An array of utters info
 * @returns {Error}  default - Unexpected error
 */

/**
 * @route POST /{project_name}/utter
 * @group Utter - Operations about utters
 * @param {string} project_name.path.required - name of project - eg: testeRasa
 * @param {Utter.model} utter.body.required
 * @returns {Array.<UtterReturnGet>} 200 -  An array of object of utter included
 * @returns {Error}  default - Unexpected error
 */

/**
 * @route PUT /utter/{utterId}
 * @group Utter - Operations about utters
 * @param {string} utterId.path.required - id of utter - eg: 1c24gdq2135s
 * @param {Utter.model} utter.body.required
 * @returns {ReturnPut.model} 200 - An object of numbers of documents modified and if status is ok
 * @returns {Error}  default - Unexpected error
 */

/**
 * @route DELETE /utter/{utterId}
 * @group Utter - Operations about utters
 * @param {string} utterId.path.required - id of utter - eg: 1c24gdq2135s
 * @returns {ReturnDelete.model} 200 - An object of numbers of documents deleted and if status is ok
 * @returns {Error}  default - Unexpected error
 */

app
  .route('/:project_name/utter')
  .post(createUtter)
  .get(getAllUtters)
app
  .route('/utter/:utter_id')
  .put(updateUtter)
  .delete(deleteUtter)

module.exports = app
