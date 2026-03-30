class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) 
        stack = [] # pair: [temp, index] 

        for index, temperature in enumerate(temperatures): 
            while stack and temperature > stack[-1][0]: 
                stackTemp, stackIndex = stack.pop() 
                res[stackIndex] = index - stackIndex 
            stack.append((temperature, index)) 
        return res
