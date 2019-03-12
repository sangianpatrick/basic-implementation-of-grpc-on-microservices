const protoPath = __dirname + '/../../user.proto';
const grpc = require('grpc');
const { host: userServiceHost, port: userServicePort } = require('../../config/global').userService;

const UserService = grpc.load(protoPath).UserService
const grpcClient = new UserService(`${userServiceHost}:${userServicePort}`, grpc.credentials.createInsecure());

function User(params = {}) {
  this.props = {
    first_name: params.firstName,
    last_name: params.lastName,
    email: params.email
  }
};

User.prototype.save = async () => {
  return this;
};

User.findAll = () => {
  return new Promise((resolve, reject) => {
    grpcClient.getUserList({}, (err, response) => {
      if (err) {
        console.log(err);
        const error = new Error('Error to retrieve user list');
        error.name = 'GrpcRetrieveError'
        error.message = err
        reject(error)
      }
      const data = {
        success: true,
        data: response.users,
        message: 'User List'
      }
      resolve(data)
    });
  })
}

User.findById = async (userId) => {
  return userId;
};

module.exports = User;