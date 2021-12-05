# https://www.hackerrank.com/challenges/jumping-on-the-clouds/

def jumpingOnClouds(c):
    jumps = 0
    cloud_idx = 0
    clouds_len = len(c)
    while cloud_idx < clouds_len - 1:
        if cloud_idx + 2 < clouds_len and c[cloud_idx + 2] == 0:
            cloud_idx += 2
        else:
            cloud_idx += 1
        jumps += 1
    return jumps
