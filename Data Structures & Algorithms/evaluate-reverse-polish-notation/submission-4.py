class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 

        # Helper Function to check for all integers 
        def is_integer(num: str) -> bool: 
            try: 
                int(num)  
                return True 
            except ValueError: 
                return False 

        for i in range(len(tokens)):  
            if is_integer(tokens[i]): 
                stack.append(int(tokens[i])) 
            else: 
                nums2 = stack.pop() 
                nums1 = stack.pop() 

                if tokens[i] == "+":
                    stack.append(nums1 + nums2) 
                elif tokens[i] == "-": 
                    stack.append(nums1 - nums2) 
                elif tokens[i] == "*":
                    stack.append(nums1  * nums2)  
                elif tokens[i] == "/":
                    stack.append(int(nums1 / nums2))  
        
        return stack[0]
