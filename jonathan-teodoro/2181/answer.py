# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = 0
        head_new_list = ListNode()
        curr_new_list = head_new_list
        while curr:
            if curr.val == 0:
                if count > 0 and curr_new_list:
                    print(curr.val, count)
                    curr_new_list.val = count
                    count = 0
                    if curr.next:
                        curr_new_list.next = ListNode()
                        curr_new_list = curr_new_list.next
            else:
                count += curr.val

            curr = curr.next
        
        return head_new_list
                
        