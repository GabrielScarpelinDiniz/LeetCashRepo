class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lista = nums1 + nums2
        lista.sort()
        n = len(lista)
        
        if n % 2 != 0:
            mid_index = n // 2
            return float(lista[mid_index])
        else:
            mid1 = n // 2
            mid2 = mid1 - 1
            return (lista[mid1] + lista[mid2]) / 2.0


junta os dois arrays (nums1 e nums2) em uma lista só (lista), depois ordena essa lista inteira. A mediana é o valor que fica no meio dessa lista ordenada. Se o tamanho total for ímpar, ele simplesmente pega o valor do meio e retorna como float. Se for par, ele pega os dois valores centrais, soma os dois e divide por 2.0 pra garantir que o resultado seja decimal. É uma solução direta e funciona bem para quando você pode ordenar tudo, mesmo que não seja a forma mais eficiente para grandes listas.