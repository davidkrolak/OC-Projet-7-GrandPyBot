import requests


def search_page_id_query(research):
    """"""
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

    if "error" in data.keys():
        return 0

    if data['query']['searchinfo']['totalhits'] == 0:
        return -1

    elif data['query']['searchinfo']['totalhits'] >= 1:
        page_id = data['query']['search'][0]['pageid']
        return page_id


def geosearch_page_id_query(lat, lon):
    """"""
    session = requests.Session()

    url = "https://fr.wikipedia.org/w/api.php"

    coords = str(lat) + "|" + str(lon)

    params = {
        'action': 'query',
        'list': 'geosearch',
        'format': 'json',
        'gscoord': coords,
        'gsradius': '100',
        'gslimit': '5',
        'utf8': ''
    }

    result = session.get(url=url, params=params)
    data = result.json()
    if "error" in data.keys():
        return "error"
    elif len(data["query"]["geosearch"]) == 0:
        return "no_info"
    elif len(data["query"]["geosearch"]) > 0:
        return data["query"]['geosearch'][0]['pageid']


def search_page_summary_query(page_id):
    """"""
    if type(page_id) is not int:
        return TypeError
    elif type(page_id) is int:
        session = requests.Session()

        url = "https://fr.wikipedia.org/w/api.php"

        params = {
            'action': 'query',
            'format': 'json',
            'prop': 'extracts',
            'exintro': '',
            'explaintext': '',
            'utf8': '',
            'pageids': str(page_id)
        }

        result = session.get(url=url, params=params)
        data = result.json()

        return data['query']['pages'][str(page_id)]['extract']
