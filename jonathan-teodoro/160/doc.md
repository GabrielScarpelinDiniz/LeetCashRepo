# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dicionario = set()
        currA = headA
        currB = headB

        while currA:
            if currA not in dicionario:
                dicionario.add(currA)
            currA = currA.next
        
        while currB:
            if currB in dicionario:
                return currB
            currB = currB.next

        return None

            
Fiz uma alternativa cool. Utilizo a estrategia dos visitados, percorro a lista um e adiciono os nós na lista visitados, depois percorro a 2, se o nó voltar a aparecer, eu retorno ele e sigo o fluxo. Bem simples a estrategia, gosto muito de exercicios de linked list.