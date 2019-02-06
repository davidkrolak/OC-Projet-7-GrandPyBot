import pytest
import requests

from app.api_calls import wikimedia


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr("requests.sessions.Session.request")


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
