from ytmusicapi import YTMusic
import multiprocessing as mp
from tqdm import tqdm

class yt():
    def __init__(self) -> None:
        self.yt = YTMusic('packages/oauth.json')
        self.missing = []
        self.currentID = 0
        self.ids = []

    def findSingles(self, query):
        for item in tqdm(query):
            result = self.yt.search(item, filter='songs')
            if result: 
                #print(result[0]['videoId'])
                self.ids.append(result[0]['videoId'])
            else: 
                self.missing.append(item)
                False

    def createPlaylist(self, name):
        self.currentID = self.yt.create_playlist(name, description='')
        print('Playlist created!')

    def setPlaylistID(self, id):
        self.currentID = id

    def addSongs(self):
        self.yt.add_playlist_items(self.currentID, self.ids)     

    def getMissing(self):
        return self.missing
    

if __name__ == '__main__':
    run = yt()
    run.createPlaylist('Test123')
    run.getYT('Peter Fox Haus am See Stadtaffe')
