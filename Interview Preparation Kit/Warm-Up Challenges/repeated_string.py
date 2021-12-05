# https://www.hackerrank.com/challenges/repeated-string/

def repeatedString(s, n):
    a_in_s = sum(l == 'a' for l in s)
    return n // len(s) * a_in_s + sum(l == 'a' for l in s[:n % len(s)])
