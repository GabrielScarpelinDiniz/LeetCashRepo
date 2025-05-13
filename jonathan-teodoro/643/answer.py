class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        soma_da_janela = sum(nums[:k])
        soma_maxima = soma_da_janela
        for i in range(k, len(nums)):
            soma_da_janela += nums[i] - nums[i-k]
            print(soma_da_janela)
            soma_maxima = max(soma_da_janela, soma_maxima)
        
        
        return soma_maxima/k