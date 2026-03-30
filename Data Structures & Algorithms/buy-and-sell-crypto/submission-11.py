# In order to make a profit you have to buy low sell high. 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMax = 0 
        for buy in range(len(prices) - 1):
            for sell in range(buy + 1, len(prices)):
                profit = prices[sell] - prices[buy]
                currMax = max(currMax, profit) 
                print(f"sell: {sell}, buy: {buy}, total: {profit}")
        return currMax

            