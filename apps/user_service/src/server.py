from config import SERVICE
import grpc
from concurrent import futures
import time

# import grpc generated class
import user_pb2
import user_pb2_grpc

# import user model
from user_model import User


class UserService(user_pb2_grpc.UserServiceServicer):
    def GetUserList(self, req, ctx):
        user_list = []

        retrive = User.get_all({}, _id=False)
        if len(retrive) < 1:
            return user_pb2.Empty()
        for user in retrive:
            user_list.append(user_pb2.User(**user))

        res = user_pb2.UserList(users=user_list)
        return res

    def GetUserById(self, req, ctx):
      user_id = req.user_id

      user = User.get_by_id(user_id, _id=False)
      if user is None:
        return user_pb2.Empty()
      
      res = user_pb2.User(**user)
      return res

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)

print('User Service Server is listening on port {}'.format(SERVICE['port']))
server.add_insecure_port('[::]:{}'.format(SERVICE['port']))
server.start()

try:
    while True:
        time.sleep(60*60*24*30)
except KeyboardInterrupt:
    server.stop(0)
