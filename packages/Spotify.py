import spotipy
import time
from spotipy.oauth2 import SpotifyClientCredentials
import json

class sp():
    def __init__(self) -> None:
        with open('packages/keys.json', 'r') as f:
            keys = json.load(f)
        self.auth_manager = SpotifyClientCredentials(client_id=keys['client_id'], client_secret=keys['client_secret'])
        self.sp = spotipy.Spotify(auth_manager=self.auth_manager)
        self.tracks = {}
        

    def getPlaylist(self, id):
        i = 0
        for j in range(0, 10000, 100):
            items = self.sp.playlist_items(id,market='DE', fields='(items(track(name, artists(name), album(name))))', limit=100, offset=j)
            if len(items['items']) == 0 and j >= 100: break
            for key, value in items.items():
                print(len(value))
                for item in value:
                    self.tracks[i] = {
                        'name': item['track']['name'],
                        'artists': item['track']['artists'][0]['name'],
                        'album': item['track']['album']['name']
                    }
                    i += 1
        return self.sp.playlist(id)['name']
    
    def createQuery(self):
        query = []
        for k, v in self.tracks.items():
            query.append(f"{v['name']} {v['artists']} {v['album']}")
        return query
    

if __name__ == "__main__":
    sp = sp()
    tracks = sp.getPlaylist('04xpedGXCtq4W9zdkCEvZq')  
    print(sp.createQuery())


