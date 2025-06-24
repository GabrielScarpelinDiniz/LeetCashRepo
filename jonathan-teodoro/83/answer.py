# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            next_node = curr.next

            if next_node.val == curr.val:
                curr.next = next_node.next

            if curr and curr.next and curr.val != curr.next.val:
                curr = curr.next
        return head