require('dotenv').config()

module.export = {
  userService: {
    host: process.env.USER_SERVICE_HOST,
    port: process.env.USER_SERVICE_PORT
  },
  articleService: {
    host: process.env.ARTICLE_SERVICE_HOST,
    port: process.env.USER_SERVICE_PORT
  }
};
