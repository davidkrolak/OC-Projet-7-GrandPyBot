import pytest

from app.api_calls import wikimedia


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr("requests.sessions.Session.request")


def test_search_page_id_status_code_500(monkeypatch):
    """"""
    result = {'status_code': 500}

    monkeypatch.setattr()

    assert wikimedia.search_page_id('research') == 'wikimedia_error_500'

