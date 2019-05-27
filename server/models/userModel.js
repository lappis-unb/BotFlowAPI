const mongoose = require('../config/connectDB')

const { Schema } = mongoose

const User = function UserModelCreate () {
  const UserSchema = new Schema(
    {
      email: { type: String, index: true, required: true },
      password: { type: String, required: true }
    },
    { collection: 'Users' }
  )
  const UserModel = mongoose.model('User', UserSchema)
  return UserModel
}
module.exports = new User()
