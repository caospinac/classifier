from abc import ABC, abstractmethod


class Stemmer(ABC):

    @abstractmethod
    def stem(self, word: str) -> str:
        pass
