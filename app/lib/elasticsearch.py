from typing import Union
from elasticsearch import Elasticsearch

es = Elasticsearch(hosts='es')


def search(index: str, body: dict, one: bool = False) -> Union[list, None]:
    res = es.search(index=index, body=body)

    if one:
        return next((x for x in res['hits']), None)

    return res['hits']
