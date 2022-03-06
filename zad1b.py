import re

html = "<div><h2>Header</h2> <p>article<b>strong text</b> <a href="">link</a></p></div>"

def usun_html(x):
    nowy = re.sub('<[^>]+>','', x)
    return nowy


print(usun_html(html))