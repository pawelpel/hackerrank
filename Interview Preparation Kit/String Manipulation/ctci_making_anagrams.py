# https://www.hackerrank.com/challenges/ctci-making-anagrams/
from collections import Counter


def makeAnagram(a, b):
    a = Counter(a)
    b = Counter(b)
    return sum((a-b).values()) + sum((b-a).values())
