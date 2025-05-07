# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        last = current
        found = {}
        while current != None:
            if found.get(current.val) == None:
                found[current.val] = True
                last = current
                current = current.next
            else:
                last.next = current.next
                current = current.next

        return head
