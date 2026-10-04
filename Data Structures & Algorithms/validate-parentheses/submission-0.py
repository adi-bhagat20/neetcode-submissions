class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }
        stack = []

        for ch in s:
            if ch not in d:
                stack.append(ch)
            else:
                if d[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return not stack