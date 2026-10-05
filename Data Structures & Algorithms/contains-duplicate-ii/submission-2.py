class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k < 1:
            return False
        L = 0
        hashSet = set()
        for R in range(len(nums)):
            if R - L > k:
                hashSet.remove(nums[L])
                L+=1
            
            if nums[R] in hashSet:
                return True
            hashSet.add(nums[R])
        
        return False