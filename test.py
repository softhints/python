import urllib.parse

f = '25 Pandas Create A Matplotlib Scatterplot From A Dataframe '
ff = urllib.parse.quote_plus(f)
print(ff.replace('+', '_'))