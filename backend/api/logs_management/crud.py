from .schemas import Log


def create_index(client_open_search, index_name: str):
    index_name = index_name
    index_body = {
        'settings': {
            'index': {
                'number_of_shards': 2
            }
        }
    }
    client_open_search.indices.create(index_name, body=index_body)


def index_log(client_open_search, log: Log, index_name: str):
    log = {
        'timestamp': log['timestamp'],
        'level': log['level'],
        'message': log['message'],
        'service': log['service'],
    }

    response = client_open_search.index(
        index=index_name,
        body=log,
        refresh=True
    )
    # A MODIF
    return response 