class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers 
        left, right = 0, len(s) - 1
        while left < right: 

            while left < right and not s[left].isalnum(): 
                left += 1
            while left < right and not s[right].isalnum(): 
                right -= 1

                
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else: 
                return False 

        return True 

        # String Manipulation 
        # string = "" 
        # for char in s: 
        #     if char in s: 
        #         if char.isalnum(): 
        #             string += char.lower()  
        # return string == string[::-1]