import requests
from . import config

class Audio:
    def __init__(self):
        self.token = config.TOKEN
        self.server = config.SERVER_URL

    def getById(self, audios, hash=None, need_user=False):
        response = requests.get(f"{self.server}/method/audio.getById", params={
            "access_token": self.token,
            "audios": audios,
            "hash": hash,
            "need_user": str(need_user).lower()
        })

        return response.json()['response']
    
    def isLagtrain(self, audio_id):
        response = requests.get(f"{self.server}/method/audio.isLagtrain", params={
            'audio_id': audio_id
        })

        return response.json()['response']
    
    
    def getPopular(self, genre_id=None, genre_str=None, offset=0, count=10, hash=None):
        response = requests.get(f"{self.server}/method/audio.getPopular", params={
            "access_token": self.token,
            "genre_id": genre_id,
            "genre_str": genre_str,
            "offset": offset,
            "count": count,
            "hash": hash
        })

        return response.json()['response']
    
    def search(self, q, lyrics=False, performer_only=False, sort=0, offset=0, count=10, hash=None):
        response = requests.get(f"{self.server}/method/audio.search", params={
            "access_token": self.token,
            "q": q,
            "lyrics": int(lyrics),
            "performer_only": int(performer_only),
            "sort": sort,
            "offset": offset,
            "count": count,
            "hash": hash
        })

        return response.json()['response']
    
    def getCount(self, owner_id, uploaded_only=False):
        response = requests.get(f"{self.server}/method/audio.getCount", params={
            "access_token": self.token,
            "owner_id": owner_id,
            "uploaded_only": int(uploaded_only)
        })

        return response.json()['response']

    
    def get(self, owner_id=None, album_id=None, audio_ids=None, offset=0, count=10, uploaded_only=False):
        response = requests.get(f"{self.server}/method/audio.get", params={
            "access_token": self.token,
            "owner_id": owner_id,
            "album_id": album_id,
            "audio_ids": audio_ids,
            "offset": offset,
            "count": count,
            "uploaded_only": int(uploaded_only)
        })

        return response.json()['response']

