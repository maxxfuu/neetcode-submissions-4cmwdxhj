class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""

        for char in s: 
            if char.isalnum(): 
                result += char.lower()

        return result == result[::-1] 
