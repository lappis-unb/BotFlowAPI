const express = require('express')

const { createSession } = require('../controllers/sessionController')
const app = express.Router()

app.route('/login').post(createSession)

module.exports = app
