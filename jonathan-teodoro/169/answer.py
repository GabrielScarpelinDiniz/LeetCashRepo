class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maior_valor = 0
        maior_contagem = 0
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] = dict[i] + 1
            if dict[i] > maior_contagem:
                maior_valor = i
                maior_contagem = dict[i]
                print(maior_valor)
    

        return maior_valor
        