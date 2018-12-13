from app.api_calls.openstreetmap import search_query


def test_search_query_montpellier():
    result = search_query("Montpellier")

    assert result["lat"] == 43.6112422
    assert result["lon"] == 3.8767337
    assert result["display_name"] == "Montpellier, Hérault, Occitanie, " \
                                     "France métropolitaine, France"


def test_search_query_tour_eiffel():
    result = search_query("tour eiffel")

    assert result["lat"] == 48.8582602
    assert result["lon"] == 2.29449905431968
    assert result["display_name"] == "Tour Eiffel, 5, Avenue Anatole France," \
                                     " Gros-Caillou, 7e, Paris, Île-de-France," \
                                     " France métropolitaine, 75007, France"


def test_search_query_no_result():
    assert search_query("asdffdsg") == 0
