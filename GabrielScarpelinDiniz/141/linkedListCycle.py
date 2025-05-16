# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hashmap = {}
        current = head
        idx = 0
        while current != None:
            hashmap[current] = idx

            if hashmap.get(current.next) != None:
                return True

            current = current.next

        return False
