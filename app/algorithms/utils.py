from app.lib import stemmers
import re
from string import punctuation
from nltk.corpus import stopwords


noisywords = set(
    stopwords.words('english') +
    list(punctuation) +
    ['__mention__', '__link__'],
)


stemmer = stemmers.create('snowball')


def stem(word: str) -> str:
    return stemmer.stem(word)


def get_document_words(*documents: str, unique: bool = True) -> list[str]:
    text = ' '.join(documents).lower()
    text = re.sub(r'((www\.[^\s]+)|(https?://[^\s]+))', '__link__', text)
    text = re.sub(r'@[^\s]+', '__mention__', text)
    text = re.sub(r'#([^\s]+)', r'\1', text)
    words = re.findall(r'[^\d\W]{2,}', text)
    words_filter = filter(lambda w: w not in noisywords, words)
    words_it = map(stem, words_filter)

    return list(set(words_it)) if unique else list(words_it)
