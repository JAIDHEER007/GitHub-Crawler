import requests
import json

class apiRequest():
    __followersUrl = "https://api.github.com/users/{username}/followers"
    __followingUrl = "https://api.github.com/users/{username}/following"
    __headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "Host": "api.gtihub.com",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.6"
    }

    def __getData(url, username):
        response = requests.get(url = url.format(username = username))
        if response.status_code != 200:
            raise Exception("Network Error", response)

        data = json.loads(response.text)
        return [user["login"] for user in data]

    def getFollowers(self, username):
        return apiRequest.__getData(apiRequest.__followersUrl, username)

    def getFollowing(self, username):
        return apiRequest.__getData(apiRequest.__followingUrl, username)

if __name__ == '__main__':
    obj1 = apiRequest()

    print(obj1.getFollowers("JAIDHEER007"))
