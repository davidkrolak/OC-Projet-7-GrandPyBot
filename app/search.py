import string
import random
from app.api_calls.wikimedia import search_page_summary_query, \
    search_page_id_query
from app.api_calls.google_places import search_query


def search_script(user_request):
    user_request = request_parser(user_request)

    # Create a dict who will be send back to the front-end
    response = {"id": None,
                "name": None,
                "formatted_address": None,
                "lat": None,
                "lng": None,
                "wiki_summary": None,
                "grandpy_response": None,
                "status": None
                }

    # This block manage the request made to the google places API
    google_places_data = search_query(user_request)
    if google_places_data == "ZERO_RESULTS":
        response["status"] = "zero_results"
    elif google_places_data == "OVER_QUERY_LIMIT":
        response["status"] = "error"
    elif google_places_data == "REQUEST_DENIED":
        response["status"] = "error"
    elif google_places_data == "INVALID_REQUEST":
        response["status"] = "error"
    elif google_places_data == "UNKNOWN_ERROR":
        response["status"] = "error"
    else:
        response["id"] = google_places_data["id"]
        response["name"] = google_places_data["name"]
        response["formatted_address"] = google_places_data["formatted_address"]
        response["lat"] = google_places_data["geometry"]["location"]["lat"]
        response["lng"] = google_places_data["geometry"]["location"]["lng"]

    # This block search for a wikipedia page and return the summary
    if response["status"] == "zero_results":
        pass
    elif response["status"] == "error":
        pass
    else:
        page_id = search_page_id_query(response["name"])
        if page_id == "error":
            response["status"] = "error"
        elif page_id == "no_info":
            response["status"] = "no_info"
        elif page_id == "zero_results":
            response["status"] = "no_info"
        else:
            response["wiki_summary"] = search_page_summary_query(page_id)
            response["status"] = "ok"

    return grandpy_response(response)


def request_parser(user_request):
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


def grandpy_response(response_dict):
    if response_dict["status"] == "zero_results":
        pass
    elif response_dict["status"] == "error":
        pass
    elif response_dict["status"] == "no_info":
        pass
    else:
        pass
    return response_dict


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
