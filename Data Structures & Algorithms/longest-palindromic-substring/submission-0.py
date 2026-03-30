class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        def helper(s, l, r):
            maxStr = ""

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l : r + 1]) > len(maxStr):
                    maxStr = s[l : r + 1]
                l -= 1
                r += 1

            return maxStr 

        for i in range(len(s)):
            if len(helper(s, i, i)) > len(longest): 
                longest = helper(s, i, i) 

            if len(helper(s, i, i + 1)) > len(longest):
                longest = helper(s, i, i + 1)
        
        return longest