import os
import json

from fileSet import userSet1
from fileQueue import userQueue1
from requestMaker import apiRequest

class bfsCrawler():
    def __init__(self, info):
        self.obj = apiRequest()

        self.q = userQueue1(info["queuePath"])
        self.visisted = userSet1(info["completedPath"])
        self.limit = info["limit"]
        self.outputPath = info["outputPath"]

    def crawl(self):
        while self.visisted.getUserCount() < self.limit:
            user = self.q.popUser()
            if self.visisted.isPresent(user): continue
            
            followers = following = []
            try:
                followers = self.obj.getFollowers(user)
                following = self.obj.getFollowing(user)
            except Exception as exp:
                print(exp.args[0])
                print(exp.args[1].text)
                self.q.addUser(user)
                return None
            else:
                self.visisted.addUser(user)

            self.q.addUserList(followers)
            self.q.addUserList(following)

            userData = {
                "user": user,
                "followers": followers,
                "following": following
            }

            with open(os.path.join(self.outputPath, "{}.json".format(user)), "w") as fileHandle:
                json.dump(userData, fileHandle, indent = 4)




        
