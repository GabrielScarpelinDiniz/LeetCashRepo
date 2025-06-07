class Solution(object):
    def removeElements(self, head, val):
        while head and head.val == val:
            head = head.next
        if head == None:
            return head
        t = head
        n = None
        while t:
            if t.val == val:
                n.next = t.next
                t = n.next
            else:
                n =t
                t = t.next
        return head



            
        


        