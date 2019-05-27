const mongoose = require('../config/connectDB')

const { Schema } = mongoose

const Story = function storyModelCreate () {
  const StorySchema = new Schema(
    {
      nameUtter: { type: String, required: true },
      nameIntent: { type: String, required: true },
      projectName: { type: String, required: true }
    },
    { collection: 'stories' }
  )
  const StoryModel = mongoose.model('Story', StorySchema)
  return StoryModel
}
module.exports.Story = new Story()
