# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = []
        curr = head

        while curr:
            temp.append(curr)
            curr = curr.next

        left, right = 0, len(temp) - 1

        while left < right:
            temp[left].next = temp[right]
            left += 1
            temp[right].next = temp[left]
            right -= 1

        temp[left].next = None