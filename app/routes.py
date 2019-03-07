from flask import render_template, request, jsonify
from flask_wtf.csrf import CSRFProtect
from app import research
from app import app

csrf = CSRFProtect(app)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/user_message', methods=['POST'])
def user_msg():
    user_input = request.form.get('user_input')
    print("User input: " + user_input)  # Logs users input to Stdout
    return render_template('user_message.html', message=user_input)


@app.route('/grandpy_message', methods=['POST'])
def grandpy_message():
    user_request = request.form.get('user_input')

    r = research.Research(user_request)
    r.main()
    response = {
        'lat': r.lat,
        'lng': r.lng,
        'status': r.status,
        'msg_1': render_template(
                'grandpy_message_1.html',
                grandpy_response=r.grandpy_response)
    }

    if r.status == 'wikimedia_page_url_ok':
        response['msg_2'] = render_template('grandpy_message_2.html',
                                            address=r.formatted_address)
        response['msg_3'] = render_template('grandpy_message_3.html',
                                            wiki_summary=r.wiki_summary,
                                            wiki_link=r.wiki_url)
    elif r.status in research.no_info_status:
        response['msg_2'] = render_template('grandpy_message_2.html',
                                            address=r.formatted_address)
    print("Response status: " + r.status)  # Logs response status to stdout
    return jsonify(response)
