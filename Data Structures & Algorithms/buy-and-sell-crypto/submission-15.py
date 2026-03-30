# In order to make a profit you have to buy low sell high. 

class Solution:
    # two pointer, O(n log n)
    def maxProfit(self, prices: List[int]) -> int: 
        currMax = 0
        buy, sell = 0, 1

        while sell < len(prices):
            if (prices[sell] > prices[buy]):
                currMax = max(currMax, (prices[sell] - prices[buy]))
            else:
                buy = sell
            sell += 1

        return currMax  

    # brute force approach 
    # def maxProfit(self, prices: List[int]) -> int:
    #     currMax = 0 
    #     for buy in range(len(prices) - 1):
    #         for sell in range(buy + 1, len(prices)):
    #             profit = prices[sell] - prices[buy]
    #             currMax = max(currMax, profit) 
    #     return currMax

            