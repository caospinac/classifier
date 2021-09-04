from abc import ABC, abstractmethod
from .stemmer import Stemmer
from .lemmatizer import WordNetLemmatizer
from .snowball import SnowballStemmer
from .lancaster import LancasterStemmer
from .porter import PorterStemmer


def create(name: str) -> Stemmer:
    if name == 'porter':
        return PorterStemmer()
    elif name == 'lancaster':
        return LancasterStemmer()
    elif name == 'snowball':
        return SnowballStemmer()
    elif name == 'lemmatizer':
        return WordNetLemmatizer()

    assert 0, "Bad stemmer creation: " + name
