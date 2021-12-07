# https://www.hackerrank.com/challenges/max-array-sum/

def maxSubsetSum(arr):
    v = [0] * len(arr)

    for i in range(len(arr)):
        if i < 2:
            v[i] = max(arr[i], 0)
            continue
        elif i == 2:
            v[i] = v[i - 2] + max(arr[i], 0)
            continue

        v[i] = max(v[i - 2], v[i - 3]) + max(arr[i], 0)

    return max(v[-1], v[-2])
