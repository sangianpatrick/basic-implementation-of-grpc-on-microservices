import grpc
import json

# import grpc generated classes
import user_pb2
import user_pb2_grpc

# open grpc channel to user grpc server
channel = grpc.insecure_channel('localhost:9001')
stub = user_pb2_grpc.UserServiceStub(channel)

def get_user_list():
  params = user_pb2.Empty()
  res = stub.GetUserList(params)
  print(res.users)

def get_user_by_id():
  params = user_pb2.RequestById(user_id='6b08ed88-0c68-4740-93f1-139c258ef3eb')
  response = stub.GetUserById(params)
  print(response.first_name)

get_user_list()
get_user_by_id()