import re
from collections import Counter

def count_words(sentence):
    words = re.findall(r'([a-z0-9]+\'[a-z0-9]{1,2}|[a-z0-9]+)', sentence.lower())
    wordcount = Counter()
    for item in words:
        wordcount[item] += 1
    return dict(wordcount)
