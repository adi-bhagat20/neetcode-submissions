class Solution:
    def isValid(self, s: str) -> bool:
        d = {')' : '(' , '}' : '{' , ']' : '['}
        stack = []

        for ch in s:
            if ch not in d:
                stack.append(ch)
            else:
                if not stack or d[ch] != stack.pop():
                    return False

        return not stack
                