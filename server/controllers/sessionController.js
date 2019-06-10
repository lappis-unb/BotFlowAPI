const { compare } = require('bcrypt')
const assert = require('assert')
const jwt = require('jsonwebtoken')
const fs = require('fs')
const path = require('path')

const User = require('../models/userModel')
const certPath = path.join(__dirname, '../private/jwtRS256.key')
const privateKey = fs.readFileSync(certPath, 'utf8')

async function verifyUser ({ email, password }) {
  let result
  const getUser = await User.collection.find({ email })
  try {
    assert('email' in getUser)
    const { password: passwordUser } = getUser
    compare(password, passwordUser, (err, res) => {
      if (err) {
        throw err
      }
      result = res
    })
  } catch (err) {
    result = false
  }
  return result
}
module.exports.createSession = async function createSession (req, res, next) {
  const userVerify = verifyUser(req.body)
  if (!userVerify) {
    res.json('Usuário não encontrado')
    next(userVerify)
  }
  const { email } = req.body
  try {
    const token = jwt.sign(email, privateKey, { algorithm: 'RS256' })
    res.json({ token })
  } catch (err) {
    res.json(err)
    next(err)
  }
}
