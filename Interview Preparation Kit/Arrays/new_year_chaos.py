# https://www.hackerrank.com/challenges/new-year-chaos/


def minimumBribes(q):
    bribes = 0
    for i, person in enumerate(q, start=1):
        if person - i > 2:
            print("Too chaotic")
            return
        for j in range(max(person-2, 0), i):
            if q[j] > person:
                bribes += 1
    print(bribes)
    return bribes


assert minimumBribes([2, 1, 5, 3, 4]) == 3
assert minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]) == 7
