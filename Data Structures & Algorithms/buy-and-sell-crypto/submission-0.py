class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = prices[0]
        maxprof = 0

        for i in prices[1:]:
            profit = i - b
            maxprof = max(maxprof,profit)
            b = min(b, i)

        return maxprof