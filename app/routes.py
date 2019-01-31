from flask import render_template, request, jsonify
from app.research import Research
from app import app


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/user_message', methods=['POST'])
def user_msg():
    user_input = request.form.get('user_input')
    return render_template('user_message.html', message=user_input)


@app.route('/grandpy_message', methods=['POST'])
def grandpy_message():
    user_request = request.form.get('user_input')
    research = Research(user_request)
