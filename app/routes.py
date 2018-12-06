import json
from flask import render_template, request, jsonify
from app.api_calls import openstreetmap_calls, wikimedia_calls
from app import app


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/about')
@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/search', methods=['POST'])
def search():
    user_request = request.form.get('search')
    coordinates = openstreetmap_calls.search_lat_lon(user_request)
    response = {"lat": coordinates[0],
                "lon": coordinates[1],
                "mapbox_token": app.config['MAPBOX_TOKEN']
                }
    return jsonify(response)
