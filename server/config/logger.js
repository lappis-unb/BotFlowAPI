const fs = require('fs');
const { Console } = require('console');

const loggerOutput = fs.createWriteStream('./stdout.log');
const errorOutput = fs.createWriteStream('./stderr.log');

module.exports.logger = new Console({ stdout: loggerOutput, stderr: errorOutput });
