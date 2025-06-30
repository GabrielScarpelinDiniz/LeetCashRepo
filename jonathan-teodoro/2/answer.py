# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        l1_num = []
        l2_num = []
        while curr1 or curr2:
            if curr1:
                l1_num.append(curr1.val)
                curr1 = curr1.next
            if curr2:
                l2_num.append(curr2.val)
                curr2 = curr2.next

        l1_num.reverse()
        l2_num.reverse()

        l2_str = ""
        l1_str = ""
        for i in l1_num:
            l1_str += str(i)

        for i in l2_num:
            l2_str += str(i)
        
        sum = int(l1_str) + int(l2_str)
        new_ll = ListNode(int(str(sum)[-1]))
        curr = new_ll

        i = len(str(sum))-2
        while i >= 0:
            curr.next = ListNode(int(str(sum)[i]))
            curr = curr.next
            i-=1
        
        return new_ll