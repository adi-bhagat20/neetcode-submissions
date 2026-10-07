class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = [0]*26

        for ch in s:
            chars[ord(ch) - ord('a')] += 1
        
        for ch in t:
            chars[ord(ch) - ord('a')] -= 1
        
        for n in chars:
            if n != 0:
                return False
        return True