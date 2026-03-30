class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
    operator = ['+', '-', '*', '/']
    stack = []
    valA, valB = 0, 0

    i = 1
    for char in tokens:
      if char not in operator:
        stack.append(int(char))
      else:
        valA = stack.pop() # 1
        valB = stack.pop() # 2 
          
        if char == '+':
          stack.append(valA + valB)
        elif char == '-':
          stack.append(valB - valA)
        elif char == '*':
          stack.append(valA * valB)
        else:
          stack.append(0 if (valA == 0 or valB == 0) else int(valB / valA))
    
    return stack[-1]
