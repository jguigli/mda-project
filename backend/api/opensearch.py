from fastapi import Depends
from typing import Annotated
from .config import OPENSEARCH_HOST, OPENSEARCH_PORT
from opensearchpy import OpenSearch

client = OpenSearch(
    hosts=[{'host': OPENSEARCH_HOST, 'port': int(OPENSEARCH_PORT)}],
    http_auth=('admin', 'admin'),
    use_ssl=False,
    verify_certs=False
)