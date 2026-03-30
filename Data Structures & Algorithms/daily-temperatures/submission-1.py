class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Stack 
        res = [0] * len(temperatures)
        stack = [] # [[index, temperature]]

        for tempInd, tempVal in enumerate(temperatures):
            while stack and stack[-1][1] < tempVal:
                res[stack[-1][0]] = tempInd - stack[-1][0]
                stack.pop()
            stack.append([tempInd, tempVal]) 
        return res

        # # Brute Force
        # result = []
        # for left in range(len(temperatures)):
        #     print(left)
        #     right = left 
        #     while temperatures[left] >= temperatures[right] and right < len(temperatures) - 1:
        #         right += 1

        #     if temperatures[left] < temperatures[right]:
        #         result.append(len(temperatures[left:right + 1]) - 1)
        #     else:
        #         result.append(0)
        
        # return result
    