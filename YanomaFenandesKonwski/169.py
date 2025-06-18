class Solution(object):
    def majorityElement(self, nums):
        dicionario = {}
        for numero in nums:
            if numero in dicionario:
                dicionario[numero] += 1
            else:
                dicionario[numero] = 1
        mais_vezes = max(dicionario, key=lambda x:dicionario[x])
        return mais_vezes
        