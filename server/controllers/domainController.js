const { Intent } = require('../models/intentModel')
const { Utter } = require('../models/utterModel')

const fs = require('fs')

const buildDomainFile = function buildDomainFile(intents, utters) {
  let domainfile = ''
  let intents_list = []
  let entities = []

  for (let i = 0; i < intents.length; i++) {
    const intent = intents[i]
    if (!intents_list.includes(intent['name'])) {
      intents_list.push(intent['name'])
    }
    if (intent['entities'] !== undefined) {
      for (let j = 0; j < intent['entities'].length; j++) {
        if (!entities.includes(intent['entities'][j]['entity'])) {
          entities.push(intent['entities'][j]['entity'])
        }
      }
    }
  }

  domainfile = 'intents:\n'
  for (let i = 0; i < intents_list.length; i++) {
    const intent = intents_list[i]
    domainfile += '  - ' + intent + '\n'
  }

  if (entities.length > 0) {
    domainfile += '\nentities:\n'
  }
  for (let i = 0; i < entities.length; i++) {
    const entity = entities[i]
    domainfile += '  - ' + entity + '\n'
  }

  domainfile += '\ntemplates:\n'
  for (let i = 0; i < utters.length; i++) {
    const utter = utters[i]['name']
    domainfile += '  ' + utter + ':\n'
    for (let j = 0; j < utters[i]['alternatives'].length; j++) {
      domainfile += '    - text: | \n'
      for (let k = 0; k < utters[i]['alternatives'][j]['contents'].length; k++) {
        domainfile += '          ' + utters[i]['alternatives'][j]['contents'][k]['text'] + '\n\n'

      }
    }
  }

  domainfile += 'actions:\n'
  for (let i = 0; i < utters.length; i++) {
    const utter = utters[i]['name']
    domainfile += '  - ' + utter + '\n'
  }

  return domainfile
}

module.exports.generateDomainFile = async function generateDomainFile(req, res, next) {
  const { project_name } = req.params
  try {
    const intents = await Intent.find({ project_name })
    const utters = await Utter.find({ project_name })

    const storyFile = await buildDomainFile(intents, utters)
    if (!fs.existsSync('/' + project_name)) {
      fs.mkdirSync('/' + project_name)
    }
    const file = '/' + project_name + '/domain.yml'

    fs.writeFile(file, storyFile, function (err) {
      if (err) {
        res.json({ success: false, message: err })
      }
      res.download(file)
    })
  } catch (err) {
    res.json({ success: false, message: err })
    next(err)
  }
}
