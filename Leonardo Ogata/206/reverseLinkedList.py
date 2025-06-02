# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not head:
            return head

        arrVal = []
        current = head

        while current:
            arrVal.append(current.val)
            current = current.next
        
        arrVal.reverse()

        arrNodes = []

        for x in range(len(arrVal)):
            arrNodes.append(ListNode(arrVal[x]))
        
        for i in range(len(arrNodes) - 1):
            arrNodes[i].next = arrNodes[i + 1]
        
        return arrNodes[0] 
        