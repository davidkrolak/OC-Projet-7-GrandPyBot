from app import app
import googlemaps


gmaps = googlemaps.Client(key="AIzaSyBPRJOkFSSGVNTOGiweoXQHX4fybc4veDs")

def search_query(research):
    research_prediction = gmaps.places_autocomplete_query(str(research))
    google_places_results = gmaps.places(research_prediction[0]["description"])
    result = google_places_results["results"][0]
    return result
