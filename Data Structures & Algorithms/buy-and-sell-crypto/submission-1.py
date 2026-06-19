class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        each_min = -1
        max_profit = 0
        for price in prices:
            if each_min == -1:
                each_min = price
            else:
                each_min = min(each_min, price)
            max_profit = max(max_profit, (price - each_min))
        
        return max_profit



        