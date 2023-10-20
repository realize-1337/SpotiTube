# *SpotiTube* - Spotify to YouTube Music Playlist Converter: 

**Disclaimer:** This project was inspired by [sigma67's spotify to ytmusic tool](https://github.com/sigma67/spotify_to_ytmusic). 
However, I did not quite like their approach and wanted to create my own tool. I actually didn't really took a deeper look into their code, thus their might be some similarities between our creations. 

## Contents

 1. [Setup](#setup)<br>
	 1.1. [Compiled Build](#compiled-build) 
	 1.2. [Compile yourself](#compile-it-on-your-own)
	 1.3. [Without compiling](#run-without-compiling)
2. [Usage](#usage)
3. [Known issues](#known-issues)

## Setup

There are basically three ways to use this tool:

 ### Compiled Build
 The easiest way is to download the current build from the releases and just run it.

### Compile it on your own
Alternatively, you can clone the repository, install the requirements `pip install -r .\requirements.txt` and then run `python setup_gui.py`.

### Run without compiling
Last but not least, you can clone the repository, install the requirements `pip install -r .\requirements.txt` and then run `python .\main.py`.

## Usage
### First start
Upon the first start, the settings dialog opens. 
It is separated into two parts:

#### Spotify
Here you need to enter your Spotify client id and client secret. You have to create a Spotify developer account at first. This can be done [here](https://developer.spotify.com/). Head over to the [dashboad](https://developer.spotify.com/dashboard) and create an app. In the app settings you are able to retrieve your client id and your client secret. Just copy paste them to the software.

#### YouTube Music
 Just click on the Login button and you are redirected to a Google login page. There you will find a code. Make sure it is the same as shown in the program (usually it is, but better save than sorry). After your login is completed, just hit the Login button again and everything is completed. 
 Press 'Ok' to complete the setup process.

#### Where is my data stored
Everything is stored locally at `$User/Documents/SpotiTube/`. Alternatively, you can run the program with `python .\main.py C:\Path\to\a\different\folder` or just append a path in the execution line on the .exe properties. Then your files are stored at this place.

### Move your first playlist
All you need is a link to your Spotify playlist. This can either be a open.spotify.com/playlist/ or you can can use the playlist id. 
Just paste the link into the line input in the Spotify tab and press 'Search Playlist'. The search usually takes only a few fractions of a seconds, for larger playlists it can take up to 5 seconds. 
Afterwards you are presented with all playlist items in the table. 

Now you can head over to the YouTube Music tab. This initializes the search for the YouTube Music items. Depending on the playlist size and your thread count this might take a few seconds. From my findings, the API can deal with around 20 requests per second.

The YouTube Music tab finally looks like this.

![enter image description here](https://imgur.com/5vrGhdv.png)

Here you can change the playlist name if you want. This name will be set for the Playlist in YouTube Music. 
In the table you will see the title and the artist(s) of the songs taken from the Spotify playlist. Next to it you can find the 'Match Ratio' in range 0 to 1, the higher the better is result. An exclamation mark (!) in front of the Match ratio indicates that the artists are highly different, thus you might need to change the YouTube item in the last column. 

The YouTube item has a dropdown list of 21 items for each song. This are the top-20 results for the title-artist-combination. The highest Match Ratio is chosen by default, however, you can change it to one of the other results just by changing it in the dropdown menu. If you set the dropdown to 'NULL' this song is not moved to the Playlist, because sometimes songs are not available. 

If you are ready to move the playlist, just hit 'Commit to YT Music'. If successful, the playlist will automatically open. 

#### Match Ratio explained
The Match Ratio is calculated from the similarities between the Spotify and YouTube Items. For each Spotify song, up to 20 YouTube Songs are searched. Each song is compared by title, artist and duration. The closer the songs are together, the higher is the similarity. Usually, a Match Ratio >= 0.8 indicates a good result. 
66 % of the Match Ratio are due to title + artist similarities, while the remaining 33 % are from the duration similarities. 

## Known Issues
At the moment only public playlists can be copied. I am planning to add private playlists later on. You can work around it by simply putting the playlist public for a spit second, start the import of the playlist data, wait for it to finish and then set it to private again. The link stays the same the whole time. 
