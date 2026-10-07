class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = [0]*26

        if len(s) != len(t):
            return False
        
        for chs , cht in zip(s , t):
            if chs == cht:
                continue
            
            if chars[ord(chs) - ord('a')] != 0:
                chars[ord(chs) - ord('a')] += 1
            elif chars[ord(chs) - ord('a')] == 0:
                chars[ord(chs) - ord('a')] -= 1
            
            if chars[ord(cht) - ord('a')] != 0:
                chars[ord(cht) - ord('a')] += 1
            elif chars[ord(cht) - ord('a')] == 0:
                chars[ord(cht) - ord('a')] -= 1
            
        for n in chars:
            if n != 0:
                return False
        return True