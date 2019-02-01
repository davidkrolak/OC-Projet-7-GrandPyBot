from app.research import Research


def test_request_parser_normal_sentence():
    research = Research("Salut, peux tu me parler de Montpellier ?")
    assert research.user_request == "montpellier"


def test_request_parser_complex_sentence():
    research = Research("Bonjour Grandpy, peux tu me parler de l'arc de "
                        "triomphe à Paris ?")
    assert research.user_request == "arc triomphe paris"
