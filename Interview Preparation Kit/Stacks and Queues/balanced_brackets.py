# https://www.hackerrank.com/challenges/balanced-brackets/

def isBalanced(s):
    stack = []
    
    brackets = {
        '}': '{',
        ')': '(',
        ']': '[',
    }
    openings = brackets.values()
    
    for b in s:
        if b in openings:
            stack.append(b)
        else:
            if not stack or stack.pop() != brackets[b]:
                return "NO"
    
    return "YES" if not stack else "NO"


assert isBalanced("()[]{}") == "YES"
assert isBalanced("([{}])") == "YES"
assert isBalanced("])([") == "NO"
assert isBalanced("(((((((((((()") == "NO"
