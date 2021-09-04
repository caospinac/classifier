from nltk import stem

from app.lib.stemmers import Stemmer


class SnowballStemmer(Stemmer):

    def __init__(self) -> None:
        self.__stemmer = stem.SnowballStemmer('english')

    def stem(self, word: str) -> str:
        return self.__stemmer.stem(word)
