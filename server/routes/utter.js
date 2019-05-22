const express = require('express');

const app = express.Router();
const {
  createUtter,
  getAllUtters,
  updateUtter,
  deleteUtter,
} = require('../controllers/utterController');

app
  .route('/:projectName/utter')
  .post(createUtter)
  .get(getAllUtters);
app
  .route('/utter/:utterId')
  .put(updateUtter)
  .delete(deleteUtter);

module.exports = app;
