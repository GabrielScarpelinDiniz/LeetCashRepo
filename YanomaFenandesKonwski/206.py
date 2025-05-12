class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class LinkedList:
#     def __init__(self, head=None):
#         self.head = head

#     def insert(self, value):
#         no = ListNode(value)
#         if self.head is None:
#             self.head = no
#             return
#         currentNode = self.head
#         while True:
#             if currentNode.next is None:
#                 currentNode.next = no
#                 break
#             currentNode = currentNode.next

#     def printLinkedList(self):
#         currentNode = self.head
#         while currentNode is not None:
#             print (currentNode.val)
#             currentNode = currentNode.next
#         print(None)

# ll = LinkedList()
# ll.insert("8")
# ll.insert("9")
# ll.insert("10")
# ll.printLinkedList()

            

        