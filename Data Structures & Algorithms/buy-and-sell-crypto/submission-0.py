class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        if len(prices) == 1:
            return 0
        for i in range(len(prices) - 1):
            for j in range(i+1 , len(prices)):
                if prices[j] - prices[i] > maxProfit:
                    maxProfit = prices[j] - prices[i]


        return 0 if maxProfit < 0 else maxProfit