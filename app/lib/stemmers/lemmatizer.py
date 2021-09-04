from nltk import stem
from nltk.corpus.reader.wordnet import VERB

from app.lib.stemmers import Stemmer


class WordNetLemmatizer(Stemmer):

    def __init__(self) -> None:
        self.__stemmer = stem.WordNetLemmatizer()

    def stem(self, word: str) -> str:
        return self.__stemmer.lemmatize(word, pos=VERB)
