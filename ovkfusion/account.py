import requests
from . import config

class Account:
    def __init__(self):
        self.token = config.TOKEN
        self.server = config.SERVER_URL

    def getProfileInfo(self):
        response = requests.get(f"{self.server}/method/account.getProfileInfo", params={"access_token": self.token})
        return response.json()

    def getInfo(self):
        response = requests.get(f"{self.server}/method/account.getInfo", params={"access_token": self.token})
        print(self.token)
        return response.json()
    
    def setOnline(self):
        response = requests.get(f"{self.server}/method/account.setOnline", params={"access_token": self.token})
        return response.json()
    
    def getCounters(self):
        response = requests.get(f"{self.server}/method/account.getCounters", params={"access_token": self.token})
        return response.json()
    
    def saveProfileInfo(self, first_name, last_name, screen_name, sex, relation, bdate, bdate_visibility, home_town, status):
        response = requests.get(f"{self.server}/method/account.saveProfileInfo", params={
            "access_token": self.token,
            "first_name": first_name,
            "last_name": last_name,
            "screen_name": screen_name,
            "sex": sex,
            "relation": relation,
            "bdate": bdate,
            "bdate_visibility": bdate_visibility,
            "home_town": home_town,
            "status": status
        })
        return response.json()

    def getBalance(self):
        response = requests.get(f"{self.server}/method/account.getBalance", params={"access_token": self.token})
        return response.json()
    
    def getOvkSettings(self):
        response = requests.get(f"{self.server}/method/account.getOvkSettings", params={"access_token": self.token})
        return response.json()['response']
    
    def sendVotes(self, reciever, value, message=""):
        response = requests.get(f"{self.server}/method/account.sendVotes", params={
            "access_token": self.token,
            "reciever": reciever,
            "value": value,
            "message": message
        })
        return response.json()['response']

    def ban(self, owner_id):
        response = requests.get(f"{self.server}/method/account.ban", params={
            "access_token": self.token,
            "owner_id": owner_id
        })
        return response.json()['response']

    def unban(self, owner_id):
        response = requests.get(f"{self.server}/method/account.unban", params={
            "access_token": self.token,
            "owner_id": owner_id
        })
        return response.json()['response']