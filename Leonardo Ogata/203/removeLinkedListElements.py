# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        current = head

        arr = []
                
        while current:
            arr.append(current.val)
            current = current.next
        
        for i in range(len(arr) -1, -1, -1):
            if arr[i] == val:
                arr.pop(i)
        
        arrNodes = []

        for x in range(len(arr)):
            arrNodes.append(ListNode(arr[x]))

        for i in range(len(arrNodes) - 1):
            arrNodes[i].next = arrNodes[i + 1]
        
        return arrNodes[0] if arrNodes else None


        


            
            
            
        