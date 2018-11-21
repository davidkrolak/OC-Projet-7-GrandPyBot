import requests


def search_lat_lon(research):
    """"""
    session = requests.Session()

    url = "https://nominatim.openstreetmap.org/search?"

    params = {
        'q': str(research),
        'format': 'json'
    }

    result = session.get(url=url, params=params)
    data = result.json()

    lat = float(data[0]['lat'])
    lon = float(data[0]['lon'])

    return (lat, lon)