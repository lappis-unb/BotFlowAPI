const express = require('express')
const { verify } = require('jsonwebtoken')

const app = express.Router()
const { getAllCollections, insertAllCollections } = require('../controllers/projectControler')

/**
 * @typedef IntentsUttersStoriesArray
 * @property {Array.<Intent>} Intent this models is inside in respectives routes
 * @property {Array.<Utter>} Utter this models is inside in respectives routes
 * @property {Array.<Story>} Story this models is inside in respectives routes
 */

/**
 * @typedef IntentsUttersStoriesArrayGet
 * @property {Array<IntentGet>} Intent this models is inside in respectives routes
 * @property {Array<UtterGet>} Utter this models is inside in respectives routes
 * @property {Array<StoryGet>} Story this models is inside in respectives routes
 */

/**
 * This function comment is parsed by doctrine
 * @route GET /{projectName}/info
 * @group Project - Operations about intents, utters and stories
 * @param {string} projectName.path.required - name of project - eg: testeRasa
 * @returns {IntentsUttersStoriesArrayGet.model} 200 - An object with all intents, utters and stories
 * @returns {Error}  default - Unexpected error
 */

/**
 * @route POST /{projectName}/upload
 * @group Project - Operations about intents, utters and stories
 * @param {string} projectName.path.required - name of project - eg: testeRasa
 * @param {IntentsUttersStoriesArray.model} utter.body.required
 * @returns {IntentsUttersStoriesArrayGet.model} 200 -  An object with all intents, utters, and stories
 * @returns {Error}  default - Unexpected error
 */

const checkToken = (req, res, next) => {
  const header = req.headers['Authorization']

  if (typeof header !== 'undefined') {
    const bearer = header.split(' ')
    const token = bearer[1]

    req.token = token
    verify(req.token, 'privatekey', (err, authorizedData) => {
      if (err) {
        res.sendStatus(403)
      } else {
        next(authorizedData)
      }
    })
  } else {
    res.sendStatus(403)
  }
}
app.get('/:projectName/info', checkToken, getAllCollections)
app.post('/:projectName/upload', checkToken, insertAllCollections)

module.exports = app
