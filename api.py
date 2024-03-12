import requests


class API:
    def __init__(self, APIKey):
        self.baseurl = "https://api.kakaowork.com/v1"
        self.headers = {"Content-Type": "application/json"}
        self.headers["Authorization"] = "Bearer " + APIKey
        self.users = self.getUsers()["users"]

    def getUsers(self):
        url = self.baseurl + "/users.list"
        res = requests.get(url, headers=self.headers)
        return res.json()

    def getConversation(self, user_id):
        url = self.baseurl + "/conversations.open"
        data = {"user_id": user_id}
        res = requests.post(url, headers=self.headers, json=data)
        return res.json()

    def sendMessageAll(self, content, send):
        url = self.baseurl + "/messages.send"
        userList = []

        if send == "student":
            for user in self.users:
                if user["department"] != "Teacher":
                    userList.append(user["id"])

        if send == "teacher":
            for user in self.users:
                if user["department"] == "Teacher":
                    userList.append(user["id"])

        for user in userList:
            data = {
                "conversation_id": self.getConversation(user)["conversation"]["id"],
                "text": content,
            }
            requests.post(url, headers=self.headers, json=data)

        return {"success": True}


if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    load_dotenv()

    api = API(os.getenv("KAKAOBOT_API_KEY"))
    print(api.sendMessageAll("Hello, World!", True, False))
