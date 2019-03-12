const express = require('express');
const server = express();
const cors = require('cors');
const bodyParser = require('body-parser');
const logger = require('morgan')
require('dotenv').config();

// handlers
const user = require('./module/user/handler');

server.use(logger('dev'));
server.use(bodyParser.urlencoded({ extended: false }));
server.use(cors());

server.get('/', (_, res) => {
  res.status(200)
    .json({
      error: false,
      message: 'Connected to app.',
      code: 200
    });
});

// user service
server.get('/users/:userId', user.getProfile);
server.get('/users', user.getUserList);

// not found handler
server.use('*', (req, res) => {
  res.status(404)
    .json({
      error: true,
      message: `This url: "${req.originalUrl}" was not found.`,
      code: 404
    });
});

// error handler
server.use((err, _, res) => {
  res.status(500)
    .json({
      error: true,
      message: err,
      code: 500
    });
});

server.listen(process.env.PORT, () => {
  console.log(`API Gateway is running on port ${process.env.PORT}`);
});
