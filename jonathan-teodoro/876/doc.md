# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        answer = []
        while (curr):
            answer.append(curr)
            curr = curr.next

        mid = len(answer)//2
        return answer[mid]

Exercício moleza de Linked List. O que eu faço? Uso uma variável auxiliar para determinar em qual node estou da linked list - enquanto o node atual nao for nulo eu vou adicionando o a um array auxiliar. Ao final do for eu tenho uma lista com todos nodes - o que eu faco?pego o len e busco o item do meio, ai eu so retorno o item da lista que ta no indice. Molezinha