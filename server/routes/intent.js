const express = require('express')

const app = express.Router()
const {
  createIntent,
  getAllIntents,
  updateIntent,
  deleteIntent
} = require('../controllers/intentController')

/**
 * @typedef Entity
 * @property {integer} start.required
 * @property {integer} end.required
 * @property {string} value.required
 * @property {string} entity.required
 */

/**
 * @typedef Intent
 * @property {string} intent.required
 * @property {string} nameIntent.required
 * @property {Array.<Entity>} entities
 */

/**
 * @typedef IntentReturnGet
 * @property {string} _id.required
 * @property {string} intent.required
 * @property {string} nameIntent.required
 * @property {string} projectName.required
 * @property {Array.<Entity>} entities
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
 * @route GET project/{projectId}/intent
 * @group Intent - Operations about intents
 * @param {string} projectName.path.required - name of project - eg: testeRasa
 * @returns {Array.<IntentReturnGet>} 200 - An array of intents info
 * @returns {Error}  default - Unexpected error
 */

/**
 * @route POST project/{projectId}/intent
 * @group Intent - Operations about intents
 * @param {string} projectName.path.required - name of project - eg: testeRasa
 * @param {Intent.model} intent.body.required
 * @returns {Array.<IntentReturnGet>} 200 - An array of object of utter included
 * @returns {Error}  default - Unexpected error
 */

/**
 * @route PUT project/{projectId}/intent/{intentId}
 * @group Intent - Operations about intents
 * @param {string} intentId.path.required - id of intent - eg: 1c24gdq2135s
 * @param {Intent.model} intent.body.required
 * @returns {ReturnPut.model} 200 - An object of numbers of documents modified and if status is ok
 * @returns {Error}  default - Unexpected error
 */

/**
 * @route DELETE project/{projectId}/intent/{intentId}
 * @group Intent - Operations about intents
 * @param {string} intentId.path.required - id of intent - eg: 1c24gdq2135s
 * @returns {ReturnDelete.model} 200 - An object of numbers of documents deleted and if status is ok
 * @returns {Error}  default - Unexpected error
 */

app
  .route('project/:projectId/intent')
  .post(createIntent)
  .get(getAllIntents)
app
  .route('project/:projectId/intent/:intentId')
  .put(updateIntent)
  .delete(deleteIntent)

module.exports = app

// paths:
//   /{projectName}/upload:
//     post:
//       summary: Post a json with stories, intents and utters
//       parameters:
//         - in: path
//           name: projectName
//           type: string
//           required: true
//       description: Post a list containing an array of stories, intents and utters of an project
//       responses:
//         200:
//           description: A list of stories, intents and utters
//           schema:
//             type: object
//             required:
//               - intents
//               - utters
//               - stories
//             properties:
//               intents:
//                 type: array
//                 items:
//                   type: object
//                   properties:
//                     _id:
//                       type: string
//                     intentName:
//                       type: string
//                     intent:
//                       type: string
//                     entities:
//                       type: array
//                       items:
//                         type: object
//                         properties:
//                           start:
//                             type: integer
//                           end:
//                             type: integer
//                           value:
//                             type: string
//                           entity:
//                             type: string
//               utters:
//                 type: array
//                 items:
//                   type: object
//                   properties:
//                     _id:
//                       type: string
//                     utterName:
//                       type: string
//                     utter:
//                       type: string
//               stories:
//                 type: array
//                 items:
//                   type: object
//                   properties:
//                     _id:
//                       type: string
//                     utterName:
//                       type: string
//                     intentName:
//                       type: string
//   /{projectName}/info:
//     get:
//       summary: Get a json with stories, intents and utters
//       parameters:
//         - in: path
//           name: projectName
//           type: string
//           required: true
//       description: Get a list containing an array of stories, intents and utters of an project
//       responses:
//         200:
//           description: A list of stories, intents and utters
//           schema:
//             type: object
//             required:
//               - intents
//               - utters
//               - stories
//             properties:
//               intents:
//                 type: array
//                 items:
//                   type: object
//                   properties:
//                     _id:
//                       type: string
//                     intentName:
//                       type: string
//                     intent:
//                       type: string
//                     entities:
//                       type: array
//                       items:
//                         type: object
//                         properties:
//                           start:
//                             type: integer
//                           end:
//                             type: integer
//                           value:
//                             type: string
//                           entity:
//                             type: string
//               utters:
//                 type: array
//                 items:
//                   type: object
//                   properties:
//                     _id:
//                       type: string
//                     utterName:
//                       type: string
//                     utter:
//                       type: string
//               stories:
//                 type: array
//                 items:
//                   type: object
//                   properties:
//                     _id:
//                       type: string
//                     utterName:
//                       type: string
//                     intentName:
//                       type: string
//   project/{projectId}/intent:
//     get:
//       summary: Get a JSON with intents
//       parameters:
//         - in: path
//           name: projectName
//           type: string
//           required: true
//       description: Get a JSON with all intents of a project
//       responses:
//         200:
//           description: A list of intents
//           schema:
//             type: array
//             items:
//               type: object
//               properties:
//                 _id:
//                   type: string
//                 nameIntent:
//                   type: string
//                 intent:
//                   type: string
//                 entities:
//                       type: array
//                       items:
//                         type: object
//                         properties:
//                           start:
//                             type: integer
//                           end:
//                             type: integer
//                           value:
//                             type: string
//                           entity:
//                             type: string
//     post:
//       summary: Post a JSON with intent
//       parameters:
//         - in: path
//           name: projectName
//           type: string
//           required: true
//       description: Post a JSON with intent of a project
//       responses:
//         200:
//           description: A list of intents
//           schema:
//             type: array
//             items:
//               type: object
//               properties:
//                 _id:
//                   type: string
//                 nameIntent:
//                   type: string
//                 intent:
//                   type: string
//                 entities:
//                       type: array
//                       items:
//                         type: object
//                         properties:
//                           start:
//                             type: integer
//                           end:
//                             type: integer
//                           value:
//                             type: string
//                           entity:
//                             type: string
//   /intent/{intentId}:
//     put:
//       summary: Update a intent
//       parameters:
//         - in: path
//           name: intentId
//           type: string
//           required: true
//       description: Update a intent of a project
//       responses:
//         200:
//           description: A object of intents updated
//           schema:
//             type: object
//             properties:
//               n:
//                 type: string
//               ok:
//                 type: string
//               nModified:
//                 type: string
//     delete:
//       summary: Delete a intent
//       parameters:
//         - in: path
//           name: intentId
//           type: string
//           required: true
//       description: Delete a intent of a project
//       responses:
//         200:
//           description: A object of intent removed
//           schema:
//             type: object
//             properties:
//               n:
//                 type: string
//               ok:
//                 type: string
//               deletedCount:
//                 type: string
