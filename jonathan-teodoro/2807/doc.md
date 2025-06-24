# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        def mdc(a, b):
            while b:
                a, b = b, a % b
            return a

        while curr and curr.next:
            next_node = curr.next
            new_val = mdc(curr.val, next_node.val)
            new_node = ListNode(new_val, next_node)
            curr.next = new_node
            curr = next_node 
        return head

primeira coisa a ser feita é gerar uma funcao auxiliar de MDC, preciso dela para descobrir qual valor eu devo inserir. Feito isso eu percorro a Linked List, enquanto ovalor da atual não for nulo nem o da proxima. A partir daí, pego o nó atual e o proximo e calculo o mdc entre eles, em sequencia eu adiciono esse node apos o atual (curr.next = new_node) e ja crio esse new_node apontando para o que antes era o .next. Bem simples, exercício ivertido de Linked List.
