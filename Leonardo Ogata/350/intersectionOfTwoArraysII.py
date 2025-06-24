class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Define qual o maior e o menor array
        if len(nums1) > len(nums2):
            longer, shorter = nums1, nums2
        else:
            shorter, longer = nums1, nums2

        # Cria array auxiliar para armazenar resposta
        auxArr = []

        # Itera sobre o array menor
        for i in range(len(shorter)): 
            # Verifica se o item i está presente no array maior e remove ele do array maior
            if shorter[i] in longer:
                auxArr.append(shorter[i])
                longer.pop(longer.index(shorter[i]))

        # Retorna o array auxiliar  
        return auxArr
        