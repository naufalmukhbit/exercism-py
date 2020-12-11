from itertools import compress
def find_anagrams(word, candidates):
    letters = sorted(word.lower())
    anagrams = [sorted(i.lower()) == letters and i.lower() != word.lower() for i in candidates]
    return list(compress(candidates, anagrams))
