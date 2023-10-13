import packages.Spotify as sp
import packages.YTMusic as yt


def do(item):
    yt.yt().getYT(item)

if __name__ == '__main__':
    yt = yt.yt()
    sp = sp.sp()

    name = sp.getPlaylist('7xTGsbLdM0p5RIKkM9QKHi')
    search = sp.createQuery()
    yt.createPlaylist(name)
    # yt.setPlaylistID()
    yt.findSingles(search)
    print('Finished searching')
    
    yt.addSongs()


    missing = yt.getMissing()
    print(missing)