``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            next_node = curr.next

            if next_node.val == curr.val:
                curr.next = next_node.next

            if curr and curr.next and curr.val != curr.next.val:
                curr = curr.next
        return head
```

Estou na onda de exercícios de linked list pra treinar essa estrutura de dados. Esse aqui é um exercicio bem padrao, preciso remover duplicatas de uma linked list. A solucao é simples: Percorro a linked list da forma padrão, enquanto houver o nó atual e o próximo. Ai eu confiro se o proximo é igual ao atual, se for eu pulo ele e adiciona para o "next" do curr para apontar para o que vem depois desse nó. Feito isso, faco uma validação - so mudo pro proximo no loop quando o proximo for diferente do atual.