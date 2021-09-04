from app.lib.const import ES_HOST
from typing import Any, Iterable, Optional
from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=ES_HOST)


def search(index: str, body: dict) -> Iterable:
    res = es.search(index=index, body=body)

    for hit in res['hits']['hits']:
        yield hit['_source']


def search_one(index: str, body: dict) -> Optional[Any]:
    hits = search(index=index, body=body)

    return next((x for x in hits), None)
