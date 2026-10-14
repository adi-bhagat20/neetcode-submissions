class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        countOfZeros = 0
        product = 1
        idxOfZero = -1

        for i , num in enumerate(nums):
            if num == 0:
                countOfZeros += 1
                idxOfZero = i
                continue
            
            if countOfZeros > 1:
                return [0]*len(nums)

            product = product*num

        if idxOfZero == -1:
            for i in range(len(nums)):
                nums[i] = product//nums[i]
            return nums
        else:
            nums = [0]*len(nums)
            nums[idxOfZero] = product
            return nums
                    