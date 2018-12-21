from app import app
import googlemaps

gmaps = googlemaps.Client(key="AIzaSyBPRJOkFSSGVNTOGiweoXQHX4fybc4veDs")


def search_query(research):
    research_prediction = gmaps.places_autocomplete_query(str(research))
    if len(research_prediction) == 0:
        return "ZERO_RESULTS"
    else:
        google_places_results = gmaps.places(research_prediction[0]["description"])

    # Check API response status
    if google_places_results["status"] == "ZERO_RESULTS":
        return "ZERO_RESULTS"
    elif google_places_results["status"] == "REQUEST_DENIED":
        return "REQUEST_DENIED"
    elif google_places_results["status"] == "INVALID_REQUEST":
        return "INVALID_REQUEST"
    elif google_places_results["status"] == "UNKNOWN_ERROR":
        return "UNKNOWN_ERROR"
    elif google_places_results["status"] == "OK":
        result = google_places_results["results"][0]
        return result
