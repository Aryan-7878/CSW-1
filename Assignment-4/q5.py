import re

def match_cvc(word):
    # starts with c
    # vowel next: [aeiou]
    # consonant next: any letter that is NOT a vowel
    pattern = r'^c[aeiou][^aeiou]$'
    return bool(re.match(pattern, word))
tests = ["cat", "cit", "cot", "cut", "caa", "c9t", "cbt"]

for w in tests:
    print(w, "-", match_cvc(w))