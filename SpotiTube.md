---


---

<h1 id="spotitube---spotify-to-youtube-music-playlist-converter"><em>SpotiTube</em> - Spotify to YouTube Music Playlist Converter:</h1>
<p><strong>Disclaimer:</strong> This project was inspired by <a href="https://github.com/sigma67/spotify_to_ytmusic">sigma67’s spotify to ytmusic tool</a>.<br>
However, I did not quite like their approach and wanted to create my own tool. I actually didn’t really took a deeper look into their code, thus their might be some similarities between our creations.</p>
<h2 id="contents">Contents</h2>
<ol>
<li><a href="##Setup">Setup</a><br>
1.1. <a href="###%20Compiled%20Build">Compiled Build</a><br>
1.2. <a href="###%20Compile%20it%20on%20your%20own">Compile yourself</a><br>
1.3. <a href="###%20Run%20without%20compiling">Without compiling</a></li>
<li><a href="##Usage">Usage</a></li>
<li><a href="##Know%20Issues">Known issues</a></li>
</ol>
<h2 id="setup">Setup</h2>
<p>There are basically three ways to use this tool:</p>
<h3 id="compiled-build">Compiled Build</h3>
<p>The easiest way is to download the current build from the releases and just run it.</p>
<h3 id="compile-it-on-your-own">Compile it on your own</h3>
<p>Alternatively, you can clone the repository, install the requirements <code>pip install -r .\requirements.txt</code> and then run <code>python setup_gui.py</code>.</p>
<h3 id="run-without-compiling">Run without compiling</h3>
<p>Last but not least, you can clone the repository, install the requirements <code>pip install -r .\requirements.txt</code> and then run <code>python .\main.py</code>.</p>
<h2 id="usage">Usage</h2>
<h3 id="first-start">First start</h3>
<p>Upon the first start, the settings dialog opens.<br>
It is separated into two parts:</p>
<h4 id="spotify">Spotify</h4>
<p>Here you need to enter your Spotify client id and client secret. You have to create a Spotify developer account at first. This can be done <a href="https://developer.spotify.com/">here</a>. Head over to the <a href="https://developer.spotify.com/dashboard">dashboad</a> and create an app. In the app settings you are able to retrieve your client id and your client secret. Just copy paste them to the software.</p>
<h4 id="youtube-music">YouTube Music</h4>
<p>Just click on the Login button and you are redirected to a Google login page. There you will find a code. Make sure it is the same as shown in the program (usually it is, but better save than sorry). After your login is completed, just hit the Login button again and everything is completed.<br>
Press ‘Ok’ to complete the setup process.</p>
<h4 id="where-is-my-data-stored">Where is my data stored</h4>
<p>Everything is stored locally at <code>$User/Documents/SpotiTube/</code>. Alternatively, you can run the program with <code>python .\main.py C:\Path\to\a\different\folder</code> or just append a path in the execution line on the .exe properties. Then your files are stored at this place.</p>
<h3 id="move-your-first-playlist">Move your first playlist</h3>
<p>All you need is a link to your Spotify playlist. This can either be a <a href="http://open.spotify.com/playlist/">open.spotify.com/playlist/</a> or you can can use the playlist id.<br>
Just paste the link into the line input in the Spotify tab and press ‘Search Playlist’. The search usually takes only a few fractions of a seconds, for larger playlists it can take up to 5 seconds.<br>
Afterwards you are presented with all playlist items in the table.</p>
<p>Now you can head over to the YouTube Music tab. This initializes the search for the YouTube Music items. Depending on the playlist size and your thread count this might take a few seconds. From my findings, the API can deal with around 20 requests per second.</p>
<p>The YouTube Music tab finally looks like this.</p>
<p><img src="https://imgur.com/5vrGhdv.png" alt="enter image description here"></p>
<p>Here you can change the playlist name if you want. This name will be set for the Playlist in YouTube Music.<br>
In the table you will see the title and the artist(s) of the songs taken from the Spotify playlist. Next to it you can find the ‘Match Ratio’ in range 0 to 1, the higher the better is result. An exclamation mark (!) in front of the Match ratio indicates that the artists are highly different, thus you might need to change the YouTube item in the last column.</p>
<p>The YouTube item has a dropdown list of 21 items for each song. This are the top-20 results for the title-artist-combination. The highest Match Ratio is chosen by default, however, you can change it to one of the other results just by changing it in the dropdown menu. If you set the dropdown to ‘NULL’ this song is not moved to the Playlist, because sometimes songs are not available.</p>
<p>If you are ready to move the playlist, just hit ‘Commit to YT Music’. If successful, the playlist will automatically open.</p>
<h4 id="match-ratio-explained">Match Ratio explained</h4>
<p>The Match Ratio is calculated from the similarities between the Spotify and YouTube Items. For each Spotify song, up to 20 YouTube Songs are searched. Each song is compared by title, artist and duration. The closer the songs are together, the higher is the similarity. Usually, a Match Ratio &gt;= 0.8 indicates a good result.<br>
66 % of the Match Ratio are due to title + artist similarities, while the remaining 33 % are from the duration similarities.</p>
<h2 id="known-issues">Known Issues</h2>
<p>At the moment only public playlists can be copied. I am planning to add private playlists later on. You can work around it by simply putting the playlist public for a spit second, start the import of the playlist data, wait for it to finish and then set it to private again. The link stays the same the whole time.</p>

