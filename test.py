import urllib.parse

f = '20. Pandas - value_counts - multiple columns, all columns and bad data'
ff = urllib.parse.quote_plus(f)
print(ff.replace('+', '_'))