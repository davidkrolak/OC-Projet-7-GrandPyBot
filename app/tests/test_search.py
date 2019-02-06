from app.research import Research



def test_request_parser_normal_sentence():
    """"""
    r = Research("Salut, peux tu me parler de montpellier ?")
    r._request_parser()
    assert r.user_request == "montpellier"