class Solution(object):
    def addTwoNumbers(self, l1, l2):
        lista = ListNode()
        atual = lista
        sobra_proximo = 0

        while l1 or l2 or sobra_proximo:
            if l1:
                val1 = l1.val 
            else: 
                val1 = 0 
            if l2:
                val2 = l2.val 
            else: 
                val2 = 0 

            soma = val1 + val2 + sobra_proximo
            sobra_proximo = soma // 10

            atual.next = ListNode(soma % 10)
            atual = atual.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return lista.next
        



# class Nodo:
#     def __init__(self, dado):
#         self.dado = dado
#         self.proximo = None

# class ListaLigada:
#     def __init__(self):
#         self.head = None

#     def append(self, dado):
#         novo_no = Nodo(dado)
#         if not self.head:
#             self.head = novo_no
#         else:
#             atual = self.head
#             while atual.proximo:
#                 atual = atual.proximo
#             atual.proximo = novo_no

#     def print_lista(self):
#         atual = self.head
#         while atual:
#             print(atual.dado, end=" -> " if atual.proximo else "")
#             atual = atual.proximo
#         print()

# def somar_listas_reversas(l1, l2) -> ListaLigada:
#     p1 = l1.head
#     p2 = l2.head
#     carry = 0
#     resultado = ListaLigada()

#     while p1 or p2 or carry:
#         val1 = p1.dado if p1 else 0
#         val2 = p2.dado if p2 else 0

#         soma = val1 + val2 + carry
#         carry = soma // 10
#         resultado.append(soma % 10)

#         if p1: p1 = p1.proximo
#         if p2: p2 = p2.proximo

#     return resultado


# l1 = ListaLigada()
# l2 = ListaLigada()
# for val in [5, 0, 0]:
#     l1.append(val)
# for val in [3, 0, 0]:
#     l2.append(val)

# print("Lista 1:")
# l1.print_lista()

# print("Lista 2:")
# l2.print_lista()


# resultado = somar_listas_reversas(l1, l2)

# print("Resultado da soma:")
# resultado.print_lista()