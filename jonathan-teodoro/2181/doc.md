``` PYTHON
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
```                
        
Todo mundo ta ligado que nos dias de aperto faço exercícioa de linked list, são minhas questões de segurança. Bem tranquilinho, sem segredo:
Percorro a lista original com um ponteiro curr e vai somando os valores entre os zeros usando uma variável count. Sempre que encontra um nó com valor 0 e o contador for maior que 0, ele entende que terminou de somar um bloco, e adiciona o valor acumulado count na nova lista (curr_new_list). A cada novo bloco de soma, ele cria um novo nó para continuar preenchendo a nova lista. Quando não está em um zero, ele só acumula o valor do nó. No final, retorna a nova lista construída, que contém a soma dos blocos entre zeros.