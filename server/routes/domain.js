const express = require('express')

const app = express.Router()
const {
    generateDomainFile
} = require('../controllers/domainController.js')

app
    .route('/:projectName/domain/generate_file')
    .get(generateDomainFile)

module.exports = app