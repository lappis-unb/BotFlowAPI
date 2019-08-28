const mongoose = require('../config/connectDB')

const { Schema } = mongoose

const Utter = function utterModelCreate() {
  const UtterSchema = new Schema(
    {
      alternatives: [{ contents: [{ text: { type: String, required: true } }] }],
      name: { type: String, required: true },
      project_name: { type: String, required: true }
    },
    { collection: 'utters' }
  )
  const UtterModel = mongoose.model('Utter', UtterSchema)
  return UtterModel
}
module.exports.Utter = new Utter()
