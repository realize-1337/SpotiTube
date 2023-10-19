from ytmusicapi import YTMusic, setup_oauth
from difflib import SequenceMatcher
import pandas as pd

class yt():
    def __init__(self, path) -> None:
        self.yt = YTMusic(path)
        self.missing = []
        self.currentID = 0
        self.ids = []
        self.added = []

    def createPlaylist(self, name):
        self.currentID = self.yt.create_playlist(name, description='')
        id = self.currentID
        print('Playlist created!')
        return id

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

    def findTables(self, title:str, artist:str, duration:int, count:int=20, filter:str='songs'):
        ids = []
        titles = []
        artists = []
        matchRatios = []
        query = rf"{title} {artist}"
        result = self.yt.search(f"{query}", filter=f"{filter}")
        for v in result:
            if v['title'] and v['artists'][0]['name'] and v['duration']:
                if rf"{v['videoId']}" not in ids:
                    ids.append(rf"{v['videoId']}")
                else: continue
                titles.append(rf"{v['title']}")
                artists.append(rf"{v['artists'][0]['name']}")


                comparison_0 = rf"{title} {artist} {duration}".lower()
                check = rf"{v['title']} {v['artists'][0]['name']} {v['duration_seconds']}".lower()
                check_time = float(v['duration_seconds'])
                ratio_time = check_time/float(duration)
                if ratio_time > 1: ratio_time = ratio_time**-1

                new_ratio = SequenceMatcher(None, comparison_0, check).ratio()
                matchRatios.append((2*new_ratio+ratio_time)/3)       
            
        ids.append('NULL')
        ids.insert(0, 'target')
        titles.append('NULL')
        titles.insert(0, rf"{title}")
        artists.append('NULL')
        artists.insert(0, rf"{artist}")
        matchRatios.append(0)
        matchRatios.insert(0, 2)
        data = {
            'title': titles,
            'artist': artists,
            'matchRatio': matchRatios
        }
        df = pd.DataFrame(index=ids, data=data)
        df = df.sort_values('matchRatio', ascending=False)
        df = df.transpose()
        df = df.to_dict()
        return df

if __name__ == '__main__':
    run = yt('packages/oauth.json')
    #run.createPlaylist('Test123')
    #print(run.findSingle(('Halt dein Maul Y-Titty', 218)))
    # run.findTables('Halt dein Maul', 'Y-Titty', '212')
    run.createPlaylist('Test')
    print(1)
