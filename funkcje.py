import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


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