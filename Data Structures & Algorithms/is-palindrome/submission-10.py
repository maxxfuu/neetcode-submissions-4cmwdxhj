class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        
        for c in s:
            if (c.isalnum()):
                newString += c.lower()
                print(c)
        
        left, right = 0, len(newString) - 1

        while left < right:
            if (newString[left] != newString[right]): 
                return False

            left += 1
            right -= 1
        return True
