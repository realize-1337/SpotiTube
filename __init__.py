import packages.Spotify as sp
import packages.YTMusic as yt
import packages.comparison as cp
from tqdm import tqdm
import multiprocessing as mp


def worker(item):
    return yt.yt().findSingle(item, 2.3)

if __name__ == '__main__':
    yt = yt.yt()
    sp = sp.sp()

    name = sp.getPlaylist('4MDF70V4N3Dfj3DXWi6lML')
    search = sp.createQuery()
    

    pool = mp.Pool(mp.cpu_count())
    with tqdm(total=len(search)) as pbar:
        for result in pool.imap(worker, search):
            if not result[0].startswith('NF'):
                yt.addID(result[0])
                yt.added.append(result[1])
            else: 
                yt.addMissing(result[1].removeprefix('NF '))
                yt.added.append('NOTFOUND')
            pbar.update(1)
        

        pool.close()
        pool.join
    
    print('Finished searching')

    missing = yt.getMissing()
    print(missing)

    cp = cp.Comparison(yt.added, sp.taken, yt.missing)
    cp.ratio()
    cp.export('./export', f'{name}_export')
    
    yt.createPlaylist(name)
    yt.addSongs()
