# https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/


def lca(root, v1, v2):

    def find(n, path, search_n):
        path.append(n)
        if n.left and n.left.info == search_n:
            path.append(n.left)
            return True, path
        elif n.right and n.right.info == search_n:
            path.append(n.right)
            return True, path

        if n.left is not None:
            found, p = find(n.left, path.copy(), search_n)
            if found:
                return found, p

        if n.right is not None:
            found, p = find(n.right, path.copy(), search_n)
            if found:
                return found, p

        return False, path

    _, v1_path = find(root, [], v1)
    _, v2_path = find(root, [], v2)

    i = 0
    while i < len(v1_path) and i < len(v2_path):
        if v1_path[i] != v2_path[i]:
            break
        i += 1

    return v2_path[i-1]
