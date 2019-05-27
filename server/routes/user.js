const express = require('express')

const { createUser } = require('../controllers/userController')
const app = express.Router()

app.route('/new').post(createUser)

module.exports = app
