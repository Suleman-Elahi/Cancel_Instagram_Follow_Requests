from instagram_private_api import Client, ClientCompatPatch
import loginInfo
import time


api = Client(loginInfo.username, loginInfo.password)

f = open("follow_req.txt", "r").read().split("\n")

i=0
for x in f:
  if bool(x):
      user_info = api.username_info(x)
      uid = user_info['user']['pk']
      api.friendships_destroy(uid)
      i+=1
      print ("Follow request "+ str(i)+" cancelled for: "+x)
