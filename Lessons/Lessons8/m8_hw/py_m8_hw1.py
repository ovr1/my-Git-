from collections import Counter
f_name = 'm8-sirotlivo.txt'

with open(f_name, encoding='utf-8') as fp:
    contents = fp.read()
    words = contents.lower()
    c = Counter(words.split())
    print(c.most_common())
