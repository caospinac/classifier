from typing import Callable, Iterable
from elasticsearch import Elasticsearch
from math import sqrt
from nltk.stem import (LancasterStemmer, PorterStemmer, SnowballStemmer,
                       WordNetLemmatizer)
from nltk.corpus import stopwords
from itertools import chain
from string import punctuation
import re
from glob import glob
import csv

import os


# TODO: Refator script

_ = os.getenv

ES_HOST = _('ES_HOST', '0.0.0.0:9200')
ES_INDEX = _('ES_INDEX')

values = {'neg', 'pos'}
stemmer_name = 'snowball'
data: list[list[str]] = []
training_data: dict = {}
all_training_data: list = []
stem: Callable = lambda x: x
noisywords: set = set()


def load_data() -> None:
    # Reading of files

    filenames = glob('training_data/*.csv')
    for file in filenames:
        with open(file) as f:
            file_reader = csv.reader(f)
            next(file_reader, None)
            for row in file_reader:
                if row[0] in values:
                    data.append(row)


def set_stem_function() -> None:
    # Set stemming algorithm
    global stem

    if stemmer_name == 'porter':
        stemmer = PorterStemmer()
        stem = stemmer.stem
    elif stemmer_name == 'lancaster':
        stemmer = LancasterStemmer()
        stem = stemmer.stem
    elif stemmer_name == 'snowball':
        stemmer = SnowballStemmer('english')
        stem = stemmer.stem
    elif stemmer_name == 'lemmatizer':
        stemmer = WordNetLemmatizer()
        stem = lambda w: stemmer.lemmatize(w, pos='v')


def set_noisywords() -> None:
    # Set of words to exclude
    noisywords.update(stopwords.words('english'))
    noisywords.update(punctuation)
    noisywords.update({'__mention__', '__link__'})


def build_training_data() -> None:
    global all_training_data

    for vj in values:
        filtered_data = filter(lambda x: x[0] == vj, data)
        training_data[vj] = list(map(lambda x: x[1], filtered_data))

    all_training_data = list(chain(*training_data.values()))


def get_document_words(*documents: str, unique: bool = True) -> list:
    text = ' '.join(documents).lower()
    text = re.sub(r'((www\.[^\s]+)|(https?://[^\s]+))', '__link__', text)
    text = re.sub(r'@[^\s]+', '__mention__', text)
    text = re.sub(r'#([^\s]+)', r'\1', text)
    words: Iterable = re.findall(r'[^\d\W]{2,}', text)
    words = filter(lambda w: w not in noisywords, words)
    words = map(stem, words)

    return list(set(words)) if unique else list(words)


if __name__ == '__main__':
    load_data()
    build_training_data()
    set_stem_function()
    set_noisywords()

    vocabulary = get_document_words(*all_training_data)

    # Training algorithm
    P = {'_': dict.fromkeys(values)}
    P.update(dict((w, {}) for w in vocabulary))
    for vj in values:
        docs_j = training_data[vj]
        P['_'][vj] = len(docs_j) / len(all_training_data)
        all_text_j = ' '.join(docs_j)
        words_j = get_document_words(all_text_j, unique=False)
        n = len(words_j)
        for w in vocabulary:
            w_occurrences = words_j.count(w)
            P[w][vj] = sqrt(
                (w_occurrences + 1) / (n + len(vocabulary)),
            )

    # Storage/Indexing
    es = Elasticsearch(hosts=ES_HOST)
    base_doc = {
        'stemmer_name': stemmer_name,
    }
    for word, p in P.items():
        total_factor = sum(v for k, v in p.items() if k in values)
        factors = {}
        for vj in values:
            factors[vj] = p[vj] / total_factor

        doc = {
            **base_doc,
            'value': word,
            'p': factors,
        }
        es.index(index=ES_INDEX, id=f'{stemmer_name}_{word}', body=doc)
