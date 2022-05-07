import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

stop_words = stopwords.words("english")

def broom(x: str):
    x = re.sub('([;:]+[)(><-]+)', ' ', x)
    x = x.lower()
    x = re.sub(r'\d', ' ', x)
    x = re.sub('<[^>]+>', ' ', x)
    x = re.sub(r'[^\w\s]+', ' ', x)
    x = re.sub(r'\s{2,}', ' ', x)
    return x


def usun_stopwords(x: str) -> list:
    lista = x.split(' ')
    nowalista: list = []
    [nowalista.append(word) for word in lista if word not in stop_words]
    return nowalista


def stemming(lista: list):
    porter = PorterStemmer()
    return [porter.stem(x) for x in lista]


def text_tokenizer(x: str) -> list:
    x = broom(x)
    x = usun_stopwords(x)
    x = stemming(x)
    [x.remove(word) for word in x if len(word) < 4]
    return x


vectorizer = TfidfVectorizer(tokenizer=text_tokenizer)
