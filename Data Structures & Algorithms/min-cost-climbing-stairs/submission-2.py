class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}

        def recursion(i):
            if i >= len(cost):
                return 0

            if i in cache:
                return cache[i]
            else:
                cache[i] = cost[i] + min(recursion(i + 1), recursion(i + 2))
            return cache[i]
            
        return min(recursion(0), recursion(1))