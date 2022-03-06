import re

hasz = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " \
       "Sed #texting eget mattis sem. Mauris #frasista egestas erat #tweetext quam, \n" \
       "ut faucibus eros #frasier congue et. In blandit, mi eu porta lobortis, tortor nisl facilisis leo, " \
       "at tristique #frasistas augue risus eu risus. "


def pokaz_hasz(x):
    nowy = re.findall('#', x)
    return nowy

print(pokaz_hasz(hasz))
