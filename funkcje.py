import re
import numpy as np
import matplotlib.pyplot as plt
from nltk import PorterStemmer
from nltk.corpus import stopwords
from prettytable import PrettyTable

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


def top_tokens(list_of_tokens, token_words, how_many) -> dict:
    top_words = []
    top_counts = []
    top_dict = {}
    for i in range(how_many):
        token_index = np.argmax(list_of_tokens)
        top_words.append(token_words[token_index])
        top_counts.append(list_of_tokens[token_index])
        list_of_tokens[token_index] = 0
    for key, value in zip(top_words, top_counts):
        top_dict[key] = value
    return top_dict


def top_documents(list_of_documents, how_many) -> list:
    list_of_documents = list_of_documents
    top_list = []
    for i in range(how_many):
        token_index = np.argmax(list_of_documents, 0)
        top_list.append(token_index)
        list_of_documents[token_index] = 0
    return top_list


def wykres(top, title):
    slowa = list(top.keys())[::-1]
    cnt = list(top.values())[::-1]
    plt.subplots(figsize=(11, 5))
    y_pos = np.arange(len(slowa))
    plt.barh(y_pos, cnt)
    plt.yticks(y_pos, slowa)
    plt.ylabel("Term")
    plt.xlabel("Weight")
    plt.title(title)
    plt.show()

def tabelka(top, title):
    slowa = list(top.keys())[::-1]
    cnt = list(top.values())[::-1]
    pretty_table = PrettyTable()
    pretty_table.title = title
    pretty_table.add_column("Term", slowa[::-1])
    pretty_table.add_column("Weight", cnt[::-1])
    return pretty_table
