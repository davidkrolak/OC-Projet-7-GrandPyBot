import requests
import string

forbidden_characters = string.punctuation


def search_page_by_id(research):
    session = requests.Session()

    url = "https://fr.wikipedia.org/w/api.php"

    params = {
        'action': 'query',
        'list': 'search',
        'format': 'json',
        'utf8': '',
        'srsearch': research
    }

    result = session.get(url=url, params=params)
    data = result.json()

    try:
        if data['error']['code'] == 'nosrsearch':
            return 0
    except KeyError:
        pass

        if data['query']['searchinfo']['totalhits'] == 0:
            return -1

        elif data['query']['searchinfo']['totalhits'] >= 1:
            page_id = data['query']['search'][0]['pageid']
            return page_id