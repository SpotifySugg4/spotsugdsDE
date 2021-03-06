import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.neighbors import NearestNeighbors
import joblib
import pickle
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from os import getenv
from dotenv import load_dotenv
load_dotenv()

# spotify credentials
SPOTIPY_CLIENT_ID = getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = getenv('SPOTIPY_CLIENT_SECRET')
# spotify login
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))

# read files
songID = pd.read_csv('./songID.csv', index_col=0)
songScaler = joblib.load('./scaler.gz')
# load pickled model
spotifyModel = pickle.load(open('./spotifyModel.pkl', 'rb'))
#print(songID)

def askTheModel(tempSongID='1Cj2vqUwlJVG27gJrun92y'):
  # some variables I need set up
  features = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
            'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
            'time_signature']
  temp = pd.DataFrame
  #tempSongID = '6meIeOX3DHdaCnaNw67abE'
  similarSongList = []
  x = temp.from_dict(spotify.audio_features(tempSongID))[features]
  inputSongScaled = songScaler.transform(x)
  #suggestedSongs = spotifyModel.kneighbors(np.array(inputSongScaled).reshape(1, -1), n_neighbors=21)
  suggestedSongs = spotifyModel.kneighbors(np.array(inputSongScaled).reshape(1, -1), n_neighbors=21, return_distance=False) #added , return_distance=False
  #  return song IDs
  
  #  convert the answers to song IDs
  #for song in suggestedSongs[1][0]:
  for song in suggestedSongs[0]:
    if (songID['id'][song]) != tempSongID:
      similarSongList = similarSongList + [(songID['id'][song])]
  return(similarSongList[:20])