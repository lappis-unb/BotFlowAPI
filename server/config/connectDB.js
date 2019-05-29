const mongoose = require('mongoose')
const { logger } = require('./logger')

const options = {
  useCreateIndex: true,
  auth: {
    user: encodeURIComponent(process.env.MONGO_USERNAME),
    password: encodeURIComponent(process.env.MONGO_PASSWORD)
  },
  dbName: process.env.MONGO_DATABASE
}
mongoose.connect('mongodb://mongodb:27017', options, (err) => {
  if (err) logger.error('Error connection:', err)
  logger.log('Connection Succesfull: ', Date.now())
})

module.exports = mongoose
