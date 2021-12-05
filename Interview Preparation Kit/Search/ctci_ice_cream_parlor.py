# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/
from collections import Counter


def whatFlavors(cost, money):
    cost_counter = Counter(cost)
    for c in sorted(x for x in cost_counter.keys() if x < money):
        if money - c in cost_counter:
            if c == money - c and cost_counter[c] < 2:
                continue
            idx1 = cost.index(c)
            cost[idx1] = None
            idx2 = cost.index(money-c)
            print(*sorted((idx1+1, idx2+1)))
            break


whatFlavors([50, 50, 1, 1, 1, 1], 100)
whatFlavors([7, 2, 5, 4, 11], 12)
