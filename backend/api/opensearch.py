from .config import OPENSEARCH_HOST, OPENSEARCH_PORT, OPENSEARCH_LOGIN, OPENSEARCH_PASSWORD
from opensearchpy import OpenSearch

client = OpenSearch(
    hosts=[{'host': OPENSEARCH_HOST, 'port': int(OPENSEARCH_PORT)}],
    http_auth=(OPENSEARCH_LOGIN, OPENSEARCH_PASSWORD),
    use_ssl=False,
    verify_certs=False
)