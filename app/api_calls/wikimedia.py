import requests


def search_page_id(research):
    """Request for a wikipedia page id based on a string query we send to the
    wikimedia API and return it"""

    url = "https://fr.wikipedia.org/w/api.php"

    params = {
        'action': 'query',
        'list': 'search',
        'format': 'json',
        'utf8': '',
        'srsearch': research
    }

    result = requests.get(url=url, params=params)
    # The function will request 3 times the api server if it return
    # a 504 http code

    # http code response management
    if result.status_code == 500:
        return "wikimedia_error_500"
    elif result.status_code == 504:
        return "wikimedia_error_504"
    elif result.status_code == 400:
        return "wikimedia_error_400"
    elif result.status_code == 404:
        return "wikimedia_error_404"
    elif result.status_code == 200:
        data = result.json()

        if "error" in data.keys():
            return "error"

        if data['query']['searchinfo']['totalhits'] == 0:
            return "zero_results"

        elif data['query']['searchinfo']['totalhits'] >= 1:
            page_id = data['query']['search'][0]['pageid']
            return page_id


def search_page_summary(page_id, tries=0):
    """Request the summary from a wikipedia page to the wikimedia API
    with the page id and return it in a string format"""
    if type(page_id) is not int:
        return TypeError
    elif type(page_id) is int:
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
        tries += 1
        # The function will request 3 times the api server if it return
        # a 504 http code

        if result.status_code == 500:
            return "wikimedia_error_500"
        elif result.status_code == 504 and tries <= 2:
            search_page_summary(page_id, tries)
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
                return summary
            else:
                return "no_summary"


def search_page_url(page_id, tries=0):
    """"""
    if type(page_id) is not int:
        return TypeError
    elif type(page_id) is int:
        url = "https://fr.wikipedia.org/w/api.php"

        params = {
            'action': 'query',
            'format': 'json',
            'prop': 'info',
            'inprop': 'url',
            'pageids': str(page_id)
        }

        result = session.get(url=url, params=params)
        tries += 1
        # The function will request 3 times the api server if it return
        # a 504 http code

        if result.status_code == 500:
            return "wikimedia_error_500"
        elif result.status_code == 504 and tries <= 2:
            search_page_summary(page_id, tries)
        elif result.status_code == 504 and tries > 2:
            return "wikimedia_error_504"
        elif result.status_code == 400:
            return "wikimedia_error_400"
        elif result.status_code == 404:
            return "wikimedia_error_404"
        elif result.status_code == 200:
            data = result.json()

            if "fullurl" in data["query"]["pages"][str(page_id)].keys():
                wikipedia_url = data['query']['pages'][str(page_id)]['fullurl']
            else:
                wikipedia_url = "no_url"

            return wikipedia_url
