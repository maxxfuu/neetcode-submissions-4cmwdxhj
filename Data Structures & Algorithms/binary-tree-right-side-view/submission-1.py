# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def rightMostValue(lst: list) -> int:
            for i in range(len(lst) - 1, -1, -1):
                if lst[i] != -1:
                    return lst[i]
            return 

        if not root:
            return []

        queue = collections.deque()
        queue.append(root)
        res = [root.val]

        while queue:
            queueLength = len(queue)
            level = []
            for i in range(queueLength):
                node = queue.popleft()
                
                if node.left:
                    level.append(node.left.val) 
                    queue.append(node.left)
                else:
                    level.append(-1)
                
                if node.right:
                    level.append(node.right.val)
                    queue.append(node.right)
                else:
                    level.append(-1)

            print(level)
            res.append(rightMostValue(level))
        res.pop() 
        return res
        