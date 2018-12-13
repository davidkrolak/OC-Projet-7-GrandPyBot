from app.api_calls.wikimedia import search_page_id_query, \
    search_page_summary_query, geosearch_page_id_query


def test_search_page_id():
    # Correct spelling test queries
    assert search_page_id_query("Montpellier") == 4038983
    assert search_page_id_query("Paris") == 681159
    assert search_page_id_query('Openclassrooms') == 4338589

    # Test spelling mistake
    assert search_page_id_query('Openclasrom') == 4338589

    # No input search query
    assert search_page_id_query("") == 0

    # Misleading search query
    assert search_page_id_query("asdfgasdfg") == -1


def test_geosearch_page_id():
    # Basic geosearch request
    assert geosearch_page_id_query(43.6111337, 3.8724111) == 1951172
    # Real place but with no information on wikipedia about it
    assert geosearch_page_id_query(43.64944305, 3.84171444330414) == "no_info"
    # Wrong input
    assert geosearch_page_id_query(43, "a") == "error"

def test_page_summary_text():
    assert search_page_summary_query('asf') == TypeError
    assert type(search_page_summary_query(4038983)) == str
    assert search_page_summary_query(4038983)[0:10] == 'Montpellie'
