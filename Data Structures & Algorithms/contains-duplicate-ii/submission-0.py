class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k < 2:
            return False
        L = 0
        hashSet = set()
        hashSet.add(nums[L])
        for R in range(1 , len(nums)):
            if abs(L - R) <= k:
                if nums[R] in hashSet:
                    return True
            else:
                hashSet.remove(nums[L])
                L+=1
                if nums[R] in hashSet:
                    return True
        
        return False