# https://www.hackerrank.com/challenges/ctci-array-left-rotation/


def rotLeft(a, d):
    d = d % len(a)
    a = a[d:] + a[:d]
    return a


assert rotLeft([1, 2, 3, 4, 5], 4) == [5, 1, 2, 3, 4]
