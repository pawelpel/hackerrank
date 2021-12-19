# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/

def height(root):
    h = 0
    if root.left:
        h = max(h, 1 + height(root.left))
    if root.right:
        h = max(h, 1 + height(root.right))
    return h
