class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s) - 1
        count = 0 

        def recur(left: int, right: int) -> int:
            # Either pointer goes out of bounds 
            if left < 0 or right > n:
                return 0

            # Not palindromic 
            if s[left] != s[right]:
                return 0

            left -= 1
            right += 1

            return 1 + recur(left, right) 

        for i in range(len(s)):
            count += recur(i, i)
            count += recur(i, i+1)
        return count
        