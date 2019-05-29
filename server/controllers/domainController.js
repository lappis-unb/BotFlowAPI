const { Intent } = require('../models/intentModel')
const { Utter } = require('../models/utterModel')

const fs = require('fs');

const buildDomainFile = function buildDomainFile(intents, utters) {
    var storyfile = ""
    storyfile += "intents:\n"
    for (let i = 0; i < intents.length; i++) {
        const intent = intents[i];
        storyfile += "  - " + intent["intent"] + "\n";
    }
    storyfile += "\actions:\n"
    for (let i = 0; i < utters.length; i++) {
        const utter = utters[i]["nameUtter"];
        storyfile += "  - " + utter + "\n";
    }
    return storyfile
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

            res.json({ success: true, message: "The domain file was saved!" })
        });
    } catch (err) {
        res.json({ success: false, message: err })
        next(err)
    }
}