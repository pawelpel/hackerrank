# https://www.hackerrank.com/challenges/2d-array/

def hourglassSum(arr):
    def get_hourglass_sum(row, col):
        cells = [
           *[(row-1, y) for y in (col-1, col, col+1)],
           (row, col),
           *[(row+1, y) for y in (col-1, col, col+1)],
        ]
        return sum(arr[cell[0]][cell[1]] for cell in cells)
    maximum = float('-inf')
    for r in range(1, 5):
        for c in range(1, 5):
            s = get_hourglass_sum(r, c)
            maximum = max(s, maximum)
    return maximum
