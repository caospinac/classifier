from app.algorithms.utils import get_document_words
from typing import Iterable, Optional
from app.schemas.classifier import P
from app.lib.elasticsearch import search, search_one


values = ['neg', 'pos']


def get_p_value(word: str) -> Optional[P]:
    payload = {
        'query': {
            'match': {
                'value.keyword': word,
            },
        },
    }
    result = search_one('words', payload)
    if result is None:
        return None

    return result['p']


def document_p_values(doc: str) -> Iterable[P]:
    document_words = get_document_words(doc)
    payload = {
        'query': {
            'terms': {
                'value.keyword': document_words,
            },
        },
    }
    for hit in search('words', payload):
        yield hit['p']


def standardize_values(p: P) -> None:
    total_factor = sum(p.values())
    for vj in values:
        p[vj] /= 1.0 * total_factor
