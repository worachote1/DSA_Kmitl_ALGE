#Ex_121 Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: list[int]):
        min_data = float('inf')
        maxProfit = 0
        for item in prices:
            if(item<min_data):
                min_data = item
            maxProfit = max(maxProfit,item-min_data)
        return maxProfit