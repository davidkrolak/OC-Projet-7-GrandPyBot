from app.search import search_script, request_parser


def test_request_parser_1():
    """"""
    request_1 = "Salut papy ! je cherche l'adresse d'openclassrooms"
    assert request_parser(request_1) == "openclassrooms"

    request_2 = "Hello, parle moi de l'arc de triomphe"
    assert request_parser(request_2) == "arc triomphe"

    request_3 = "peux tu me parler de paris de ton enfance"
    assert request_parser(request_3) == "paris enfance"


def test_search_script_1():
    """"""
    request_1 = "peux tu me parler de la place de la comédie ?"
    result_1 = search_script(request_1)
    assert result_1["id"] == "8312dd8ab88cea897f1f5b1949a0d7ff51b4fc4f"
    assert result_1["name"] == "Place de la Comédie"
    assert result_1["formatted_address"] == "Place de la Comédie, " \
                                            "34000 Montpellier, " \
                                            "France"
    assert result_1["lat"] == 43.60870240000001
    assert result_1["lng"] == 3.88034
    assert result_1["wiki_summary"][0:20] == "La place de la Coméd"
    assert result_1["status"] == "ok"
