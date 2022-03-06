import re
import string

tekst = "Lorem ipsum dolor sit amet, consectetur; adipiscing elit. Sed eget mattis sem. Mauris egestas erat quam, " \
       "ut faucibus eros congue et. \n" \
       " In blandit, mi eu porta; lobortis, tortor nisl facilisis leo, at tristique augue " \
       "risus eu risus. "

def usun_inter(x):
       nowy = re.sub('[^\w\s]', '', x)
       return nowy

print(usun_inter(tekst))