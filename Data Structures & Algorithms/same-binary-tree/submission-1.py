# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and q or not q and p: 
            return False 

        stack1 = [p]
        stack2 = [q] 

        while stack1 and stack2: 
            nodeP = stack1.pop(0)
            nodeQ = stack2.pop(0) 

            if nodeP is None and nodeQ is None: 
                continue 

            if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val: 
                return False 

            stack1.append(nodeP.left) 
            stack1.append(nodeP.right) 
 
            stack2.append(nodeQ.left) 
            stack2.append(nodeQ.right)        

        return True  