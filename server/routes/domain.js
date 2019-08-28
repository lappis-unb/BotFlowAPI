const express = require('express')

const app = express.Router()
const {
    generateDomainFile
} = require('../controllers/domainController.js')

/**
 * This function comment is parsed by doctrine
 * @route GET /{project_name}/domain/generate_file
 * @group Domain - Operations about domain
 * @param {string} project_name.path.required - name of project - eg: testeRasa
 * @returns {BinaryType} 200 - Domain file
 * @returns {Error}  default - Unexpected error
 */


app
    .route('/:project_name/domain/generate_file')
    .get(generateDomainFile)

module.exports = app
