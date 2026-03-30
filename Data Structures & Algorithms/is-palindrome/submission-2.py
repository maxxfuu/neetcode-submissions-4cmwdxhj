class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = "" 

        for char in s: 
            if char.isalnum():
                newString += char.lower()
                print(char)

        left, right = 0, len(newString) - 1 

        while (left < right): 
            if (newString[left] == newString[right]): 
                left += 1 
                right -= 1
            else: 
                return False 
             
        return True 