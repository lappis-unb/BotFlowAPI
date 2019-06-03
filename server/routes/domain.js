const express = require('express')

const app = express.Router()
const {
    generateDomainFile
} = require('../controllers/domainController.js')

/**
 * This function comment is parsed by doctrine
 * @route GET /{projectName}/domain/generate_file
 * @group Domain - Operations about domain
 * @param {string} projectName.path.required - name of project - eg: testeRasa
 * @returns {BinaryType} 200 - Domain file
 * @returns {Error}  default - Unexpected error
 */


app
    .route('/:projectName/domain/generate_file')
    .get(generateDomainFile)

module.exports = app