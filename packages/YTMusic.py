from ytmusicapi import YTMusic
from difflib import SequenceMatcher

class yt():
    def __init__(self) -> None:
        self.yt = YTMusic('packages/oauth.json')
        self.missing = []
        self.currentID = 0
        self.ids = []
        self.added = []

    def createPlaylist(self, name):
        self.currentID = self.yt.create_playlist(name, description='')
        print('Playlist created!')

    def setPlaylistID(self, id):
        self.currentID = id

    def addSongs(self):
        # print(self.ids)
        self.yt.add_playlist_items(self.currentID, self.ids, duplicates=True)  

    def findSingle(self, item, threshold = 2.5):
        result = self.yt.search(rf'{item[0]}', filter='songs')
        ratio = 0
        for v in result:
            comparison_0 = rf'{item[0]} {item[1]}'
            check = rf"{v['title']} {v['artists'][0]['name']} {v['duration_seconds']}"
            
            comparison_time = item[1]
            check_time = float(v['duration_seconds'])

            ratio_time = check_time/comparison_time
            if ratio_time > 1: ratio_time = ratio_time**-1

            new_ratio = SequenceMatcher(None, comparison_0, check).ratio()
            if 2*new_ratio+ratio_time > ratio:
                ratio = 2*new_ratio+ratio_time
                cand = v

        if ratio > threshold:
            return (cand['videoId'], f"{cand['title']} {cand['artists'][0]['name']} {cand['duration_seconds']}")
        else: return ('NF', f"NF {cand['title']} {cand['artists'][0]['name']}")

    def addID(self, id):
        self.ids.append(id)       

    def addMissing(self, id):
        self.missing.append(id)

    def getMissing(self):
        print(self.missing)

if __name__ == '__main__':
    run = yt()
    #run.createPlaylist('Test123')
    print(run.findSingle(('Halt dein Maul Y-Titty', 218)))
    print(1)
