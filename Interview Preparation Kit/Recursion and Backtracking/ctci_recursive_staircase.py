# https://www.hackerrank.com/challenges/ctci-recursive-staircase/

def stepPerms(n):
    cache = {}
    
    def count(left_stairs):
        if left_stairs in cache:
            return cache[left_stairs]

        if left_stairs == 1:
            t = 1  # (1)
        elif left_stairs == 2:
            t = 2  # (1,1) (2)
        elif left_stairs == 3:
            t = 4  # (1,1,1), (1,2), (2,1), (3)
        else:
            t = count(left_stairs-1) + count(left_stairs-2) + count(left_stairs-3)
        cache[left_stairs] = t
        return t

    total = count(n)   
    
    return total % (10**10 + 7)


assert stepPerms(1) == 1
assert stepPerms(3) == 4
assert stepPerms(7) == 44
