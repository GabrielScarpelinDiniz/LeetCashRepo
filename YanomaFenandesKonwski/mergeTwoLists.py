#Código certo

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        vetor = ListNode()
        atual = vetor
        if not list1:
            return list2
        if not list2:
            return list1
        while list1 and list2:
            if list1.val<=list2.val:
                atual.next = list1
                list1 = list1.next
            else:
                atual.next = list2
                list2 = list2.next
            atual = atual.next
            if list1:
                atual.next = list1
            else:
                atual.next = list2
        return vetor.next
        
        


# list1 = [1,3,5]
# list2 = [2,4,6]


# def mergeTwoLists(list1, list2):
#     lista = []
#     i = 0
#     j = 0
#     while i<len(list1) and j<len(list2):
#         if list1[i]<=list2[j]:
#             lista.append(list1[i])
#             i+=1
#         else:
#             lista.append(list2[j])
#             j+=1

#         if i ==len(list1):
#             lista.append(list2[j])
#         elif j==len(list2):
#             lista.append(list1[i])
#     return lista

# print(mergeTwoLists(list1,list2))

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



        
        