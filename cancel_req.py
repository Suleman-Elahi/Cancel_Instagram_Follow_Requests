from instagram_private_api import Client, ClientCompatPatch
import loginInfo

api = Client(loginInfo.username, loginInfo.password)

f = open("follow_req.txt", "r").read().split("\n")

for x in f:
  if bool(x):
    user_info = api.username_info(x)
    uid = user_info['user']['pk']
    api.friendships_destroy(uid)
    print ("Follow request cancelled for: "+x)