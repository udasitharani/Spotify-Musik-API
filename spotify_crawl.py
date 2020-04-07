import spotipy, os
from spotipy.oauth2 import SpotifyClientCredentials

id = os.getenv('SPOTIPY_CLIENT_ID')
secret = os.getenv('SPOTIPY_CLIENT_SECRET')

HINDI = "hi_IN"
ENGLISH = "en_US"
COUNTRY="IN"

client_credentials_manager = SpotifyClientCredentials(client_id=id, client_secret=secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def featured_playlists(count, language):
    global HINDI, ENGLISH, COUNTRY
    playlists = {}
    if(language=="hi"):
        result = spotify.featured_playlists(locale=HINDI, limit=50, country=COUNTRY)
    elif(language=="en"):
        result = spotify.featured_playlists(locale=ENGLISH, limit=50, country=COUNTRY)
    else:
        return {"message":"invalid language"}
    playlists = read_playlists(result['playlists']['items'][:count])
    return playlists

def read_playlists(items):
    playlists = {}
    for index, item in enumerate(items):
        playlist = {}
        if(item['type']=='album'):
            tracks[str(index)] = read_albums([item])['0']
            continue
        elif(item['type']=='track'):
            tracks[str(index)] = get_songs([item])['0']
            continue
        elif(item['type']=='playlist'):
            playlist['type'] = item['type']
            playlist['name'] = item['name']
            playlist['thumbnails'] = item['images']
            playlist['uri'] = item['uri']
            playlist['id'] = item['id']
            playlist['external_urls'] = item['external_urls']
            playlist['tracks'] = get_playlist_songs(spotify.playlist_tracks(playlist_id=playlist['id'], limit=50)['items'])
            playlists[str(index)] = playlist
    return playlists

def get_playlist_songs(items):
    tracks = {}
    for index, ite in enumerate(items):
        track = {}
        item = ite['track']
        track['type'] = 'track'
        track['name'] = item['name']
        track['href'] = item['href']
        track['duration'] = item['duration_ms']
        track['uri'] = item['uri']
        track['id'] = item['id']
        track['artists'] = item['artists']
        tracks[str(index)] = track
    return tracks

def new_releases(count):
    global COUNTRY
    albums = {}
    result = spotify.new_releases(country=COUNTRY, limit=50)
    albums = read_albums(result['albums']['items'][:count])
    return albums

def read_albums(items):
    albums = {}
    for index, item in enumerate(items):
        if(item['type']=='track'):
            tracks[str(index)] = get_songs([item])['0']
            continue
        elif(item['type']=='playlist'):
            tracks[str(index)] = read_playlists([item])['0']
            continue
        elif(item['type']=='album'):
            album = {}
            album['type'] = "album"
            album['name'] = item['name']
            album['thumbnails'] = item['images']
            album['uri'] = item['uri']
            album['id'] = item['id']
            album['external_urls'] = item['external_urls']
            album['tracks'] = get_songs(spotify.album_tracks(album_id=album['id'], limit=50)['items'])
            album['track_count'] = item['total_tracks']
            albums[str(index)] = album
    return albums

def get_songs(items):
    tracks = {}
    for index, item in enumerate(items):
        track = {}
        track['type'] = 'track'
        track['name'] = item['name']
        track['href'] = item['href']
        track['duration'] = item['duration_ms']
        track['uri'] = item['uri']
        track['id'] = item['id']
        track['artists'] = item['artists']
        tracks[str(index)] = track
    return tracks

def get_artist(id):
    artist = spotify.artist(artist_id=id)
    return artist

def get_artist_songs(id):
    global COUNTRY
    top_tracks = {}
    result = get_songs(spotify.artist_top_tracks(id, country=COUNTRY)['tracks'])
    return result

def get_artist_albums(id, count):
    albums = {}
    if(count>50): count = 50
    result = read_albums(spotify.artist_albums(artist_id=id, limit=count)['items'])
    return result

def search_tracks(keyword, count):
    if(count>50): count = 50
    result = spotify.search(q="track:"+keyword, limit=count, type="track")
    tracks = read_tracks(result['tracks']['items'])
    return tracks

def read_tracks(items):
    tracks = {}
    for index, item in enumerate(items):
        if(item['type']=='album'):
            tracks[str(index)] = read_albums([item])['0']
            continue
        elif(item['type']=='track'):
            tracks[str(index)] = get_songs([item])['0']
            continue
        elif(item['type']=='playlist'):
            tracks[str(index)] = read_playlists([item])['0']
            continue
    return tracks

def search_albums(keyword, count):
    if(count>50): count = 50
    result = spotify.search(q="album:"+keyword, limit=count, type="album")
    albums = read_albums(result['albums']['items'])
    return albums
 
def search_playlists(keyword, count):
    if(count>50): count = 50
    result = spotify.search(q="playlist:"+keyword, limit=count, type="playlist")
    playlists = read_playlists(result['playlists']['items'])
    return playlists

def search_artists(keyword, count):
    if(count>50): count = 50
    artist = spotify.search(q="artist:"+keyword, limit=count, type="artist")
    return artist
