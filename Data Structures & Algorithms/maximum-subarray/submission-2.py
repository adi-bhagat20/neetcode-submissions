class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxL , maxR = -1 , -1
        L = 0
        maxSum = float('-inf')
        currSum = 0

        for R in range(len(nums)):
            if currSum < 0:
                currSum = 0
                L = R
            
            currSum += nums[R]

            if currSum > maxSum:
                maxSum = currSum
                maxL , maxR = L , R
        
        return maxSum