from app.api_calls.wikimedia import search_page_id, \
    search_page_summary


def test_search_page_id():
    """Mocks for the research of page id in the wikimedia api"""
    # Correct spelling test queries
    assert search_page_id("Montpellier") == 4038983

    assert search_page_id("Paris") == 681159

    assert search_page_id('Openclassrooms') == 4338589

    # Test spelling mistake
    assert search_page_id('Openclasrom') == 4338589
    # No input search query
    assert search_page_id("") == "nosrsearch"
    # Misleading search query
    assert search_page_id("asdfgasdfg") == "zero_results"


def test_page_summary_text():
    """Mocks for the summary query to the wikimedia api"""
    assert search_page_summary('asf') == TypeError

    assert type(search_page_summary(4038983)) == str

    assert search_page_summary(4038983)[0:10] == 'Montpellie'
