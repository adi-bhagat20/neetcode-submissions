class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)
        ans = r

        while l <= r:
            k = l + (r - l)//2

            totalTime = 0
            for p in piles:
                totalTime += (p + k - 1) // k
            if totalTime <= h:
                ans = k
                r = k - 1
            else:
                l = k + 1
        return ans