const express = require('express');

const app = express.Router();
const { getAllCollections, insertAllCollections } = require('../controllers/projectControler');

app.post('/:projectName/upload', insertAllCollections);
app.get('/:projectName/info', getAllCollections);

module.exports = app;
