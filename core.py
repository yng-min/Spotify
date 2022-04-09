# -*- coding: utf-8 -*-

import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

try:
    with open(r'./config.json', 'rt', encoding='UTF8') as configJson:
        config = json.load(configJson)
except:
    print('config.json is not loaded.')

client_credentials_manager = SpotifyClientCredentials(
    client_id = config['clientID'],
    client_secret = config['secretClientID']
)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
artist_search = str(input('Enter artist name: '))
print('=' * 25)

try:
    searchResult = sp.search(artist_search, type='artist')

    # artistReslut = searchResult['artists']['items'][0]
    # print(artistReslut)

    artistLINK = searchResult['artists']['items'][0]['external_urls']['spotify']
    print('Spotify URL: ' + artistLINK)

    artistNAME = searchResult['artists']['items'][0]['name']
    print('Artist Name: ' + artistNAME)

    artistID = searchResult['artists']['items'][0]['id']
    print('Artist ID: ' + artistID)

    artistIMAGE = searchResult['artists']['items'][0]['images'][0]['url']
    print('Artist Profile: ' + artistIMAGE)

    artistGENRES = searchResult['artists']['items'][0]['genres']
    genreMSG = ', '.join(genre for genre in artistGENRES[:5])
    print('Artist Genres: ' + genreMSG)

    artistFOLLOWERS = searchResult['artists']['items'][0]['followers']['total']
    print('Artist Followers: ' + str(artistFOLLOWERS))

    print('Artist Top Tracks: ↓')
    trackResult = sp.artist_top_tracks(artistID)
    i = 0
    for track in trackResult['tracks'][:10]:
        i += 1
        print(f'{i}/10')
        print('Track Name: ' + track['name'])
        print('Track URL: ' + track['album']['images'][0]['url'])

except:
    print('Artist is not found.')

input('\nPress Enter to exit...')
