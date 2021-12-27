# https://www.hackerrank.com/challenges/two-strings/

def twoStrings(s1, s2):
    return 'YES' if len(set(s1).intersection(set(s2))) else 'NO'
