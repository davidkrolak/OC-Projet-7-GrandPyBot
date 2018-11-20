from API_calls.wikimedia_calls import *

def test_page_id_search_1():
    '''Test if the research get the proper page id'''

    assert search_page_by_id('Montpellier') == 4038983
    assert search_page_by_id('Paris') == 681159
    assert search_page_by_id('Toulouse') == 2996
    assert search_page_by_id('Openclassrooms') == 4338589
    assert search_page_by_id('Openclasrom') == 4338589
