# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        pseudo = ListNode(-1) 
        pseudoHead = pseudo
        curr1, curr2 = list1, list2

        while curr1 and curr2:
            if curr1.val == curr2.val:
                pseudo.next = curr1
                curr1 = curr1.next
            elif curr1.val > curr2.val:
                pseudo.next = curr2
                curr2 = curr2.next
            elif curr1.val < curr2.val:
                pseudo.next = curr1
                curr1 = curr1.next
            pseudo = pseudo.next
            
        if curr1 == None:
            pseudo.next = curr2
        else: 
            pseudo.next = curr1

        return pseudoHead.next


                

