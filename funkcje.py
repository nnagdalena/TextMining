import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import numpy as np

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


def top_tokens(list_of_tokens, token_words, how_many) -> list:
    list_of_tokens = list_of_tokens
    top_list = []
    for i in range(how_many):
        token_index = np.argmax(list_of_tokens)
        top_list.append(token_words[token_index])
        list_of_tokens[token_index] = 0
    return top_list


def top_documents(list_of_documents, how_many) -> list:
    list_of_documents = list_of_documents
    top_list = []
    for i in range(how_many):
        token_index = np.argmax(list_of_documents, 0)
        top_list.append(token_index)
        list_of_documents[token_index] = 0
    return top_list