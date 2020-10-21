from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
from sugg.models import askTheModel, spotify


def create_app():
    '''Create and configure an instance of the Flask application'''
    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def main():
        return 'Welcome to our Spotify Song Suggester!'
    
    @app.route('/suggestions', methods=['POST'])
    # Takes json requests from web.
    def suggestions():
        song_id = request.json['song_id']
        results = askTheModel(song_id)
        results = (spotify.tracks(results)) #Remove this line to only return song_IDs
        return jsonify(results)

    @app.route('/search', methods=['POST'])
    # Takes json requests from web.
    def search():
        name = request.json['name']
        results2 = spotify.search(q='track:' + name, type='track', limit=20)
        return jsonify(results2)
        
    return app