# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        anterior = None
        atual = head

        while atual:
            proximo = atual.next
            atual.next = anterior
            anterior = atual
            atual = proximo
        
        return anterior