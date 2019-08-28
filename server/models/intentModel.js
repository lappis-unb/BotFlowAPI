const mongoose = require('../config/connectDB')

const { Schema } = mongoose

const Intent = function IntentModelCreate() {
  const EntitySchema = new Schema({
    start: { type: Number, required: true },
    end: { type: Number, required: true },
    value: { type: String, required: true },
    entity: { type: String, required: true }
  })
  const IntentSchema = new Schema(
    {
      questions: [{ text: { type: String, required: true } }],
      name: { type: String, index: true, required: true },
      project_name: { type: String, required: true },
      entities: [EntitySchema]
    },
    { collection: 'intents' }
  )
  const IntentModel = mongoose.model('Intent', IntentSchema)
  return IntentModel
}
module.exports.Intent = new Intent()
