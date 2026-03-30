class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {}

        def recursion(n: int) -> int:
            # base condition
            if n == 0: return 0
            elif n == 1: return 1
            elif n == 2: return 1

            if n in cache:
                return cache[n]

            cache[n] = recursion(n-1) + recursion(n-2) + recursion(n-3)
            return cache[n]

        return recursion(n)         
