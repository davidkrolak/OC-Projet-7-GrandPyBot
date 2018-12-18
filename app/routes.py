from flask import render_template, request, jsonify
from app.api_calls import openstreetmap, wikimedia
from app.search import search_script
from app import app


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/search', methods=['POST'])
def search():
    user_request = request.form.get('search')
    return jsonify(search_script(user_request))


@app.route("/init_token", methods=["POST"])
def init_token():
    return jsonify({"token": app.config['GOOGLE_CLOUD_TOKEN']})
