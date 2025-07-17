# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

exercicio trivial que custei a entender. MUITO SIMPLES, so mudar o atual para o proximo, faco isso invertendo o val, e apontando pro que vem apos o proximo. DUAS LINHAS DE CODIGO - IMPRESSIONANTE.