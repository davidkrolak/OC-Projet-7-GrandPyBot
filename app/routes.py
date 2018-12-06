from flask import render_template, request, jsonify
from app.api_calls import openstreetmap_calls, wikimedia_calls
from app.search import search_script
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
    return jsonify(search_script(user_request))
