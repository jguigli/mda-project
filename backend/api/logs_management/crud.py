from .schemas import Log


def create_index(client_open_search, index_name: str):
    # shard: partie physique d'un index stockée sur un noeud
    # objectif: paralléliser le traitement / répartir la charge sur plusieurs noeuds
    index_body = {
        'settings': {
            'index': {
                'number_of_shards': 2
            }
        }
    }
    
    client_open_search.indices.create(index_name, body=index_body)


def index_log(client_open_search, log: Log, index_name: str):
    # on garde le timestamp du log dans OpenSearch au format ISO 8601
    log = {
        'timestamp': log.timestamp,
        'level': log.level,
        'message': log.message,
        'service': log.service,
    }

    response = client_open_search.index(
        index=index_name,
        body=log,
        refresh=True
    )

    return response['_id']

# construction de la requete de recherche a OpenSearch (combinaison de match -> recherche textuelle / combinaison de term -> filtres)
def set_log_search_query(q=None, level=None, service=None, size=500):
    filters = []
    musts = []

    # création d'une boolean query afin de combiner la recherche full-text et les filtres
    if q:
        musts.append({ 'match': { 'message': q }})
    if level:
        filters.append({ 'term': { 'level': level }})
    if service:
        filters.append({ 'term': { 'service': service }})
    
    # must: agit comme un 'AND', contribue au score (pertinence de recherche)
    # filter: agit comme un 'AND', le score est ignoré, évaluation true ou false
    # sort: tri les resultats par timestamp décroissant (desc)
    query = {
        'query': {
            'bool': {
                'must': musts,
                'filter': filters,
            }
        },
        'sort': [
            { 'timestamp': 'desc' }
        ],
        'size' : size,
    }

    return query