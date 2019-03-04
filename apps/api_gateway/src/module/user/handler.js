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

module.exports = {
  getProfile
}