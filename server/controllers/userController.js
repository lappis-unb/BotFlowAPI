const { hashSync } = require('bcrypt')
const User = require('../models/userModel')

module.exports.createUser = async function createUser (req, res, next) {
  const jsonObject = req.body
  jsonObject.password = hashSync(jsonObject.password, 10)
  try {
    const saveUser = await User.collection.insertOne(jsonObject)
    res.json(saveUser.ops)
  } catch (err) {
    res.json(err)
    next(err)
  }
}
