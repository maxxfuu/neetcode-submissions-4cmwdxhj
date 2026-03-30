class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0  # Minimum possible unmatched '('
        high = 0  # Maximum possible unmatched '('
        
        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                if low > 0:
                    low -= 1
                high -= 1
            elif char == '*':
                if low > 0:
                    low -= 1
                high += 1
            
            # If `high` becomes negative, too many unmatched `)`
            if high < 0:
                return False
        
        # Valid if all possible unmatched `(` can be balanced
        return low == 0
