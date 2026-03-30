# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    head1, head2 = l1, l2
    dummy = node = ListNode(0)

    carry = 0
    while head1 and head2:
      total = head1.val + head2.val + carry
      carry = total // 10
      remainder = total % 10 

      node.next = ListNode(remainder)
      node = node.next

      head1 = head1.next
      head2 = head2.next
    
    # Handle Edge case
    if head1 == None:
      loneNode = head2
    else:
      loneNode = head1

    while loneNode:
      total = loneNode.val + carry
      carry = total // 10
      remainder = total % 10
      node.next = ListNode(remainder)
      node = node.next

      loneNode = loneNode.next

    if carry > 0:
      node.next = ListNode(carry)

    return dummy.next