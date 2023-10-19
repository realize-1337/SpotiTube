import spotipy
import time
from spotipy.oauth2 import SpotifyClientCredentials
import json

class sp():
    def __init__(self, path) -> None:
        with open(path, 'r') as f:
            keys = json.load(f)
        self.auth_manager = SpotifyClientCredentials(client_id=keys['client_id'], client_secret=keys['client_secret'])
        self.sp = spotipy.Spotify(auth_manager=self.auth_manager)
        self.tracks = {}
        self.taken = []
        

    def getPlaylist(self, id):
        i = 0
        for j in range(0, 10000, 100):
            items = self.sp.playlist_items(id,market='DE', fields='(items(track(name, artists(name), album(name), duration_ms)))', limit=100, offset=j)
            if len(items['items']) == 0 and j >= 100: break
            for key, value in items.items():
                print(len(value))
                for item in value:
                    artists = ''
                    for artist in item['track']['artists']:
                        artists += f'{artist["name"]} '
                    self.tracks[i] = {
                        'name': item['track']['name'],
                        # 'artists': item['track']['artists'][0]['name'],
                        'artists': artists,
                        'album': item['track']['album']['name'],
                        'duration': round(float(item['track']['duration_ms'])/1000)
                    }
                    i += 1
        return self.sp.playlist(id)['name']
    
    def createQuery(self):
        query = []
        for k, v in self.tracks.items():
            #query.append(f"{v['name']} {v['artists']} {v['album']}")
            query.append((f"{v['name']} {v['artists']}", v['duration']))
            self.taken.append(f"{v['name']} {v['artists']} {v['duration']}")
        return query
    
    def songDict(self) -> dict: 
        dict = {}
        for key, value in self.tracks.items():
            dict[f"{key}"] = {
                'title': f"{value['name']}",
                'artist': f"{value['artists']}",
                'album': f"{value['album']}",
                'duration': f"{value['duration']}"
            }
        self.tracks.clear()
        return dict


if __name__ == "__main__":
    sp = sp('packages/keys.json')
    tracks = sp.getPlaylist('04xpedGXCtq4W9zdkCEvZq')  
    dict = sp.songDict()
    print(sp.createQuery())


