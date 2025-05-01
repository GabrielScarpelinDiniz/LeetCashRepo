list1 = [1,3,5]
list2 = [2,4,6]


def mergeTwoLists(list1, list2):
    lista = []
    i = 0
    j = 0
    while i<len(list1) and j<len(list2):
        if list1[i]<=list2[j]:
            lista.append(list1[i])
            i+=1
        else:
            lista.append(list2[j])
            j+=1

        if i ==len(list1):
            lista.append(list2[j])
        elif j==len(list2):
            lista.append(list1[i])
    return lista

print(mergeTwoLists(list1,list2))