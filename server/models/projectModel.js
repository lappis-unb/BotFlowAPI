const mongoose = require('../config/connectDB')

const { Schema } = mongoose

const Project = function projectModelCreate () {
  const ProjectSchema = new Schema(
    {
      nameProject: { type: String, required: true },
      descriptionProject: { type: String, required: true }
    },
    { collection: 'projects' }
  )
  const ProjectModel = mongoose.model('Project', ProjectSchema)
  return ProjectModel
}
module.exports.Project = new Project()
