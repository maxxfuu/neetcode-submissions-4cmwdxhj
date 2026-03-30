class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        cache = {}

        def dp(i):
            if i in cache:
                return cache[i]
            
            if i == n:
                return 1

            if s[i] == '0':
                return 0
            
            ways = dp(i + 1)

            if i + 1 < n and 10 <= int(s[i:i+2]) <= 26: 
                ways += dp(i + 2)

            cache[i] = ways
            return cache[i] 
        
        return dp(0)
