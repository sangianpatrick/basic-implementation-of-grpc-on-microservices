const User = require('./model');

const getProfile = async (req, res, next) => {
  const userId = req.params.userId;
  const getUserById = await User.findById(userId);
  res.status(200)
    .json({
      error: false,
      data: getUserById,
      code: 200
    });
}

const getUserList = async (req, res, next) => {
  try {
    const start = Math.floor(new Date())
    const userList = await User.findAll();
    const end = Math.floor(new Date()) - start
    const data = {
      ...userList,
      executionTime: end + 'ms'
    }
    res.status(200)
      .json(data);
  } catch (err) {
    res.status(200)
      .json(err);
  }
}

module.exports = {
  getProfile,
  getUserList
}