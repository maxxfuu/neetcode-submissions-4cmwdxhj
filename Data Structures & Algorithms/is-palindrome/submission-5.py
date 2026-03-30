class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Solve this using left and right pointer  
        strs = "" 
        for char in s: 
            if char.isalnum(): 
                strs += char .lower()
        
        left, right = 0, len(strs) - 1 
        while left < right: 
            if strs[left] == strs[right]: 
                left += 1
                right -= 1
            else: 
                return False 
        
        return True 


        
        # String Comparison Method 
        # result = ""

        # for char in s: 
        #     if char.isalnum(): 
        #         result += char.lower()

        # return result == result[::-1] 
