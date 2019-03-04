
function User(params = {}) {
  this.firstName = params.firstName;
  this.lastName = params.lastName;
  this.email = params.email;
};

User.prototype.save = async () => {
  return this;
};

User.findById = async (userId) => {
  return userId;
};

module.exports = User;