from bebechy import text_tokenizer, vectorizer

import pandas as pd

#fake = pd.read_csv('Fake.csv')
#tekst2 = " ".join(x for x in fake.title)


tekst = "<body>The Norwegian :) artist AURORA has always stood out for her strong singularity " \
        "and this fourth ;< album, The Gods We Can Touch, is proof that this is not about to change. " \
        "Since her 2015 single “Runaway,” AURORA :-) has established herself as one of the icons of " \
        "the pop avant-garde, while building an impressive mainstream following.</body>"

tekst = text_tokenizer(tekst)

#print(tekst2)
#print(len(tekst2))

X_transform = vectorizer.fit_transform(tekst)
print(X_transform.shape)
print(X_transform)
print(X_transform.toarray())