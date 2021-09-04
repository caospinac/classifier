from nltk import stem

from app.lib.stemmers import Stemmer


class PorterStemmer(Stemmer):

    def __init__(self) -> None:
        self.__stemmer = stem.PorterStemmer()

    def stem(self, word: str) -> str:
        return self.__stemmer.stem(word)
