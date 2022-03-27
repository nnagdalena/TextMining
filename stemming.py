from nltk.stem import PorterStemmer

tekst = "The Norwegian artist AURORA has always stood out for her strong singularity " \
        "and this fourth album, The Gods We Can Touch, is proof that this is not about to change. " \
        "Since her 2015 single “Runaway,” AURORA has established herself as one of the icons of " \
        "the pop avant-garde, while building an impressive mainstream following."

lista: list = tekst.split(" ")


def stemming(lista: list):
    porter = PorterStemmer()
    return [porter.stem(x) for x in lista]


lista = stemming(lista)
print(lista)
