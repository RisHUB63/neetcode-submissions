class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        each_min = []

        max_profit = 0
        for price in prices:
            if len(each_min) == 0:
                each_min.append(price)
            else:
                _min = min(each_min[len(each_min) - 1], price)
                each_min.append(_min)
            max_profit = max(max_profit, (price - each_min[len(each_min) - 1]))
        
        return max_profit



        