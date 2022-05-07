import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
from funkcje import broom, usun_stopwords, stemming, stop_words

fake = pd.read_csv('News_dataset/Fake.csv')
true = pd.read_csv('News_dataset/True.csv')

list = []

fake_title = " ".join(x for x in fake.title)
list.append(fake_title)
true_title = " ".join(x for x in true.title)
list.append(true_title)
# fake_text = " ".join(x for x in fake.text)
# list.append(fake_text)
# true_text = " ".join(x for x in true.text)
# list.append(true_text)

for ziomek in list:
    ziomek = broom(ziomek)
    ziomek = usun_stopwords(ziomek)
    ziomek = stemming(ziomek)
    ziomek = " ".join(ziomek)

fake_title_wc = WordCloud(stopwords=stop_words, background_color="white").generate(fake_title)
true_title_wc = WordCloud(stopwords=stop_words, background_color="white").generate(true_title)
# fake_text_wc = WordCloud(stopwords=stop_words, background_color="white").generate(fake_title)
# true_text_wc = WordCloud(stopwords=stop_words, background_color="white").generate(true_title)

lista_wc = [fake_title_wc, true_title_wc]

for wc in lista_wc:
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()

