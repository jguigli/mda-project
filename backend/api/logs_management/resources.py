from fastapi import (Depends, Response, HTTPException, APIRouter)
from datetime import date, time, datetime
from .schemas import Log, SearchedLogs
from api.opensearch import client_open_search
from .crud import create_index, index_log

router = APIRouter(tags=["logs_management"])

@router.post("/logs")
def retrieve_logs(log: Log):
    # validation du log par pydantic
    # index dans OpenSearch : logs-YYYY.MM.DD
    try:
        d = datetime.date.fromisoformat(log['timestamp'])
        formated_date = d.strftime('%Y-%m-%d')
        index_name = f'logs-{formated_date}'
    except Exception:
        return HTTPException(status_code=400, detail="Invalid timestamp")
    
    if not client_open_search.indices.exists(index=index_name):
        create_index(client_open_search, index_name)

    # on garde le timestamp du log dans OpenSearch au format ISO 8601
    log_indexed = index_log(client_open_search, log, index_name)
    if not log_indexed:
        return HTTPException(status_code=404, detail="Invalid timestamp")

    # endpoint retourne log inséré avec ID généré par OpenSearch
    return log_indexed


@router.get("/logs/search", response_model=list[Log])
def search_logs(searchedLogs: SearchedLogs):
    # requete de recherche pertinente a OpenSearch (combinaison de match -> recherche textuelle / combinaison de term -> filtres)
    # q = 'Harper Lee'
    # query = {
    #     'size': 5,
    #     'query': {
    #         'multi_match': {
    #             'query': q,
    #             'fields': ['title^2', 'author']
    #         }
    #     }
    # }
    # response = client.search(
    #     body=query,
    #     index='python-example-index'
    # )
    # print('Search results:', response)

    # endpoint retourne une liste de logs correspondant aux criteres de recherche, triés par timestamp décroissant
    return