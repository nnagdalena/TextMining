import re

tekst = "Dzisiaj mamy 4 stopnie na plusie, 1 marca 2022 roku"

def usun_liczby(x):
    nowy = re.sub("\d", "", x)
    return nowy


print(usun_liczby(tekst))
