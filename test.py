import urllib.parse

f = 'Pandas count values in a column of type list'
ff = urllib.parse.quote_plus(f)
print(ff.replace('+', '_'))