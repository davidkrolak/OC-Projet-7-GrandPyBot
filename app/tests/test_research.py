from app.research import Research


# Request parser tests
def test_request_parser_normal_sentence():
    r = Research("Salut, peux tu me parler de Montpellier ?")
    r._request_parser()
    assert r.user_request == "montpellier"


def test_request_parser_no_input():
    r = Research("")
    r._request_parser()
    assert r.user_request == ""


def test_request_parser_punctuation_input():
    r = Research("!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~")
    r._request_parser()
    assert r.user_request == ""


# Google Places request tests
def test_google_places_request_zero_results(monkeypatch):
    """"""

    def mock_return(user_request):
        return "ZERO_RESULTS"

    monkeypatch.setattr('app.api_calls.google_places.search_places',
                        mock_return)

    r = Research("")
    r._google_places_request()
    assert r.status == "google_zero_results"


def test_google_places_request_over_query_limit(monkeypatch):
    """"""

    def mock_return(user_request):
        return "OVER_QUERY_LIMIT"

    monkeypatch.setattr('app.api_calls.google_places.search_places',
                        mock_return)

    r = Research("")
    r._google_places_request()
    assert r.status == "google_over_query_limit"


def test_google_places_request_request_denied(monkeypatch):
    """"""

    def mock_return(user_request):
        return "REQUEST_DENIED"

    monkeypatch.setattr('app.api_calls.google_places.search_places',
                        mock_return)

    r = Research("")
    r._google_places_request()
    assert r.status == "google_request_denied"


def test_google_places_request_invalid_request(monkeypatch):
    """"""

    def mock_return(user_request):
        return "INVALID_REQUEST"

    monkeypatch.setattr('app.api_calls.google_places.search_places',
                        mock_return)

    r = Research("")
    r._google_places_request()
    assert r.status == "google_invalid_request"


def test_google_places_request_unknown_error(monkeypatch):
    """"""

    def mock_return(user_request):
        return "UNKNOWN_ERROR"

    monkeypatch.setattr('app.api_calls.google_places.search_places',
                        mock_return)

    r = Research("")
    r._google_places_request()
    assert r.status == "google_unknown_error"


def test_google_places_request_normal_case(monkeypatch):
    """"""

    def mock_return(user_request):
        r = {'name': 'test',
             'formatted_address': 'test',
             'geometry': {'location': {'lat': 'test',
                                       'lng': 'test'}}}
        return r

    monkeypatch.setattr('app.api_calls.google_places.search_places',
                        mock_return)

    r = Research("")
    r._google_places_request()
    assert r.name == 'test'
    assert r.formatted_address == 'test'
    assert r.lat == 'test'
    assert r.lng == 'test'


# Wikimedia page id request tests
def test_wikimedia_page_id_request_wrong_status():
    """"""
    r = Research("")
    r.status = "google_error"
    r._wikimedia_page_id_request()

    assert r.status == "google_error"


def test_wikimedia_page_id_request_error_500(monkeypatch):
    """"""

    def mock_return(name):
        return "wikimedia_error_500"

    monkeypatch.setattr('app.api_calls.wikimedia.search_page_id', mock_return)

    r = Research("user_input")
    r.status = "google_ok"
    r._wikimedia_page_id_request()

    assert r.status == "wikimedia_error_500"


def test_wikimedia_page_id_request_error_504(monkeypatch):
    """"""

    def mock_return(name):
        return "wikimedia_error_504"

    monkeypatch.setattr('app.api_calls.wikimedia.search_page_id', mock_return)

    r = Research("user_input")
    r.status = "google_ok"
    r._wikimedia_page_id_request()

    assert r.status == "wikimedia_error_504"


def test_wikimedia_page_id_request_error_400(monkeypatch):
    """"""

    def mock_return(name):
        return "wikimedia_error_400"

    monkeypatch.setattr('app.api_calls.wikimedia.search_page_id', mock_return)

    r = Research("user_input")
    r.status = "google_ok"
    r._wikimedia_page_id_request()

    assert r.status == "wikimedia_error_400"


def test_wikimedia_page_id_request_error_404(monkeypatch):
    """"""

    def mock_return(name):
        return "wikimedia_error_404"

    monkeypatch.setattr('app.api_calls.wikimedia.search_page_id', mock_return)

    r = Research("user_input")
    r.status = "google_ok"
    r._wikimedia_page_id_request()

    assert r.status == "wikimedia_error_404"


def test_wikimedia_page_id_request_undefined_error(monkeypatch):
    """"""

    def mock_return(name):
        return "error"

    monkeypatch.setattr('app.api_calls.wikimedia.search_page_id', mock_return)

    r = Research("user_input")
    r.status = "google_ok"
    r._wikimedia_page_id_request()

    assert r.status == "wikimedia_api_error"


def test_wikimedia_page_id_request_zero_results(monkeypatch):
    """"""

    def mock_return(name):
        return "zero_results"

    monkeypatch.setattr('app.api_calls.wikimedia.search_page_id', mock_return)

    r = Research("user_input")
    r.status = "google_ok"
    r._wikimedia_page_id_request()

    assert r.status == "wikimedia_zero_results"


def test_wikimedia_page_id_normal_case(monkeypatch):
    """"""

    def mock_return(name):
        return 1

    monkeypatch.setattr('app.api_calls.wikimedia.search_page_id', mock_return)

    r = Research("user_input")
    r.status = "google_ok"
    r._wikimedia_page_id_request()

    assert r.status == "wikimedia_page_id_ok"
    assert r.wiki_page_id == 1


# Wikimedia page summary request tests
def test_wikimedia_page_summary_request_wrong_status():
    """"""

    r = Research("")
    r.status = "wikimedia_error"
    r._wikimedia_page_summary_request()

    assert r.status == "wikimedia_error"


def test_wikimedia_page_summary_request_error_500(monkeypatch):
    """"""

    def mock_return(name):
        return "wikimedia_error_500"

    monkeypatch.setattr('app.api_calls.wikimedia.search_page_summary',
                        mock_return)

    r = Research("user_input")
    r.status = "wikimedia_page_id_ok"
    r._wikimedia_page_summary_request()

    assert r.status == "wikimedia_error_500"


def test_wikimedia_page_summary_request_error_504(monkeypatch):
    """"""

    def mock_return(name):
        return "wikimedia_error_504"

    monkeypatch.setattr('app.api_calls.wikimedia.search_page_summary',
                        mock_return)

    r = Research("user_input")
    r.status = "wikimedia_page_id_ok"
    r._wikimedia_page_summary_request()

    assert r.status == "wikimedia_error_504"


def test_wikimedia_page_summary_request_error_400(monkeypatch):
    """"""

    def mock_return(name):
        return "wikimedia_error_400"

    monkeypatch.setattr('app.api_calls.wikimedia.search_page_summary',
                        mock_return)

    r = Research("user_input")
    r.status = "wikimedia_page_id_ok"
    r._wikimedia_page_summary_request()

    assert r.status == "wikimedia_error_400"


def test_wikimedia_page_summary_request_error_404(monkeypatch):
    """"""

    def mock_return(name):
        return "wikimedia_error_404"

    monkeypatch.setattr('app.api_calls.wikimedia.search_page_summary',
                        mock_return)

    r = Research("user_input")
    r.status = "wikimedia_page_id_ok"
    r._wikimedia_page_summary_request()

    assert r.status == "wikimedia_error_404"


def test_wikimedia_page_summary_request_no_summary(monkeypatch):
    """"""

    def mock_return(name):
        return "no_summary"

    monkeypatch.setattr('app.api_calls.wikimedia.search_page_summary',
                        mock_return)

    r = Research("user_input")
    r.status = "wikimedia_page_id_ok"
    r._wikimedia_page_summary_request()

    assert r.status == "wikimedia_zero_results"


def test_wikimedia_page_summary_normal_case(monkeypatch):
    """"""

    def mock_return(page_id):
        return "test"

    monkeypatch.setattr('app.api_calls.wikimedia.search_page_summary',
                        mock_return)

    r = Research("user_input")
    r.status = "wikimedia_page_id_ok"
    r._wikimedia_page_summary_request()

    assert r.status == "wikimedia_page_summary_ok"
    assert r.wiki_summary == "test"


# Wikimedia page url request tests
def test_wikimedia_page_url_request_wrong_status():
    """"""

    r = Research("")
    r.status = "wikimedia_zero_results"
    r._wikimedia_page_url_request()

    assert r.status == "wikimedia_zero_results"


def test_wikimedia_page_url_request_error_500(monkeypatch):
    """"""

    def mock_return(name):
        return "wikimedia_error_500"

    monkeypatch.setattr('app.api_calls.wikimedia.search_page_url',
                        mock_return)

    r = Research("user_input")
    r.status = "wikimedia_page_summary_ok"
    r._wikimedia_page_url_request()

    assert r.status == "wikimedia_error_500"


def test_wikimedia_page_url_request_error_504(monkeypatch):
    """"""

    def mock_return(name):
        return "wikimedia_error_504"

    monkeypatch.setattr('app.api_calls.wikimedia.search_page_url',
                        mock_return)

    r = Research("user_input")
    r.status = "wikimedia_page_summary_ok"
    r._wikimedia_page_url_request()

    assert r.status == "wikimedia_error_504"


def test_wikimedia_page_url_request_error_400(monkeypatch):
    """"""

    def mock_return(name):
        return "wikimedia_error_400"

    monkeypatch.setattr('app.api_calls.wikimedia.search_page_url',
                        mock_return)

    r = Research("user_input")
    r.status = "wikimedia_page_summary_ok"
    r._wikimedia_page_url_request()

    assert r.status == "wikimedia_error_400"


def test_wikimedia_page_url_request_error_404(monkeypatch):
    """"""

    def mock_return(name):
        return "wikimedia_error_404"

    monkeypatch.setattr('app.api_calls.wikimedia.search_page_url',
                        mock_return)

    r = Research("user_input")
    r.status = "wikimedia_page_summary_ok"
    r._wikimedia_page_url_request()

    assert r.status == "wikimedia_error_404"


def test_wikimedia_page_url_request_no_url(monkeypatch):
    """"""

    def mock_return(name):
        return "no_url"

    monkeypatch.setattr('app.api_calls.wikimedia.search_page_url',
                        mock_return)

    r = Research("user_input")
    r.status = "wikimedia_page_summary_ok"
    r._wikimedia_page_url_request()

    assert r.status == "wikimedia_no_page_url"


def test_wikimedia_page_url_request_normal_case(monkeypatch):
    """"""

    def mock_return(name):
        return "test"

    monkeypatch.setattr('app.api_calls.wikimedia.search_page_url',
                        mock_return)

    r = Research("user_input")
    r.status = "wikimedia_page_summary_ok"
    r._wikimedia_page_url_request()

    assert r.status == "wikimedia_page_url_ok"
    assert r.wiki_url == "test"
