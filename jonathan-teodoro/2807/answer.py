# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        def mdc(a, b):
            while b:
                a, b = b, a % b
            return a

        while curr and curr.next:
            next_node = curr.next
            new_val = mdc(curr.val, next_node.val)
            new_node = ListNode(new_val, next_node)
            curr.next = new_node
            curr = next_node 
        return head
