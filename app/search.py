import string
from app.api_calls import openstreetmap, wikimedia
from app import app


def search_script(user_request):
    user_request = user_request.split(' ')
    filtered_request = []
    for word in user_request:
        if word in stop_words:
            pass
        elif word in string.punctuation:
            pass
        else:
            filtered_request.append(word + ' ')
    filtered_request = ''.join(filtered_request)

    openstreetmap_data = openstreetmap.search_query(filtered_request)
    wikipedia_page_id = wikimedia.search_page_id_query(filtered_request)
    if (wikipedia_page_id not in (0, -1)):
        wiki_definition = wikimedia.search_page_summary_query(wikipedia_page_id)

    if openstreetmap_data == 0:
        return "no_result"
    elif (wikipedia_page_id == 0) or (wikipedia_page_id == -1):
        return "no_result"
    else:
        response = {"lat": openstreetmap_data['lat'],
                    "lon": openstreetmap_data['lon'],
                    "mapbox_token": app.config['MAPBOX_TOKEN'],
                    "wiki_definition": wiki_definition
                    }

        return response


stop_words = ["a", "abord", "absolument", "afin", "ah", "ai", "aie", "ailleurs",
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
              "chaque", "cher", "chers", "chez", "chiche", "chut", "chère",
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
              "ouverte", "ouverts", "o|", "où", "p", "paf", "pan", "par",
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
              "être", "ô"]
