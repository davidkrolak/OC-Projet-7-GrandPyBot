import string
import random

from flask import render_template
from app.api_calls import wikimedia, google_places


class Research:
    """"""

    def __init__(self, user_input):
        self.user_request = user_input.lower()
        self.name = None
        self.formatted_address = None
        self.lat = None
        self.lng = None
        self.wiki_page_id = None
        self.wiki_summary = None
        self.wiki_url = None
        self.grandpy_response = None
        self.status = None

        # Bot custom responses
        self._zero_results_responses = [
            "Je ne peux pas répondre à ta question, désolé",
            "J'aimerai pouvoir te répondre mais je suis trop fatigué pour le moment",
            "J'ai peur de ne pas pouvoir t'aider",
            "Mmmh désolé, je ne peux pas te répondre à ce sujet"
        ]
        self._error_responses = [
            "Je ne peux pas répondre à ta question, désolé",
            "Je crois bien que mes informations à ce sujet sont éronnées, désolé mais je ne vais pas pouvoir te répondre",
            "J'aurais aimé te répondre mais je ne tourne pas rond aujourd'hui"
        ]
        self._no_info_responses = [
            "Je sais ou c'est mais je ne connais rien à propos de cette endroit",
            "Je connais l'adresse de ce lieu mais je ne pourrais pas t'en dire plus",
            "Je connais ce lieu, malheuresement je ne me souviens pas de son histoire"
        ]
        self._good_responses = [
            "Je connais cette endroit ! Laisse moi t'en parler un peu",
            "Je connais ce lieu ! Laisse moi t'en parler"
        ]

        # Stop words list for the parser
        self._stop_words = ["a", "à", "abord", "absolument", "afin", "ah", "ai",
                            "aie",
                            "ailleurs",
                            "ainsi", "ait", "allaient", "allo", "allons",
                            "allô",
                            "alors",
                            "anterieur", "anterieure", "anterieures", "apres",
                            "après", "as",
                            "assez", "attendu", "au", "aucun", "aucune",
                            "aujourd",
                            "aujourd'hui", "aupres", "auquel", "aura",
                            "auraient", "aurait",
                            "auront", "aussi", "autre", "autrefois",
                            "autrement",
                            "autres",
                            "autrui", "aux", "auxquelles", "auxquels",
                            "avaient",
                            "avais",
                            "avait", "avant", "avec", "avoir", "avons", "ayant",
                            "b", "bah",
                            "bas", "basee", "bat", "beau", "beaucoup", "bien",
                            "bigre",
                            "boum", "bravo", "brrr", "c", "car", "ce", "ceci",
                            "cela",
                            "celle", "celle-ci", "celle-là", "celles",
                            "celles-ci",
                            "celles-là", "celui", "celui-ci", "celui-là",
                            "cent",
                            "cependant",
                            "certain", "certaine", "certaines", "certains",
                            "certes", "ces",
                            "cet", "cette", "ceux", "ceux-ci", "ceux-là",
                            "chacun", "chacune",
                            "chaque", "cher", "cherche", "chers", "chez",
                            "chiche", "chut",
                            "chère",
                            "chères", "ci", "cinq", "cinquantaine", "cinquante",
                            "cinquantième", "cinquième", "clac", "clic",
                            "combien", "comme",
                            "comment", "comparable", "comparables", "compris",
                            "concernant",
                            "contre", "couic", "crac", "d", "da", "dans", "de",
                            "debout",
                            "dedans", "dehors", "deja", "delà", "depuis",
                            "dernier",
                            "derniere", "derriere", "derrière", "des",
                            "desormais",
                            "desquelles", "desquels", "dessous", "dessus",
                            "deux", "deuxième",
                            "deuxièmement", "devant", "devers", "devra",
                            "different",
                            "differentes", "differents", "différent",
                            "différente",
                            "différentes", "différents", "dire", "directe",
                            "directement",
                            "dit", "dite", "dits", "divers", "diverse",
                            "diverses", "dix",
                            "dix-huit", "dix-neuf", "dix-sept", "dixième",
                            "doit", "doivent",
                            "donc", "dont", "douze", "douzième", "dring", "du",
                            "duquel",
                            "durant", "dès", "désormais", "e", "effet", "egale",
                            "egalement",
                            "egales", "eh", "elle", "elle-même", "elles",
                            "elles-mêmes", "en",
                            "encore", "enfin", "entre", "envers", "environ",
                            "es", "est",
                            "et", "etant", "etc", "etre", "eu", "euh", "eux",
                            "eux-mêmes",
                            "exactement", "excepté", "extenso", "exterieur",
                            "f",
                            "fais",
                            "faisaient", "faisant", "fait", "façon", "feront",
                            "fi", "flac",
                            "floc", "font", "g", "gens", "h", "ha", "hein",
                            "hem", "hep",
                            "hi", "ho", "holà", "hop", "hormis", "hors", "hou",
                            "houp", "hue",
                            "hui", "huit", "huitième", "hum", "hurrah", "hé",
                            "hélas", "i",
                            "il", "ils", "importe", "j", "je", "jusqu",
                            "jusque",
                            "juste",
                            "k", "l", "la", "laisser", "laquelle", "las", "le",
                            "lequel",
                            "les", "lesquelles", "lesquels", "leur", "leurs",
                            "longtemps",
                            "lors", "lorsque", "lui", "lui-meme", "lui-même",
                            "là", "lès",
                            "m", "ma", "maint", "maintenant", "mais", "malgre",
                            "malgré",
                            "maximale", "me", "meme", "memes", "merci", "mes",
                            "mien",
                            "mienne", "miennes", "miens", "mille", "mince",
                            "minimale", "moi",
                            "moi-meme", "moi-même", "moindres", "moins", "mon",
                            "moyennant",
                            "multiple", "multiples", "même", "mêmes", "n", "na",
                            "naturel",
                            "naturelle", "naturelles", "ne", "neanmoins",
                            "necessaire",
                            "necessairement", "neuf", "neuvième", "ni",
                            "nombreuses",
                            "nombreux", "non", "nos", "notamment", "notre",
                            "nous",
                            "nous-mêmes", "nouveau", "nul", "néanmoins",
                            "nôtre",
                            "nôtres",
                            "o", "oh", "ohé", "ollé", "olé", "on", "ont",
                            "onze",
                            "onzième",
                            "ore", "ou", "ouf", "ouias", "oust", "ouste",
                            "outre", "ouvert",
                            "ouverte", "ouverts", "o|", "où", "p", "paf", "pan",
                            "papy",
                            "par",
                            "parce", "parfois", "parle", "parlent", "parler",
                            "parmi",
                            "parseme", "partant", "particulier", "particulière",
                            "particulièrement", "pas", "passé", "pendant",
                            "pense", "permet",
                            "personne", "peu", "peut", "peuvent", "peux", "pff",
                            "pfft",
                            "pfut", "pif", "pire", "plein", "plouf", "plus",
                            "plusieurs",
                            "plutôt", "possessif", "possessifs", "possible",
                            "possibles",
                            "pouah", "pour", "pourquoi", "pourrais", "pourrait",
                            "pouvait",
                            "prealable", "precisement", "premier", "première",
                            "premièrement",
                            "pres", "probable", "probante", "procedant",
                            "proche", "près",
                            "psitt", "pu", "puis", "puisque", "pur", "pure",
                            "q",
                            "qu",
                            "quand", "quant", "quant-à-soi", "quanta",
                            "quarante", "quatorze",
                            "quatre", "quatre-vingt", "quatrième",
                            "quatrièmement", "que",
                            "quel", "quelconque", "quelle", "quelles",
                            "quelqu'un", "quelque",
                            "quelques", "quels", "qui", "quiconque", "quinze",
                            "quoi",
                            "quoique", "r", "rare", "rarement", "rares",
                            "relative",
                            "relativement", "remarquable", "rend", "rendre",
                            "restant",
                            "reste", "restent", "restrictif", "retour",
                            "revoici", "revoilà",
                            "rien", "s", "sa", "sacrebleu", "sait", "sans",
                            "sapristi",
                            "sauf", "se", "sein", "seize", "selon", "semblable",
                            "semblaient",
                            "semble", "semblent", "sent", "sept", "septième",
                            "sera",
                            "seraient", "serait", "seront", "ses", "seul",
                            "seule",
                            "seulement", "si", "sien", "sienne", "siennes",
                            "siens", "sinon",
                            "six", "sixième", "soi", "soi-même", "soit",
                            "soixante", "son",
                            "sont", "sous", "souvent", "specifique",
                            "specifiques",
                            "speculatif", "stop", "strictement", "subtiles",
                            "suffisant",
                            "suffisante", "suffit", "suis", "suit", "suivant",
                            "suivante",
                            "suivantes", "suivants", "suivre", "superpose",
                            "sur", "surtout",
                            "t", "ta", "tac", "tant", "tardive", "te", "tel",
                            "telle",
                            "tellement", "telles", "tels", "tenant", "tend",
                            "tenir", "tente",
                            "tes", "tic", "tien", "tienne", "tiennes", "tiens",
                            "toc", "toi",
                            "toi-même", "ton", "touchant", "toujours", "tous",
                            "tout",
                            "toute", "toutefois", "toutes", "treize", "trente",
                            "tres",
                            "trois", "troisième", "troisièmement", "trop",
                            "très", "tsoin",
                            "tsouin", "tu", "té", "u", "un", "une", "unes",
                            "uniformement",
                            "unique", "uniques", "uns", "v", "va", "vais",
                            "vas",
                            "vers",
                            "via", "vif", "vifs", "vingt", "vivat", "vive",
                            "vives", "vlan",
                            "voici", "voilà", "vont", "vos", "votre", "vous",
                            "vous-mêmes",
                            "vu", "vé", "vôtre", "vôtres", "w", "x", "y", "z",
                            "zut", "à",
                            "â", "ça", "ès", "étaient", "étais", "était",
                            "étant", "été",
                            "être", "ô", "grandpy", "bot", "adresse", "salut",
                            "bonjour",
                            "hello"]


    def _request_parser(self):
        """Parse the user request in multiple words, then check if those one are
        punctuation or not and finally delete the words in the request who matchs
        our stop words list"""

        for character in string.punctuation:
            if character in self.user_request:
                self.user_request = self.user_request.replace(character, " ")

        filtered_request = []
        self.user_request = self.user_request.split(" ")
        for word in self.user_request:
            if word in self._stop_words:
                pass
            else:
                filtered_request.append(word + " ")

        filtered_request = "".join(filtered_request).strip().lower()
        self.user_request = filtered_request

    def _google_places_request(self):
        """Request google places data from the google API and deal with errors
        linked to it then modify value in our response dict"""

        google_places_data = google_places.search_places(self.user_request)

        if google_places_data == "ZERO_RESULTS":
            self.status = "google_zero_results"
        elif google_places_data == "OVER_QUERY_LIMIT":
            self.status = "google_over_query_limit"
        elif google_places_data == "REQUEST_DENIED":
            self.status = "google_request_denied"
        elif google_places_data == "INVALID_REQUEST":
            self.status = "google_invalid_request"
        elif google_places_data == "UNKNOWN_ERROR":
            self.status = "google_unknown_error"
        else:
            self.name = google_places_data['name']
            self.formatted_address = google_places_data['formatted_address']
            self.lat = google_places_data['geometry']['location']['lat']
            self.lng = google_places_data['geometry']['location']['lng']
            self.status = "google_ok"

    def _wikimedia_page_id_request(self):
        """Request wikipedia data from the wikimedia API and deals with errors
        linked to it, then pass the wikipedia summary of the page requested to
        our response dict if possible"""

        # Check status of the google places research
        if self.status != "google_ok":
            pass
        else:
            search_page_id_response = wikimedia.search_page_id(self.name)

            if search_page_id_response == "wikimedia_error_500":
                self.status = "wikimedia_error_500"
            elif search_page_id_response == "wikimedia_error_504":
                self.status = "wikimedia_error_504"
            elif search_page_id_response == "wikimedia_error_400":
                self.status = "wikimedia_error_400"
            elif search_page_id_response == "wikimedia_error_404":
                self.status = "wikimedia_error_404"
            elif search_page_id_response == "error":
                self.status = "wikimedia_api_error"
            elif search_page_id_response == "zero_results":
                self.status = "wikimedia_zero_results"
            else:
                self.wiki_page_id = search_page_id_response
                self.status = 'wikipedia_page_id_ok'

    def _wikimedia_page_summary_request(self):
        """"""

        if self.status != "wikipedia_page_id_ok":
            pass
        else:
            search_page_summary_response = wikimedia.search_page_summary(
                self.wiki_page_id)

            if search_page_summary_response == "wikimedia_error_500":
                self.status = "wikimedia_error_500"
            elif search_page_summary_response == "wikimedia_error_504":
                self.status = "wikimedia_error_504"
            elif search_page_summary_response == "wikimedia_error_400":
                self.status = "wikimedia_error_400"
            elif search_page_summary_response == "wikimedia_error_404":
                self.status = "wikimedia_error_404"
            elif search_page_summary_response == "no_summary":
                self.status = "wikimedia_zero_results"
            else:
                self.wiki_summary = search_page_summary_response
                self.status = "wikipedia_page_summary_ok"

    def _wikimedia_page_url_request(self):
        """"""

        if self.status != "wikipedia_page_summary_ok":
            pass
        else:
            search_page_url_response = wikimedia.search_page_url(
                    self.wiki_page_id)

            if search_page_url_response == "wikimedia_error_500":
                self.status = "wikimedia_error_500"
            elif search_page_url_response == "wikimedia_error_504":
                self.status = "wikimedia_error_504"
            elif search_page_url_response == "wikimedia_error_400":
                self.status = "wikimedia_error_400"
            elif search_page_url_response == "wikimedia_error_404":
                self.status = "wikimedia_error_404"
            elif search_page_url_response == "no_url":
                self.status = "wikimedia_no_page_url"
            else:
                self.wiki_url = search_page_url_response
                self.status = "wikipedia_page_url_ok"

    def _grandpy_response(self):
        """Add a randomized response to our response dict depending on the
        status of our request"""

        if self.status == "google_zero_results":
            self.grandpy_response = random.choice(self._zero_results_responses)
        elif self.status == "google_error":
            self.grandpy_response = random.choice(self._error_responses)
        elif self.status == "wikimedia_error":
            self.grandpy_response = random.choice(self._no_info_responses)
        elif self.status == "wikimedia_no_info":
            self.grandpy_response = random.choice(self._no_info_responses)
        elif self.status == "wikimedia_zero_results":
            self.grandpy_response = random.choice(self._no_info_responses)
        else:
            self.grandpy_response = random.choice(self._good_responses)

    def _render_messages(self):
        """"""

    def render(self):
        self._request_parser()
        self._google_places_request()
        self._wikimedia_page_id_request()
        self._wikimedia_page_summary_request()
        self._wikimedia_page_url_request()
        self._grandpy_response()