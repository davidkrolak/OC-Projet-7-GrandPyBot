from app.research import *


def test_search_script_1():
    """Basic search request"""
    user_request = "peux tu me parler de la place de la comédie ?"
    result = search_script(user_request)
    assert result["id"] == "8312dd8ab88cea897f1f5b1949a0d7ff51b4fc4f"
    assert result["name"] == "Place de la Comédie"
    assert result["formatted_address"] == "Place de la Comédie, " \
                                          "34000 Montpellier, " \
                                          "France"
    assert result["lat"] == 43.60870240000001
    assert result["lng"] == 3.88034
    assert result["wiki_summary"][0:20] == "La place de la Coméd"
    assert result["status"] == "ok"


def test_search_script_2():
    """Request with no supposed result"""
    user_request = "afhasjhfsajfah"
    result = search_script(user_request)
    assert result["id"] is None
    assert result["name"] is None
    assert result["formatted_address"] is None
    assert result["lat"] is None
    assert result["lng"] is None
    assert result["wiki_summary"] is None
    assert result["status"] == "zero_results"


def test_search_script_3():
    """Request with en empty string"""
    user_request = ""
    result = search_script(user_request)
    assert result["id"] is None
    assert result["name"] is None
    assert result["formatted_address"] is None
    assert result["lat"] is None
    assert result["lng"] is None
    assert result["wiki_summary"] is None
    assert result["status"] == "error"


def test_request_parser_1():
    """Self explanatory, should parse the user request, remove punctuation,
    lower the string and delete words from the request who are in the stop
    words list"""
    request_1 = "Salut papy ! je cherche l'adresse d'openclassrooms"
    assert request_parser(request_1) == "openclassrooms"

    request_2 = "Hello, parle moi de l'arc de triomphe"
    assert request_parser(request_2) == "arc triomphe"

    request_3 = "peux tu me parler de paris de ton enfance"
    assert request_parser(request_3) == "paris enfance"


def test_google_api_request_1():
    """Basic test with a response from the google api"""
    response_dict = {"id": None,
                     "name": None,
                     "formatted_address": None,
                     "lat": None,
                     "lng": None,
                     "wiki_summary": None,
                     "grandpy_response": None,
                     "status": None
                     }

    user_request = "place comédie"

    google_api_request(user_request, response_dict)

    assert response_dict["id"] == "8312dd8ab88cea897f1f5b1949a0d7ff51b4fc4f"
    assert response_dict["name"] == "Place de la Comédie"
    assert response_dict["formatted_address"] == "Place de la Comédie, " \
                                                 "34000 Montpellier, " \
                                                 "France"
    assert response_dict["lat"] == 43.60870240000001
    assert response_dict["lng"] == 3.88034
    assert response_dict["status"] is None


def test_google_api_request_2():
    """Request with no results"""
    response_dict = {"id": None,
                     "name": None,
                     "formatted_address": None,
                     "lat": None,
                     "lng": None,
                     "wiki_summary": None,
                     "grandpy_response": None,
                     "status": None
                     }

    user_request = "afhasjhfsajfah"

    google_api_request(user_request, response_dict)

    assert response_dict["id"] is None
    assert response_dict["name"] is None
    assert response_dict["formatted_address"] is None
    assert response_dict["lat"] is None
    assert response_dict["lng"] is None
    assert response_dict["status"] == "zero_results"


def test_google_api_request_3():
    """Empty request test"""
    response_dict = {"id": None,
                     "name": None,
                     "formatted_address": None,
                     "lat": None,
                     "lng": None,
                     "wiki_summary": None,
                     "grandpy_response": None,
                     "status": None
                     }

    user_request = ""

    google_api_request(user_request, response_dict)

    assert response_dict["id"] is None
    assert response_dict["name"] is None
    assert response_dict["formatted_address"] is None
    assert response_dict["lat"] is None
    assert response_dict["lng"] is None
    assert response_dict["status"] == "error"


def test_wikimedia_api_request_1():
    """Test the function for zero_results status in the response dict"""
    response_dict = {"wiki_summary": None,
                     "status": "zero_results"}

    wikimedia_api_request(response_dict)
    assert response_dict["wiki_summary"] is None


def test_wikimedia_api_request_2():
    """Test the function for an error status in the response dict"""
    response_dict = {"wiki_summary": None,
                     "status": "error"}

    wikimedia_api_request(response_dict)
    assert response_dict["wiki_summary"] is None


def test_wikimedia_api_request_3():
    """Test the function for a correct usage case"""
    response_dict = {"name": "montpellier",
                     "wiki_summary": None,
                     "status": None}

    wikimedia_api_request(response_dict)
    assert response_dict["wiki_summary"][0:20] == "Montpellier — pronon"


def test_grandpy_response_1():
    """Test the function for a zero results response"""
    response_dict = {"status": "zero_results",
                     "grandpy_response": None}

    grandpy_response(response_dict)

    assert response_dict["grandpy_response"] in zero_results_responses


def test_grandpy_response_2():
    """Test the function for an error response"""
    response_dict = {"status": "error",
                     "grandpy_response": None}

    grandpy_response(response_dict)

    assert response_dict["grandpy_response"] in error_responses


def test_grandpy_response_3():
    """Test the function for a no info response"""
    response_dict = {"status": "no_info",
                     "grandpy_response": None}

    grandpy_response(response_dict)

    assert response_dict["grandpy_response"] in no_info_responses


def test_grandpy_response_4():
    """Test the function for a correct response"""
    response_dict = {"status": "ok",
                     "grandpy_response": None}

    grandpy_response(response_dict)

    assert response_dict["grandpy_response"] in good_responses


zero_results_responses = [
    "Je ne peux pas répondre à ta question, désolé",
    "J'aimerai pouvoir te répondre mais je suis trop fatigué pour le moment",
    "J'ai peur de ne pas pouvoir t'aider",
    "Mmmh désolé, je ne peux pas te répondre à ce sujet"
]

error_responses = [
    "Je ne peux pas répondre à ta question, désolé",
    "Je crois bien que mes informations à ce sujet sont éronnées, désolé mais je ne vais pas pouvoir te répondre",
    "J'aurais aimé te répondre mais je ne tourne pas rond aujourd'hui"
]

no_info_responses = [
    "Je sais ou c'est mais je ne connais rien à propos de cette endroit",
    "Je connais l'adresse de ce lieu mais je ne pourrais pas t'en dire plus",
    "Je connais ce lieu, malheuresement je ne me souviens pas de son histoire"
]

good_responses = [
    "Oui je connais cette endroit ! Laisse moi t'en parler un peu",
    "Je connais ce lieu ! laisse moi t'en parler"
]
