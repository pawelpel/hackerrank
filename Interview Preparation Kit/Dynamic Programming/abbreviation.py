# https://www.hackerrank.com/challenges/abbr/problem
# https://www.youtube.com/watch?v=4WzCFTmjKu4

def abbreviation(a, b):
    a_len = len(a)
    abbr_len = len(b)
    dp = [
        [False] * (abbr_len + 1) for _ in range(a_len + 1)
    ]
    dp[0][0] = True
    for i in range(a_len):
        for j in range(abbr_len + 1):
            if dp[i][j]:
                if j < abbr_len and a[i].upper() == b[j]:
                    dp[i + 1][j + 1] = True
                if a[i].islower():
                    dp[i + 1][j] = True

    return 'YES' if dp[a_len][abbr_len] else 'NO'
