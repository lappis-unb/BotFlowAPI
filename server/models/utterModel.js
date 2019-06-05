const mongoose = require('../config/connectDB')

const { Schema } = mongoose

const Utter = function utterModelCreate () {
  const UtterSchema = new Schema(
    {
      utters: [{ utterText: { type: String, required: true }, order: { type: Number, required: true } }],
      nameUtter: { type: String, required: true },
      projectName: { type: String, required: true }
    },
    { collection: 'utters' }
  )
  const UtterModel = mongoose.model('Utter', UtterSchema)
  return UtterModel
}
module.exports.Utter = new Utter()
