import requests
import string

forbidden_characters = string.punctuation


def search_page_by_id(research):
    session = requests.Session()

    url = "https://fr.wikipedia.org/w/api.php"

    srsearch = []
    for character in research:
        if character in forbidden_characters:
            pass
        elif character == ' ':
            srsearch.append('%20')
        else:
            srsearch.append(character)
    srsearch = ''.join(srsearch)

    params = {
        'action': 'query',
        'list': 'search',
        'format': 'json',
        'utf8': '',
        'srsearch': srsearch
    }

    result = session.get(url=url, params=params)
    data = result.json()

    page_id = data['query']['search'][0]['pageid']

    return page_id
