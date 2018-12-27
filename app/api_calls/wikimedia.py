import requests


def search_page_id_query(research, tries=0):
    """Request for a wikipedia page id based on a string query we send to the
    wikimedia API and return it"""
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
    tries += 1

    # http code response management
    if result.status_code == 500:
        return "wikimedia_error_500"
    elif result.status_code == 504 and tries <=2:
        search_page_id_query(research, tries)
    elif result.status_code == 504 and tries > 2:
        return "wikimedia_error_504"
    elif result.status_code == 400:
        return "wikimedia_error_400"
    elif result.status_code == 404:
        return "wikimedia_error_404"
    elif result.status_code == 200:
        data = result.json()
        if "error" in data.keys():
            return data["error"]["code"]

        if data['query']['searchinfo']['totalhits'] == 0:
            return "zero_results"

        elif data['query']['searchinfo']['totalhits'] >= 1:
            page_id = data['query']['search'][0]['pageid']
            return page_id


def search_page_summary_query(page_id, tries=0):
    """Request the summary from a wikipedia page to the wikimedia API
    with the page id and return it in a string format"""
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
        tries =+ 1

        if result.status_code == 500:
            return "wikimedia_error_500"
        elif result.status_code == 504 and tries <=2:
            search_page_summary_query(page_id, tries)
        elif result.status_code == 504 and tries > 2:
            return "wikimedia_error_504"
        elif result.status_code == 400:
            return "wikimedia_error_400"
        elif result.status_code == 404:
            return "wikimedia_error_404"
        elif result.status_code == 200:
            data = result.json()
            if "extract" in data["query"]["pages"][str(page_id)].keys():
                summary = data['query']['pages'][str(page_id)]['extract']
            else:
                summary = "no_summary"

            return summary
