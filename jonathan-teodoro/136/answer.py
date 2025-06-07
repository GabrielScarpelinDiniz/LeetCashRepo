class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dicionario = {}
        for i in nums:
            if i in dicionario:
                dicionario[i] += 1
            else:
                dicionario[i] = 1
        
        for i,j in dicionario.items():
            if j == 1:
                return i