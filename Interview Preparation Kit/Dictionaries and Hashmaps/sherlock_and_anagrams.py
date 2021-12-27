# https://www.hackerrank.com/challenges/sherlock-and-anagrams/
import collections


def sherlockAndAnagrams(s):
    from collections import Counter
    counter = 0
    window_size = 1
    while window_size < len(s):
        pairs = []
        for i in range(len(s)-window_size+1):
            x = ''.join(sorted(s[i:window_size+i]))
            pairs.append(x)
        for v in Counter(pairs).values():
            counter += v*(v-1)//2
        window_size += 1
    return counter


assert sherlockAndAnagrams('ifailuhkqq') == 3
assert sherlockAndAnagrams('kkkk') == 10
