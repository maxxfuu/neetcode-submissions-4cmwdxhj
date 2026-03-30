class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dp(amount):
            if amount == 0:
                return 0

            if amount in cache:
                return cache[amount] 

            res = 1e9

            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dp(amount - coin))
            cache[amount] = res
            return res 
        
        return -1 if dp(amount) == 1e9 else dp(amount)
                