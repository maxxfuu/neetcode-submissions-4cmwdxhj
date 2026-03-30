# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle point of the linked list 
        slow, fast = head, head.next 
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next 
        
        second = slow.next 
        slow.next = None 
        
        # Reverse Second Hald 
        prev = None 
        while second: 
            temp = second.next 
            second.next = prev  
            prev = second 
            second = temp  

        # Merge Two Half 
        first, second = head, prev 
        while second: 
            temp1, temp2 = first.next, second.next 
            first.next = second 
            second.next = temp1 
            first, second = temp1, temp2

         