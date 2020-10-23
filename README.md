# spotsugdsDE
Spotify Song Suggester Data Science Data Engineer

## Setup

Instructions for virtual environment and packages install:
(It is recommended to use a pip enviornment to run a flask app.)

```sh
create a pip enviornment with pipfile and pipfile lock (this will hold your dependencies)

Install packages: pip install spotipy, gunicorn, flask-cors, pandas, sklearn, getenv, and python-dotenv

Activate pip environment: activate pipenv
```

Instructions to setup flask app:

```sh
<b>Creation of the app.py, __init__.py for the routes and initiations.<b>
sugg/app.py
App.py file:
This file holds all the routes that will be used in the app. It holds the main, song suggestions, and song search routes.
  
sugg/__init__/py
 __init__.py file:
 This file holds the imports and the app creation
 
from flask import Flask
from sugg.app import create_app
from sugg.models import models

APP = create_app()
```

## Usage
```sh
Deploy Flask App Itself: FLASK_APP_sugg.py
Run Flask App: flask run
```
## Usage for Spotify API
```sh
sugg/models.py
Import packages spotipy and SpotifyClientCredentials:
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
```
```
# spotify credentials
SPOTIPY_CLIENT_ID = getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = getenv('SPOTIPY_CLIENT_SECRET')
# spotify login
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))
```
## Data pull from Spotify
```sh
import pandas as pd
import numpy as np

Creation of dataset list that would be pulled from Spotify's API:
Spotify Dataset 1921-2020, 160k+ Tracks (sent through Spotify API for list of songid's)
```

## Pickle Model for predictions
```sh
from sklearn import preprocessing
from sklearn.neighbors import Nearest Neighbors
import joblib
import pickle
from os import getenv
from dotenv import load_dotenv
load_dotenv()

Creation of a scaler to read the files:
songID = pd.read_csv('./songID.csv', index_col=0)
songScaler = joblib.load('./scaler.gz')

The pickled model:
spotifyModel = pickle.load(open('./spotifyModel.pkl', 'rb'))

Class for the model:
def askTheModel(tempSongID='1Cj2vqUwlJVG27gJrun92y'):
  # some variables I need set up
  features = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
            'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
            'time_signature']
              
 Download songs data from Spotify and scale it:
temp = pd.DataFrame
  tempSongID = '6meIeOX3DHdaCnaNw67abE'
  similarSongList = []
  x = temp.from_dict(spotify.audio_features(tempSongID))[features]
  inputSongScaled = songScaler.transform(x)
  
Ask the model:
#suggestedSongs = spotifyModel.kneighbors(np.array(inputSongScaled).reshape(1, -1), n_neighbors=21)
  suggestedSongs = spotifyModel.kneighbors(np.array(inputSongScaled).reshape(1, -1), n_neighbors=21, return_distance=False) #added , return_distance=False
  #  return song IDs
 
Convert the answers to song ids:
for song in suggestedSongs[1][0]:
    if (songID['id'][song]) != tempSongID:
      similarSongList = similarSongList + [(songID['id'][song])]
  return(similarSongList[:21])
  ```
  
  ## Push app to Heroku and/or Postman
  ```sh
  Link to live app in Heroku:
  https://spotifindya.herokuapp.com/ 
```



