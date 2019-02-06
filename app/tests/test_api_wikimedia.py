import pytest
import requests

from app.api_calls import wikimedia


# Forbide request library to do http calls
@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr("requests.sessions.Session.request")


# Search page id function tests
def test_search_page_id_status_code_500(monkeypatch):
    """"""

    def get_mock(url, params):
        r = requests.Response()
        r.status_code = 500
        return r

    monkeypatch.setattr('app.api_calls.wikimedia.requests.get', get_mock)

    assert wikimedia.search_page_id('research') == 'wikimedia_error_500'


def test_search_page_id_status_code_504(monkeypatch):
    """"""

    def get_mock(url, params):
        r = requests.Response()
        r.status_code = 504
        return r

    monkeypatch.setattr('app.api_calls.wikimedia.requests.get', get_mock)

    assert wikimedia.search_page_id('research') == 'wikimedia_error_504'


def test_search_page_id_status_code_400(monkeypatch):
    """"""

    def get_mock(url, params):
        r = requests.Response()
        r.status_code = 400
        return r

    monkeypatch.setattr('app.api_calls.wikimedia.requests.get', get_mock)

    assert wikimedia.search_page_id('research') == 'wikimedia_error_400'


def test_search_page_id_status_code_404(monkeypatch):
    """"""

    def get_mock(url, params):
        r = requests.Response()
        r.status_code = 404
        return r

    monkeypatch.setattr('app.api_calls.wikimedia.requests.get', get_mock)

    assert wikimedia.search_page_id('research') == 'wikimedia_error_404'


def test_search_page_id_status_code_200_error(monkeypatch):
    """"""

    def get_mock(url, params):
        r = requests.Response()
        r.status_code = 200
        return r

    def json_mock(data):
        return {'error': 'error'}

    monkeypatch.setattr('app.api_calls.wikimedia.requests.get', get_mock)
    monkeypatch.setattr('app.api_calls.wikimedia.requests.Response.json',
                        json_mock)

    assert wikimedia.search_page_id('research') == 'error'


def test_search_page_id_status_code_200_zero_results(monkeypatch):
    """"""

    def get_mock(url, params):
        r = requests.Response()
        r.status_code = 200
        return r

    def json_mock(data):
        return {'query': {'searchinfo': {'totalhits': 0}}}

    monkeypatch.setattr('app.api_calls.wikimedia.requests.get', get_mock)
    monkeypatch.setattr('app.api_calls.wikimedia.requests.Response.json',
                        json_mock)

    assert wikimedia.search_page_id('research') == 'zero_results'


def test_search_page_id_normal_case(monkeypatch):
    """"""

    def get_mock(url, params):
        r = requests.Response()
        r.status_code = 200
        return r

    def json_mock(data):
        return {'query': {'searchinfo': {'totalhits': 1},
                          'search': [{'pageid': 1}]}}

    monkeypatch.setattr('app.api_calls.wikimedia.requests.get', get_mock)
    monkeypatch.setattr('app.api_calls.wikimedia.requests.Response.json',
                        json_mock)

    assert wikimedia.search_page_id('research') == 1


# Search page summary function tests
def test_search_page_summary_wrong_input_type():
    assert wikimedia.search_page_summary('hello') == TypeError
    assert wikimedia.search_page_summary(['hello']) == TypeError
    assert wikimedia.search_page_summary({'hello': 1}) == TypeError
    assert wikimedia.search_page_summary((1, 2)) == TypeError


def test_search_page_summary_status_code_500(monkeypatch):
    """"""

    def get_mock(url, params):
        r = requests.Response()
        r.status_code = 500
        return r

    monkeypatch.setattr('app.api_calls.wikimedia.requests.get', get_mock)

    assert wikimedia.search_page_summary(1) == 'wikimedia_error_500'


def test_search_page_summary_status_code_504(monkeypatch):
    """"""

    def get_mock(url, params):
        r = requests.Response()
        r.status_code = 504
        return r

    monkeypatch.setattr('app.api_calls.wikimedia.requests.get', get_mock)

    assert wikimedia.search_page_summary(1) == 'wikimedia_error_504'


def test_search_page_summary_status_code_400(monkeypatch):
    """"""

    def get_mock(url, params):
        r = requests.Response()
        r.status_code = 400
        return r

    monkeypatch.setattr('app.api_calls.wikimedia.requests.get', get_mock)

    assert wikimedia.search_page_summary(1) == 'wikimedia_error_400'


def test_search_page_summary_status_code_404(monkeypatch):
    """"""

    def get_mock(url, params):
        r = requests.Response()
        r.status_code = 404
        return r

    monkeypatch.setattr('app.api_calls.wikimedia.requests.get', get_mock)

    assert wikimedia.search_page_summary(1) == 'wikimedia_error_404'


def test_search_page_summary_code_200_error(monkeypatch):
    """"""

    def get_mock(url, params):
        r = requests.Response()
        r.status_code = 200
        return r

    def json_mock(data):
        return {'error': 'error'}

    monkeypatch.setattr('app.api_calls.wikimedia.requests.get', get_mock)
    monkeypatch.setattr('app.api_calls.wikimedia.requests.Response.json',
                        json_mock)

    assert wikimedia.search_page_summary(1) == 'error'


def test_search_page_summary_code_200_no_summary(monkeypatch):
    """"""

    def get_mock(url, params):
        r = requests.Response()
        r.status_code = 200
        return r

    def json_mock(data):
        return {'query': {'pages': {'1': {'test': 'test'}}}}

    monkeypatch.setattr('app.api_calls.wikimedia.requests.get', get_mock)
    monkeypatch.setattr('app.api_calls.wikimedia.requests.Response.json',
                        json_mock)

    assert wikimedia.search_page_summary(1) == 'no_summary'


def test_search_page_summary_normal_case(monkeypatch):
    """"""

    def get_mock(url, params):
        r = requests.Response()
        r.status_code = 200
        return r

    def json_mock(data):
        return {'query': {'pages': {'1': {'extract': 'test'}}}}

    monkeypatch.setattr('app.api_calls.wikimedia.requests.get', get_mock)
    monkeypatch.setattr('app.api_calls.wikimedia.requests.Response.json',
                        json_mock)

    assert wikimedia.search_page_summary(1) == 'test'


# Search page url function tests
def test_search_page_url_wrong_input_type():
    assert wikimedia.search_page_url('hello') == TypeError
    assert wikimedia.search_page_url(['hello']) == TypeError
    assert wikimedia.search_page_url({'hello': 1}) == TypeError
    assert wikimedia.search_page_url((1, 2)) == TypeError


def test_search_page_url_status_code_500(monkeypatch):
    """"""

    def get_mock(url, params):
        r = requests.Response()
        r.status_code = 500
        return r

    monkeypatch.setattr('app.api_calls.wikimedia.requests.get', get_mock)

    assert wikimedia.search_page_url(1) == 'wikimedia_error_500'


def test_search_page_url_status_code_504(monkeypatch):
    """"""

    def get_mock(url, params):
        r = requests.Response()
        r.status_code = 504
        return r

    monkeypatch.setattr('app.api_calls.wikimedia.requests.get', get_mock)

    assert wikimedia.search_page_url(1) == 'wikimedia_error_504'


def test_search_page_url_status_code_400(monkeypatch):
    """"""

    def get_mock(url, params):
        r = requests.Response()
        r.status_code = 400
        return r

    monkeypatch.setattr('app.api_calls.wikimedia.requests.get', get_mock)

    assert wikimedia.search_page_url(1) == 'wikimedia_error_400'


def test_search_page_url_status_code_404(monkeypatch):
    """"""

    def get_mock(url, params):
        r = requests.Response()
        r.status_code = 404
        return r

    monkeypatch.setattr('app.api_calls.wikimedia.requests.get', get_mock)

    assert wikimedia.search_page_url(1) == 'wikimedia_error_404'


def test_search_page_url_code_200_error(monkeypatch):
    """"""

    def get_mock(url, params):
        r = requests.Response()
        r.status_code = 200
        return r

    def json_mock(data):
        return {'error': 'error'}

    monkeypatch.setattr('app.api_calls.wikimedia.requests.get', get_mock)
    monkeypatch.setattr('app.api_calls.wikimedia.requests.Response.json',
                        json_mock)

    assert wikimedia.search_page_url(1) == 'error'


def test_search_page_url_code_200_no_url(monkeypatch):
    """"""

    def get_mock(url, params):
        r = requests.Response()
        r.status_code = 200
        return r

    def json_mock(data):
        return {'query': {'pages': {'1': {'test': 'test'}}}}

    monkeypatch.setattr('app.api_calls.wikimedia.requests.get', get_mock)
    monkeypatch.setattr('app.api_calls.wikimedia.requests.Response.json',
                        json_mock)

    assert wikimedia.search_page_url(1) == 'no_url'


def test_search_page_url_normal_case(monkeypatch):
    """"""

    def get_mock(url, params):
        r = requests.Response()
        r.status_code = 200
        return r

    def json_mock(data):
        return {'query': {'pages': {'1': {'fullurl': 'test'}}}}

    monkeypatch.setattr('app.api_calls.wikimedia.requests.get', get_mock)
    monkeypatch.setattr('app.api_calls.wikimedia.requests.Response.json',
                        json_mock)

    assert wikimedia.search_page_url(1) == 'test'
