import requests
from . import config  # Import the config module

class Auth:
    def __init__(self, username: str, password: str, server: str = "https://ovk.to"):
        self.username = username
        self.password = password
        self.server = server
        self.token = None

    def get_token(self) -> str:
        response = requests.get(
            f"{self.server}/token",
            params={"username": self.username, "password": self.password, "grant_type": "password"}
        )
    
        if response.status_code == 200:
            self.token = response.json()
            config.TOKEN = self.token['access_token']  # Update TOKEN globally
            return self.token['access_token']  # Return the token for further use
        else:
            raise ConnectionError(f"Failed to get token: {response.json()}")