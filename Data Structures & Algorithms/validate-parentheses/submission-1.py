class Solution:
    def isValid(self, s: str) -> bool:
        map = {"(" : ")", "{" : "}", "[" : "]"} 
        stack = [] 

        for char in s: 
            if char in map: # if char is a opening type 
                stack.append(char) # push it to the stack 
            else: # Assume that the the char is closing type
                if len(stack) == 0: 
                    return False 
                topOfStack = stack[-1]  # get the opening 
                stack.pop() # delete element from stack 
                if char != map.get(topOfStack): # Evaluate  
                    return False
        if len(stack) == 0: # meaning its empty  
            return True 
        
        return False 

# Second iter: ] 
# Stack: [