class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for word in strs:

            og = [0]*26

            for ch in word:
                og[ord(ch) - ord('a')] += 1
            
            key = tuple(og)
            d[key] = d.get(key ,[])
            d[key].append(word)

        return list(d.values())