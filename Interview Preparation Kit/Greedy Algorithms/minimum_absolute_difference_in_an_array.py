# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/

def minimumAbsoluteDifference(arr):
    minimum = None
    arr = sorted(arr)
    start = 0
    stop = len(arr) - 1
    while start != stop:
        dif = abs(arr[start] - arr[stop])
        if minimum:
            minimum = min(minimum, dif)
        else:
            minimum = dif
        if abs(arr[start+1] - arr[stop]) < abs(arr[start] - arr[stop-1]):
            start += 1
        else:
            stop -= 1
    return minimum
