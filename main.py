import pandas as pd
from funkcje import text_tokenizer, top_tokens, top_documents, tabelka, wykres, plot_table_most_important
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import seaborn as sns

fake = pd.read_csv('Fake.csv', usecols=['title', 'text'])
true = pd.read_csv('True.csv', usecols=['title', 'text'])
joined = pd.concat([fake, true],ignore_index=True)


def main():
    vectorizer_count = CountVectorizer(tokenizer=text_tokenizer)
    true_count = vectorizer_count.fit_transform(true['title'])
    fake_count = vectorizer_count.fit_transform(fake['title'])

    vectorizer_tfid = TfidfVectorizer(tokenizer=text_tokenizer)
    true_tfid = vectorizer_tfid.fit_transform(true['text'])

    vectorizer_binary = CountVectorizer(tokenizer=text_tokenizer, binary=True)
    binary = vectorizer_binary.fit_transform(joined['title'])

    top_fake_count = top_tokens(fake_count.toarray().sum(axis=0), vectorizer_count.get_feature_names_out(), 15)
    top_true_count = top_tokens(true_count.toarray().sum(axis=0), vectorizer_count.get_feature_names_out(), 15)
    top_true_tfid = top_tokens(true_tfid.toarray().sum(axis=0), vectorizer_tfid.get_feature_names_out(), 15)
    top_binary = top_tokens(binary.toarray().sum(axis=0), vectorizer_binary.get_feature_names_out(), 15)

    print(wykres(top_fake_count, "Tokeny występujące w tytułach fałszywych wiadomości"))
    print(tabelka(top_fake_count, "Tokeny występujące w tytułach fałszywych wiadomości"))

    print(wykres(top_true_count, "Tokeny występujące w tytułach prawdziwych wiadomości"))
    print(tabelka(top_true_count, "Tokeny występujące w tytułach prawdziwych wiadomości"))

    print(wykres(top_true_tfid, "Kluczowe tokeny prawdziwych wiadomości na podstawie miary TF-IDF"))
    print(tabelka(top_true_tfid, "Kluczowe tokeny prawdziwych wiadomości na podstawie miary TF-IDF"))

    print(wykres(top_binary,  "Crucial tokens based on binary weight"))
    print(tabelka(top_binary,  "Crucial tokens based on binary weight"))


main()
