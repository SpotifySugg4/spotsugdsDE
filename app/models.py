import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.neighbors import KDTree
import joblib
import pickle
# spotify imports
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# spotify credentials
SPOTIPY_CLIENT_ID = '70a4ac0c19a0485290b200065069b58e'
SPOTIPY_CLIENT_SECRET = 'a9344253f7fa4902bf568a7e5d44f519'
# spotify login
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id = SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))

# read files
songID = pd.read_csv('../spotsugdsDE/songID.csv', index_col=0)
songScaler = joblib.load('../spotsugdsDE/scaler.gz')
# load pickled model
spotifyModel = pickle.load(open('../spotsugdsDE/spotifyModel.pkl', 'rb'))

def askTheModel(tempSongID='1Cj2vqUwlJVG27gJrun92y'):
  # some variables I need set up
  features = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
              'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
              'time_signature']
  temp = pd.DataFrame
  similarSongList = []
  # download the song data from spotify and scale it
  x = temp.from_dict(spotify.audio_features(tempSongID))[features]
  x_scaled = songScaler.transform(x)
  inputSongScaled = pd.DataFrame(x_scaled)
  # ask the model
  suggestedSongs = spotifyModel.query(np.array(inputSongScaled).reshape(1, -1), k=11)
  #  convert the answers to song IDs
  for song in suggestedSongs[1][0]:
    if (songID['id'][song]) != tempSongID:
      similarSongList = similarSongList + [(songID['id'][song])]
  return(similarSongList[:10])