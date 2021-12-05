# https://www.hackerrank.com/challenges/counting-valleys/

def countingValleys(steps, path):
    pos = 0
    counter = 0
    for p in path:
        if p == 'U':
            pos += 1
        if p == 'D':
            if pos == 0:
                counter += 1
            pos -= 1
    return counter
