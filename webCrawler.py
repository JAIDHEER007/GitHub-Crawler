import os
import requests
import json

from fileSet import userSet1
from fileQueue import userQueue1

followersUrl = "https://api.github.com/users/{username}/followers"
followingUrl = "https://api.github.com/users/{username}/following"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Host": "api.gtihub.com",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.6"
}

def getData(url, username):
    response = requests.get(url = url.format(username = username))
    if response.status_code != 200:
        raise Exception("Network Error")
    
    data = json.loads(response.text)
    return [user["login"] for user in data]

class bfsCrawler():
    def __init__(self, info):
    
        self.q = userQueue1(info["queuePath"])
        self.visisted = userSet1(info["completedPath"])
        self.limit = info["limit"]
        self.outputPath = info["outputPath"]

    def crawl(self):
        while self.visisted.getUserCount() < self.limit:
            user = self.q.popUser()

            if self.visisted.isPresent(user): continue

            self.visisted.addUser(user)

            followers = getData(followersUrl, user)
            following = getData(followingUrl, user)

            self.q.addUserList(followers)
            self.q.addUserList(following)

            userData = {
                "user": user,
                "followers": followers,
                "following": following
            }

            with open(os.path.join(self.outputPath, "{}.json".format(user)), "w") as fileHandle:
                json.dump(userData, fileHandle, indent = 4)




        
