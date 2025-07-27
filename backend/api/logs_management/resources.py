from fastapi import (HTTPException, APIRouter, Query)
from datetime import date, time, datetime
from .schemas import Log
from api.opensearch import client_open_search
from .crud import create_index, index_log, set_log_search_query

from typing import Optional

router = APIRouter(tags=["logs_management"])

@router.post("/logs")
async def retrieve_logs(log: Log):
    # validation du log par pydantic
    
    try:
        d = datetime.fromisoformat(log.timestamp)
        formated_date = d.strftime('%Y-%m-%d')
        # index dans OpenSearch : logs-YYYY.MM.DD
        index_name = f'logs-{formated_date}'
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid timestamp")
    
    # si l'index n'existe pas, on le crée
    if not client_open_search.indices.exists(index=index_name):
        create_index(client_open_search, index_name)

    # indexation du log dans OpenSearch
    log_id = index_log(client_open_search, log, index_name)
    if not log_id:
        raise HTTPException(status_code=500, detail="Error while indexing the log")

    # endpoint retourne log inséré avec ID généré par OpenSearch
    return log_id


# Utilisation de Query params optionnels pour GET, car body interdit
@router.get("/logs/search", response_model=list[Log])
async def search_logs(
    q: Optional[str] = Query(None),
    level: Optional[str] = Query(None),
    service: Optional[str] = Query(None)
    ):
    logs = []

    # si il y a des params, alors on fait une recherche spécifique
    # sinon on renvoit les 20 derniers logs
    if q or level or service:
        query = set_log_search_query(q=q, level=level, service=service)
    else:
        query = set_log_search_query(size=20)
    
    response = client_open_search.search(
        body=query,
        index='logs-*'
    )

    if response['hits']['hits']:
        for log in response['hits']['hits']:
            logs.append(log['_source'])

    return logs
