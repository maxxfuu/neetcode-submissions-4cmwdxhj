class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def recursion(i):
            if (i == len(cost) - 1): 
                return cost[i]

            if (i > len(cost) - 1): 
                return 0

            if recursion(i + 2) > recursion(i + 1):
                return cost[i] + recursion(i + 1)
            else:
                return cost[i] + recursion(i + 2)

        return min(recursion(0), recursion(1))

"""
subproblem: each ith value that we start at, we keep shifting by 2 until the end or past the end. 
basecase: when we reached the end of the cost or past the cost.
"""
        