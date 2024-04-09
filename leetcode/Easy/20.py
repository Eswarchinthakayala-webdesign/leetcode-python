class Solution(object):
    def isValid(self, s):
        paren = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in paren.values():
                stack.append(char)
            elif char in paren.keys():
                if not stack or stack.pop() != paren[char]:
                    return False
        return not stack

