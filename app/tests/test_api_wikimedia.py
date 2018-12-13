from app.api_calls.wikimedia import search_page_id_query, \
    search_page_summary_query


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


def test_page_summary_text():
    assert search_page_summary_query('asf') == TypeError
    assert type(search_page_summary_query(4038983)) == str
    assert search_page_summary_query(4038983)[0:10] == 'Montpellie'
