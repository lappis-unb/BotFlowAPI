const { Intent } = require('../models/intentModel')
const { Utter } = require('../models/utterModel')

const fs = require('fs');

const buildDomainFile = function buildDomainFile(intents, utters) {
    var domainfile = ""
    var intents_list = []
    var entities = []

    for (let i = 0; i < intents.length; i++) {
        const intent = intents[i];
        if (!intents_list.includes(intent["nameIntent"])){
            intents_list.push(intent["nameIntent"]);
        }
        if (intent["entities"] != undefined){
            for (let j = 0; j < intent["entities"].length; j++){
                if (!entities.includes(intent["entities"][j]["entity"])){
                    entities.push(intent["entities"][j]["entity"])
                }
            }
        }
    }

    domainfile = "intents:\n"
    for (let i = 0; i < intents_list.length; i++) {
        const intent = intents_list[i];
        domainfile += "  - " + intent + "\n";
    }

    if(entities.length > 0){
        domainfile += "\nentities:\n"
    }
    for (let i = 0; i < entities.length; i++) {
        const entity = entities[i];
        domainfile += "  - " + entity + "\n";
    }
    
    domainfile += "\ntemplates:\n"
    for (let i = 0; i < utters.length; i++) {
        const utter = utters[i]["nameUtter"];
        const text = utters[i]["utter"];
        domainfile += "  " + utter + ":\n";
        domainfile += "    - text: | \n"
        domainfile += "          " + text + "\n\n"
    }

    domainfile += "actions:\n"
    for (let i = 0; i < utters.length; i++) {
        const utter = utters[i]["nameUtter"];
        domainfile += "  - " + utter + "\n";
    }

    return domainfile
}

module.exports.generateDomainFile = async function generateDomainFile(req, res, next) {
    const { projectName } = req.params
    try {
        const intents = await Intent.find({ projectName })
        const utters = await Utter.find({ projectName })

        const storyFile = await buildDomainFile(intents, utters);
        if (!fs.existsSync("/" + projectName)) {
            fs.mkdirSync("/" + projectName);
        }
        const file = "/" + projectName + "/domain.yml"

        fs.writeFile(file, storyFile, function (err) {
            if (err) {
                res.json({ success: false, message: err })
            }
            res.download(file)
        });
    } catch (err) {
        res.json({ success: false, message: err })
        next(err)
    }
}