# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getMinValueAndIdxAndFinished(pointers):
    minValue = None
    minIdx = None
    allNone = True
    for i in range(len(pointers)):
        if pointers[i] != None:
            allNone = False
            if minValue == None:
                minValue = pointers[i].val
                minIdx = i
            else:
                if pointers[i].val < minValue:
                    minIdx = i
                    minValue = pointers[i].val
    return minValue, minIdx, allNone

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if len(lists) == 0:
            return None

        pointers = [0] * len(lists)
        for i in range(len(lists)):
            pointers[i] = lists[i]

        current = ListNode(0, None)
        root = current
        finished = False
        while finished == False:
            minV, idx, finished = getMinValueAndIdxAndFinished(pointers)
            if idx != None:
                pointers[idx] = pointers[idx].next
                if pointers[idx] == None:
                    pointers.pop(idx)

            if minV != None:
                current.next = ListNode(minV, None)
                current = current.next

        return root.next
