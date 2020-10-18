from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
from models import askTheModel


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
        return jsonify(results)
        
    return app