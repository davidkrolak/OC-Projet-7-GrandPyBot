import string
import random
from app.api_calls.wikimedia import search_page_summary_query, \
    search_page_id_query
from app.api_calls.google_places import search_query


def search_script(user_request):
    """"""
    user_request = request_parser(user_request)

    # Create a dict who will be send back to the front-end
    response_dict = {"id": None,
                     "name": None,
                     "formatted_address": None,
                     "lat": None,
                     "lng": None,
                     "wiki_summary": None,
                     "grandpy_response": None,
                     "status": None
                     }

    google_api_request(user_request, response_dict)

    wikimedia_api_request(response_dict)

    grandpy_response(response_dict)

    return response_dict


def request_parser(user_request):
    """Parse the user request in multiple words, then check if those one are
    punctuation or not and finally delete the words in the request who matchs
    our stop words list"""

    filtered_request = []
    for character in string.punctuation:
        if character in user_request:
            user_request = user_request.replace(character, " ")

    user_request = user_request.split(" ")
    for word in user_request:
        if word.lower() in stop_words:
            pass
        else:
            filtered_request.append(word + " ")

    filtered_request = "".join(filtered_request).strip()
    return filtered_request


def google_api_request(user_request, response_dict):
    """Request google places data from the google API and deal with errors
    linked to it then modify value in our response dict"""
    google_places_data = search_query(user_request)

    if google_places_data == "ZERO_RESULTS":
        response_dict["status"] = "zero_results"
    elif google_places_data == "OVER_QUERY_LIMIT":
        response_dict["status"] = "error"
    elif google_places_data == "REQUEST_DENIED":
        response_dict["status"] = "error"
    elif google_places_data == "INVALID_REQUEST":
        response_dict["status"] = "error"
    elif google_places_data == "UNKNOWN_ERROR":
        response_dict["status"] = "error"
    else:
        response_dict["id"] = google_places_data["id"]
        response_dict["name"] = google_places_data["name"]
        response_dict["formatted_address"] = google_places_data[
            "formatted_address"]
        response_dict["lat"] = google_places_data["geometry"]["location"]["lat"]
        response_dict["lng"] = google_places_data["geometry"]["location"]["lng"]


def wikimedia_api_request(response_dict):
    """Request wikipedia data from the wikimedia API and deals with errors
    linked to it, then pass the wikipedia summary of the page requested to
    our response dict if possible"""
    if response_dict["status"] == "zero_results":
        pass
    elif response_dict["status"] == "error":
        pass
    else:
        page_id = search_page_id_query(response_dict["name"])
        if page_id == "error":
            response_dict["status"] = "error"
        elif page_id == "no_info":
            response_dict["status"] = "no_info"
        elif page_id == "zero_results":
            response_dict["status"] = "no_info"
        else:
            response_dict["wiki_summary"] = search_page_summary_query(page_id)
            response_dict["status"] = "ok"


def grandpy_response(response_dict):
    """Add a randomized response to our response dict depending on the status of
    our request"""
    if response_dict["status"] == "zero_results":
        pos = random.randint(0, len(zero_results_responses) - 1)
        response_dict["grandpy_response"] = zero_results_responses[pos]
    elif response_dict["status"] == "error":
        pos = random.randint(0, len(error_responses) - 1)
        response_dict["grandpy_response"] = error_responses[pos]
    elif response_dict["status"] == "no_info":
        pos = random.randint(0, len(no_info_responses) - 1)
        response_dict["grandpy_response"] = no_info_responses[pos]
    else:
        pos = random.randint(0, len(good_responses) - 1)
        response_dict["grandpy_response"] = good_responses[pos]


zero_results_responses = ["Je ne peux pas répondre à ta question, désolé",

                          "J'aimerai pouvoir te répondre mais je suis trop "
                          "fatigué pour le moment",

                          "J'ai peur de ne pas pouvoir t'aider",

                          "Mmmh désolé, je ne peux pas te répondre à ce sujet"]

error_responses = ["Je ne peux pas répondre à ta question, désolé",

                   "Je crois bien que mes informations à ce sujet sont "
                   "éronnées, désolé mais je ne vais pas pouvoir te répondre",

                   "J'aurais aimé te répondre mais je ne tourne pas rond "
                   "aujourd'hui"]

no_info_responses = ["Je sais ou c'est mais je ne connais rien à propos de "
                     "cette endroit",

                     "Je connais l'adresse de ce lieu mais "
                     "je ne pourrais pas t'en dire plus",

                     "Je connais ce lieu, malheuresement je ne me souviens "
                     "pas de son histoire"]

good_responses = ["Oui je connais cette endroit ! Laisse moi t'en parler un "
                  "peu",

                  "Je connais ce lieu ! laisse moi t'en parler"]

stop_words = ["a", "à", "abord", "absolument", "afin", "ah", "ai", "aie",
              "ailleurs",
              "ainsi", "ait", "allaient", "allo", "allons", "allô", "alors",
              "anterieur", "anterieure", "anterieures", "apres", "après", "as",
              "assez", "attendu", "au", "aucun", "aucune", "aujourd",
              "aujourd'hui", "aupres", "auquel", "aura", "auraient", "aurait",
              "auront", "aussi", "autre", "autrefois", "autrement", "autres",
              "autrui", "aux", "auxquelles", "auxquels", "avaient", "avais",
              "avait", "avant", "avec", "avoir", "avons", "ayant", "b", "bah",
              "bas", "basee", "bat", "beau", "beaucoup", "bien", "bigre",
              "boum", "bravo", "brrr", "c", "car", "ce", "ceci", "cela",
              "celle", "celle-ci", "celle-là", "celles", "celles-ci",
              "celles-là", "celui", "celui-ci", "celui-là", "cent", "cependant",
              "certain", "certaine", "certaines", "certains", "certes", "ces",
              "cet", "cette", "ceux", "ceux-ci", "ceux-là", "chacun", "chacune",
              "chaque", "cher", "cherche", "chers", "chez", "chiche", "chut",
              "chère",
              "chères", "ci", "cinq", "cinquantaine", "cinquante",
              "cinquantième", "cinquième", "clac", "clic", "combien", "comme",
              "comment", "comparable", "comparables", "compris", "concernant",
              "contre", "couic", "crac", "d", "da", "dans", "de", "debout",
              "dedans", "dehors", "deja", "delà", "depuis", "dernier",
              "derniere", "derriere", "derrière", "des", "desormais",
              "desquelles", "desquels", "dessous", "dessus", "deux", "deuxième",
              "deuxièmement", "devant", "devers", "devra", "different",
              "differentes", "differents", "différent", "différente",
              "différentes", "différents", "dire", "directe", "directement",
              "dit", "dite", "dits", "divers", "diverse", "diverses", "dix",
              "dix-huit", "dix-neuf", "dix-sept", "dixième", "doit", "doivent",
              "donc", "dont", "douze", "douzième", "dring", "du", "duquel",
              "durant", "dès", "désormais", "e", "effet", "egale", "egalement",
              "egales", "eh", "elle", "elle-même", "elles", "elles-mêmes", "en",
              "encore", "enfin", "entre", "envers", "environ", "es", "est",
              "et", "etant", "etc", "etre", "eu", "euh", "eux", "eux-mêmes",
              "exactement", "excepté", "extenso", "exterieur", "f", "fais",
              "faisaient", "faisant", "fait", "façon", "feront", "fi", "flac",
              "floc", "font", "g", "gens", "h", "ha", "hein", "hem", "hep",
              "hi", "ho", "holà", "hop", "hormis", "hors", "hou", "houp", "hue",
              "hui", "huit", "huitième", "hum", "hurrah", "hé", "hélas", "i",
              "il", "ils", "importe", "j", "je", "jusqu", "jusque", "juste",
              "k", "l", "la", "laisser", "laquelle", "las", "le", "lequel",
              "les", "lesquelles", "lesquels", "leur", "leurs", "longtemps",
              "lors", "lorsque", "lui", "lui-meme", "lui-même", "là", "lès",
              "m", "ma", "maint", "maintenant", "mais", "malgre", "malgré",
              "maximale", "me", "meme", "memes", "merci", "mes", "mien",
              "mienne", "miennes", "miens", "mille", "mince", "minimale", "moi",
              "moi-meme", "moi-même", "moindres", "moins", "mon", "moyennant",
              "multiple", "multiples", "même", "mêmes", "n", "na", "naturel",
              "naturelle", "naturelles", "ne", "neanmoins", "necessaire",
              "necessairement", "neuf", "neuvième", "ni", "nombreuses",
              "nombreux", "non", "nos", "notamment", "notre", "nous",
              "nous-mêmes", "nouveau", "nul", "néanmoins", "nôtre", "nôtres",
              "o", "oh", "ohé", "ollé", "olé", "on", "ont", "onze", "onzième",
              "ore", "ou", "ouf", "ouias", "oust", "ouste", "outre", "ouvert",
              "ouverte", "ouverts", "o|", "où", "p", "paf", "pan", "papy",
              "par",
              "parce", "parfois", "parle", "parlent", "parler", "parmi",
              "parseme", "partant", "particulier", "particulière",
              "particulièrement", "pas", "passé", "pendant", "pense", "permet",
              "personne", "peu", "peut", "peuvent", "peux", "pff", "pfft",
              "pfut", "pif", "pire", "plein", "plouf", "plus", "plusieurs",
              "plutôt", "possessif", "possessifs", "possible", "possibles",
              "pouah", "pour", "pourquoi", "pourrais", "pourrait", "pouvait",
              "prealable", "precisement", "premier", "première", "premièrement",
              "pres", "probable", "probante", "procedant", "proche", "près",
              "psitt", "pu", "puis", "puisque", "pur", "pure", "q", "qu",
              "quand", "quant", "quant-à-soi", "quanta", "quarante", "quatorze",
              "quatre", "quatre-vingt", "quatrième", "quatrièmement", "que",
              "quel", "quelconque", "quelle", "quelles", "quelqu'un", "quelque",
              "quelques", "quels", "qui", "quiconque", "quinze", "quoi",
              "quoique", "r", "rare", "rarement", "rares", "relative",
              "relativement", "remarquable", "rend", "rendre", "restant",
              "reste", "restent", "restrictif", "retour", "revoici", "revoilà",
              "rien", "s", "sa", "sacrebleu", "sait", "sans", "sapristi",
              "sauf", "se", "sein", "seize", "selon", "semblable", "semblaient",
              "semble", "semblent", "sent", "sept", "septième", "sera",
              "seraient", "serait", "seront", "ses", "seul", "seule",
              "seulement", "si", "sien", "sienne", "siennes", "siens", "sinon",
              "six", "sixième", "soi", "soi-même", "soit", "soixante", "son",
              "sont", "sous", "souvent", "specifique", "specifiques",
              "speculatif", "stop", "strictement", "subtiles", "suffisant",
              "suffisante", "suffit", "suis", "suit", "suivant", "suivante",
              "suivantes", "suivants", "suivre", "superpose", "sur", "surtout",
              "t", "ta", "tac", "tant", "tardive", "te", "tel", "telle",
              "tellement", "telles", "tels", "tenant", "tend", "tenir", "tente",
              "tes", "tic", "tien", "tienne", "tiennes", "tiens", "toc", "toi",
              "toi-même", "ton", "touchant", "toujours", "tous", "tout",
              "toute", "toutefois", "toutes", "treize", "trente", "tres",
              "trois", "troisième", "troisièmement", "trop", "très", "tsoin",
              "tsouin", "tu", "té", "u", "un", "une", "unes", "uniformement",
              "unique", "uniques", "uns", "v", "va", "vais", "vas", "vers",
              "via", "vif", "vifs", "vingt", "vivat", "vive", "vives", "vlan",
              "voici", "voilà", "vont", "vos", "votre", "vous", "vous-mêmes",
              "vu", "vé", "vôtre", "vôtres", "w", "x", "y", "z", "zut", "à",
              "â", "ça", "ès", "étaient", "étais", "était", "étant", "été",
              "être", "ô", "grandpy", "bot", "adresse", "salut", "bonjour",
              "hello"]
