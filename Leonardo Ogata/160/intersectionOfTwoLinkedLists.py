# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        currentA = headA 
        counterA = 0

        while currentA.next != None:
            currentA = currentA.next
            counterA += 1
        currentA = headA 

        currentB = headB 
        counterB = 0

        while currentB.next != None:
            currentB = currentB.next
            counterB += 1
        currentB = headB 

        skip = abs(counterA - counterB)

        if counterA > counterB:
            smallest = currentB
            biggest = currentA
        else: 
            smallest = currentA
            biggest = currentB
        
        for x in range(skip):
            biggest = biggest.next
        
        
        while biggest and smallest:
            if biggest == smallest:
                return biggest
            biggest = biggest.next
            smallest = smallest.next
        return 