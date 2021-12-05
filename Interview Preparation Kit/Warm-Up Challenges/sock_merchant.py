# https://www.hackerrank.com/challenges/sock-merchant/
from collections import Counter


def sockMerchant(n, ar):
    return sum(v // 2 for _, v in Counter(ar).items())
