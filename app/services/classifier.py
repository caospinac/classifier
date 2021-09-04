from app.schemas.classifier import P
from typing import Tuple
from app.helpers.classifier import (
    document_p_values, get_p_value, standardize_values, values,
)


def get_perception(document: str) -> Tuple[str, P]:
    if not document:
        raise Exception('Error: The document is not valid.')

    p = get_p_value('_')
    assert p is not None

    for p_w in document_p_values(document):
        for vj in values:
            p[vj] *= p_w[vj]

    standardize_values(p)

    return max(p, key=p.__getitem__), p
