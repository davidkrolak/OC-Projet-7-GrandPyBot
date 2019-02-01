from app.api_calls.google_places import search_places


def test_search_query_1():
    magic_pizza = search_places("pizza a la valsiere")
    assert magic_pizza["id"] == "4f98191f37d122d7758a4875b4ee7eb13b3782f9"
    assert magic_pizza["name"] == "Magic Pizza"
    assert magic_pizza["formatted_address"] == "2 Rue Nicolas Appert, " \
                                               "34790 Grabels, " \
                                               "France"


def test_search_query_2():
    openclassrooms = search_places("Openclassrooms")
    assert openclassrooms["id"] == 'dd80dc7de1802674cba35cce4e303e6862a4f3ed'
    assert openclassrooms["name"] == "Openclassrooms"
    assert openclassrooms['formatted_address'] == '7 Cité Paradis, ' \
                                                  '75010 Paris, ' \
                                                  'France'
    assert openclassrooms["geometry"]["location"]["lat"] == 48.8747265
    assert openclassrooms["geometry"]["location"]["lng"] == 2.3505517


def test_search_query_3():
   misleading_request = search_places("fdsjfdslfkjsdlkhfiuerw")
   assert misleading_request == "ZERO_RESULTS"