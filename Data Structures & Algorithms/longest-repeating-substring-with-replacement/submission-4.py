class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxF = 0
        count = [0]*26
        L = 0

        for R in range(len(s)):
            idx = ord(s[R]) - ord('A')
            count[idx] += 1
            maxF = max(maxF , count[idx])
            if (R - L + 1) - maxF > k:
                count[ord(s[L]) - ord('A')] -= 1
                L += 1
        
        return len(s) - L