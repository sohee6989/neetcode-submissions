class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                maxProfit = max(maxProfit, prices[r]-prices[l])
            else:
                l = r
            r += 1
 
        return maxProfit



    def maxProfit2(self, prices: List[int]) -> int:
        maxProfit = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > maxProfit:
                    maxProfit = prices[j] - prices[i]

        return maxProfit
        