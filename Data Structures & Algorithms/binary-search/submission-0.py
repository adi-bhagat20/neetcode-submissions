class Solution:
    def bs(self , nums , low , high ,target):
        if low > high:
            return -1
        mid = low + (high - low)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.bs(nums , low , mid - 1 , target)
        else:
            return self.bs(nums , mid +1, high , target)

    def search(self, nums: List[int], target: int) -> int:
        return self.bs(nums , 0 , len(nums) - 1 ,target)