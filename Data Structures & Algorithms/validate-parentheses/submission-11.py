class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"(":")", "{":"}", "[":"]"}
        stack = []

        if len(s) < 2:
            return False

        for symbol in s:
            if symbol in hashmap:
                stack.append(symbol)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if hashmap[popped] != symbol:
                        return False 
        return not stack 