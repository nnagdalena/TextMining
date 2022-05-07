import pandas as pd
from funkcje import text_tokenizer, top_tokens, top_documents
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

df = pd.read_csv('News_dataset/Fake.csv', usecols=['title', 'text'])


def main():
    vectorizer_count = CountVectorizer(tokenizer=text_tokenizer)
    count_transform = vectorizer_count.fit_transform(df['title'])
    vectorizer_tfid = TfidfVectorizer(tokenizer=text_tokenizer)
    tfid_transform = vectorizer_tfid.fit_transform(df['title'])
    print("Jeśli do vectorizera liczebnościowego przekażemy jedynie jeden dokument, to jakie "
          "wartości będzie miała otrzymana macierz? Albo jakich nie będzie miała?")
    print("\nPuszczajac kod, ktory jest zakomentowany poznamy odpowiedz, ze wyswietla sie same 1, "
          "zadnych 0 nie bedzie")

    most_common_tokens: list = top_tokens(count_transform.toarray().sum(axis=0),
                                        vectorizer_count.get_feature_names_out(), 10)
    print("\n10 najczesciej wystepujacych tokenow")
    print(most_common_tokens)
    most_important_tokens: list = top_tokens(tfid_transform.toarray().sum(axis=0),
                                            vectorizer_tfid.get_feature_names_out(), 10)
    print("\n10 najwazniejszych tokenow")
    print(most_important_tokens)
    most_common_docs: list = top_documents(count_transform.toarray().sum(axis=0), 10)
    print("\n10 najczesciej wystepujacych dokumentow")
    for doc in most_common_docs:
        print(df['title'][doc])


main()
