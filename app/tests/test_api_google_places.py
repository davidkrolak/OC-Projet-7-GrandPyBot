from app.api_calls import google_places


def test_invalid_request_len_0():
    assert google_places.search_places("") == "INVALID_REQUEST"


def test_places_autocomplete_zero_results(monkeypatch):
    """Mock cases where the google places autocomplete function find no results"""

    def zero_result(places_autocomplete_query):
        return []

    monkeypatch.setattr(
            'app.api_calls.google_places.gmaps.places_autocomplete_query',
                        zero_result)

    assert google_places.search_places('research') == 'ZERO_RESULTS'


def test_google_places_zero_results(monkeypatch):
    """"""
    google_places_results = {'status': 'ZERO_RESULTS',
                             'description': 'description'}

    def autocomplete_results(places_autocomplete_query):
        return [google_places_results]

    def zero_result(places):
        return google_places_results

    monkeypatch.setattr(google_places.gmaps, 'places_autocomplete_query',
                        autocomplete_results)
    monkeypatch.setattr(google_places.gmaps, 'places', zero_result)

    assert google_places.search_places('research') == 'ZERO_RESULTS'


def test_google_places_request_denied(monkeypatch):
    """"""
    google_places_results = {'status': 'REQUEST_DENIED',
                             'description': 'description'}

    def autocomplete_results(places_autocomplete_query):
        return [google_places_results]

    def request_denied(places):
        return google_places_results

    monkeypatch.setattr(google_places.gmaps, 'places_autocomplete_query',
                        autocomplete_results)
    monkeypatch.setattr(google_places.gmaps, 'places', request_denied)

    assert google_places.search_places('research') == 'REQUEST_DENIED'


def test_google_places_invalid_request(monkeypatch):
    """"""
    google_places_results = {'status': 'INVALID_REQUEST',
                             'description': 'description'}

    def autocomplete_results(places_autocomplete_query):
        return [google_places_results]

    def invalid_request(places):
        return google_places_results

    monkeypatch.setattr(google_places.gmaps, 'places_autocomplete_query',
                        autocomplete_results)
    monkeypatch.setattr(google_places.gmaps, 'places', invalid_request)

    assert google_places.search_places('research') == 'INVALID_REQUEST'


def test_google_places_unknown_error(monkeypatch):
    """"""
    google_places_results = {'status': 'UNKNOWN_ERROR',
                             'description': 'description'}

    def autocomplete_results(places_autocomplete_query):
        return [google_places_results]

    def unknown_error(places):
        return google_places_results

    monkeypatch.setattr(google_places.gmaps, 'places_autocomplete_query',
                        autocomplete_results)
    monkeypatch.setattr(google_places.gmaps, 'places', unknown_error)

    assert google_places.search_places('research') == 'UNKNOWN_ERROR'


def test_google_places_ok(monkeypatch):
    """"""
    google_places_results = {'status': 'OK',
                             'description': 'description',
                             'results': ['result']}

    def autocomplete_results(places_autocomplete_query):
        return [google_places_results]

    def ok_status(places):
        return google_places_results

    monkeypatch.setattr(google_places.gmaps, 'places_autocomplete_query',
                        autocomplete_results)
    monkeypatch.setattr(google_places.gmaps, 'places', ok_status)

    assert google_places.search_places('research') == 'result'


