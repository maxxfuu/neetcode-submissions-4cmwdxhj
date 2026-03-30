# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        map = {} 
        curr = head.next 
        index = 0 

        while curr: 
            if curr not in map: 
                map[curr] = index
                curr = curr.next 
            else: 
                return True 
            index += 1 
        return False  

