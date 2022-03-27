import re
from nltk.corpus import stopwords

tekst = "<body>The Norwegian :) artist AURORA has always stood out for her strong singularity " \
        "and this fourth ;< album, The Gods We Can Touch, is proof that this is not about to change. " \
        "Since her 2015 single “Runaway,” AURORA :-) has established herself as one of the icons of " \
        "the pop avant-garde, while building an impressive mainstream following. Lorem ipsum. </body>"

stop_words = stopwords.words("english")

def broom(x: str):
    emoji = re.findall('([;:]+[)(><-]+)', x)
    x = re.sub('([;:]+[)(><-]+)', ' ', x)
    x = x.lower()
    x = re.sub(r'\d', ' ', x)
    x = re.sub('<[^>]+>', ' ', x)
    x = re.sub(r'[^\w\s]+', ' ', x)
    x = re.sub(r'\s{2,}', ' ', x)
    x = (x + " ".join(emoji))
    return x


def stopwords(x: str) -> str:
    lista = x.split(' ')
    nowalista: list = []
    [nowalista.append(word) for word in lista if word not in stop_words]
    nowy: str = (" ".join(nowalista))
    return nowy


tekst = broom(tekst)
tekst = stopwords(tekst)
print(tekst)
