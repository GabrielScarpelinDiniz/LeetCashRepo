class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
       
        while curr and curr.next:
            temp_val = curr.val
            curr.val = curr.next.val
            curr.next.val = temp_val
            curr = curr.next.next
            
        return head  
