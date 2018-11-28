import string
from GrandPyBot.api_calls.wikimedia_calls import *


def test_search_page_id_1():
    """Classic test with somehow correct input where the result should always
    be True"""

    assert search_page_id('Montpellier') == 4038983
    assert search_page_id('Paris') == 681159
    assert search_page_id('Openclassrooms') == 4338589
    assert search_page_id('Openclasrom') == 4338589  # test spelling


def test_search_page_id_2():
    assert search_page_id('') == 0
    # test query with no input

    assert search_page_id('fdsfdjsfds') == -1
    # misleading query with no results

    assert search_page_id('Montpellier' + string.punctuation) == 4038983
    # test if wikimedia filter punctuation in the queries


def test_page_summary_text():
    assert page_summary_text('asf') == TypeError
    assert type(page_summary_text(4038983)) == str
    assert page_summary_text(4038983)[0:10] == 'Montpellie'
