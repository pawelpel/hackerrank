# https://www.hackerrank.com/challenges/ctci-ransom-note/
from collections import Counter


def checkMagazine(magazine, note):
    magazine = Counter(magazine)
    for n in note:
        if n in magazine and magazine[n] > 0:
            magazine[n] -= 1
        else:
            return 'No'
    return 'Yes'
