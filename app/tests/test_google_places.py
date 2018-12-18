from app.api_calls.google_places import search_query

def test_search_query_1():
    magic_pizza = search_query("pizza a la valsiere")
    assert magic_pizza["id"] == "4f98191f37d122d7758a4875b4ee7eb13b3782f9"
    assert magic_pizza["name"] == "Magic Pizza"
    assert magic_pizza["formatted_address"] == "2 Rue Nicolas Appert, " \
                                               "34790 Grabels, " \
                                               "France"
def test_search_query_2():
    openclassrooms = search_query("Openclassrooms")
    assert openclassrooms["id"] ==
    assert openclassrooms["name"] == "Openclassrooms"