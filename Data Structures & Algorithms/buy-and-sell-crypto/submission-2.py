class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        each_min = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            each_min = min(each_min, prices[i])
            max_profit = max(max_profit, (prices[i] - each_min))
        
        return max_profit



        