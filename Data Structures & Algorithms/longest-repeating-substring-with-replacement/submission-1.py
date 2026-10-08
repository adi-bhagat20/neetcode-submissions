class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        arr = [0]*26
        maxL = 0
        L = 0

        for R in range(len(s)):
            arr[ord(s[R]) - ord('A')] += 1
            if (R - L + 1) - max(arr) <= k:
                maxL = max(maxL , R - L + 1)
            else:
                while (R-L+1) - max(arr) > k:
                    arr[ord(s[L]) - ord('A')] -= 1
                    L+=1
        return maxL