# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        l1_num = []
        l2_num = []
        while curr1 or curr2:
            if curr1:
                l1_num.append(curr1.val)
                curr1 = curr1.next
            if curr2:
                l2_num.append(curr2.val)
                curr2 = curr2.next

        l1_num.reverse()
        l2_num.reverse()

        l2_str = ""
        l1_str = ""
        for i in l1_num:
            l1_str += str(i)

        for i in l2_num:
            l2_str += str(i)
        
        sum = int(l1_str) + int(l2_str)
        new_ll = ListNode(int(str(sum)[-1]))
        curr = new_ll

        i = len(str(sum))-2
        while i >= 0:
            curr.next = ListNode(int(str(sum)[i]))
            curr = curr.next
            i-=1
        
        return new_ll

Tenho a leve impressao de que escrevi o codigo mais porco da história! Mas funciona! Excesso de memoria e de tempo, codigo pesado e demorado. Mas foi muito bom para eu reforçar meu conhecimento em linked list. Com ctz irei refatorá-lo em algum momento. Vai ser treta explicar:

Primeiro soma dois números representados por listas ligadas (l1 e l2), onde cada nó tem um dígito, e os dígitos estão em ordem reversa (ou seja, o número 342 seria representado como 2 → 4 → 3). Primeiro, ele percorre as duas listas e coloca os valores em duas listas Python (l1_num e l2_num). Depois ele inverte essas listas pra reconstruir os números na ordem certa, junta os dígitos como strings (l1_str e l2_str), transforma isso em inteiros, soma os dois, e converte o resultado de volta pra uma nova lista ligada. Começa criando o último dígito da soma como cabeça da nova lista, e vai conectando os outros dígitos em ordem reversa até acabar. No final, retorna essa nova lista com o número somado.