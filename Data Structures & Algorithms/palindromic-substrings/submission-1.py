class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s) 
        pal_memo, memo = {}, {}

        def dp(i, j):
            if i >= j:
                return True 
            
            if (i, j) in pal_memo:
                return pal_memo[(i, j)]
            
            pal_memo[(i, j)] = s[i] == s[j] and dp(i + 1, j - 1)
            return pal_memo[(i, j)]

        def count(i, j):
            if i > j:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]
           
            if dp(i, j): 
                curr = 1
            else:
                curr = 0

            memo[(i, j)] = curr + count(i + 1, j) + count(i, j - 1) - count(i + 1, j - 1)
            return memo[(i, j)]
        
        return count(0, n - 1) 

        # n = len(s) - 1
        # count = 0 

        # def recur(left: int, right: int) -> int:
        #     # Either pointer goes out of bounds 
        #     if left < 0 or right > n:
        #         return 0

        #     # Not palindromic 
        #     if s[left] != s[right]:
        #         return 0

        #     left -= 1
        #     right += 1

        #     return 1 + recur(left, right) 

        # for i in range(len(s)):
        #     count += recur(i, i)
        #     count += recur(i, i+1)

        # return count
        