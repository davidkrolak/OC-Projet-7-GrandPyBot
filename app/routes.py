from flask import render_template, request, jsonify
from app.research import search_script
from app import app


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/search', methods=['POST'])
def search():
    user_request = request.form.get('search')
    return jsonify(search_script(user_request))


@app.route('/user_message', methods=['POST'])
def user_msg():
    user_input = request.form.get('user_input')
    user = {"message": user_input}
    return render_template('user_message.html', user=user)
