import requests
from .config import TOKEN, SERVER_URL

class OVK:
    def __init__(self):
        self.token = TOKEN
        self.server = SERVER_URL
    
    def aboutInstance(self): 
        response = requests.get(f"{self.server}/method/ovk.aboutInstance")
        return response.json()
    
    def chickenWings(self):
        response = requests.get(f"{self.server}/method/ovk.chickenWings")
        return response.json()
    
    def version(self):
        response = requests.get(f"{self.server}/method/ovk.version")
        return response.json()
    

