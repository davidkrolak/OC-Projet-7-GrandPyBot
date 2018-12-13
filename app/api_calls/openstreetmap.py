import requests


def search_query(research):
    """"""
    session = requests.Session()
    url = "https://nominatim.openstreetmap.org/search?"
    params = {
        'q': str(research),
        'format': 'json',
        'extratags': 1,
        'namedetails': 1
    }
    result = session.get(url=url, params=params)
    data = result.json()
    openstreetmap_data = {"lat": None,
                          "lon": None,
                          "display_name": None
                          }
    if len(data) == 0:
        return 0
    elif len(data) > 0:
        if "lat" in data[0].keys():
            lat = float(data[0]['lat'])
            openstreetmap_data['lat'] = lat
        if "lon" in data[0].keys():
            lon = float(data[0]['lon'])
            openstreetmap_data['lon'] = lon
        if "display_name" in data[0].keys():
            display_name = data[0]['display_name']
            openstreetmap_data['display_name'] = display_name

    return openstreetmap_data
