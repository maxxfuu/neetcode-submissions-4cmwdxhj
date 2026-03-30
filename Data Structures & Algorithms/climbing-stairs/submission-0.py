class Solution:
    def climbStairs(self, n: int) -> int:
        def backTrack(n):
            if n == 0:
                return 1
            
            if n < 0:
                return 0
            
            return backTrack(n - 1) + backTrack(n - 2)
        
        return backTrack(n)
            