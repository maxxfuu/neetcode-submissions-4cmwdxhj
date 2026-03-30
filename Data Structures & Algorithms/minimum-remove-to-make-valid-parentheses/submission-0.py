class Solution:
  def minRemoveToMakeValid(self, s: str) -> str:
    stack = [] # [['(', index], ]
    s_arr = list(s)

    for index, char in enumerate(s): 
      if char == '(':
        stack.append([char, index])
      elif char == ')':
        if stack and stack[-1][0] == "(":
          stack.pop()
        else:
          stack.append([char, index])

    for item in reversed(stack): 
      s_arr.pop(item[1])

    return "".join(s_arr)
          

  
        
      