class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
       
        while curr and curr.next:
            temp_val = curr.val
            curr.val = curr.next.val
            curr.next.val = temp_val
            curr = curr.next.next
            
        return head  

Esse código percorre a lista ligada dois nós por vez e troca os valores entre cada par de nós vizinhos. Ele não altera a estrutura da lista (ou seja, não muda os ponteiros next), só faz um swap dos valores (val). A cada iteração, ele pega o valor do nó atual (curr), troca com o valor do próximo (curr.next), e depois pula dois nós pra frente, indo direto pro próximo par. No final, retorna a cabeça da lista, que agora tem os valores dos pares trocados.

