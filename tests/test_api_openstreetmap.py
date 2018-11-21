import string
from api_calls.openstreetmap_calls import *


def test_search_lat_lon():
    assert search_lat_lon('Montpellier') == \
           (43.6112422, 3.8767337)
    assert search_lat_lon('Place de la comédie') == \
           (43.6086897, 3.87991789999031)
