# https://www.hackerrank.com/challenges/ctci-bubble-sort/

def countSwaps(a):
    counter = 0

    def swap(x, y):
        nonlocal counter
        tmp = a[x]
        a[x] = a[y]
        a[y] = tmp
        counter += 1

    a_len = len(a)
    for i in range(a_len):
        for j in range(a_len - 1):
            if a[j] > a[j + 1]:
                swap(j, j + 1)

    print(f"Array is sorted in {counter} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
