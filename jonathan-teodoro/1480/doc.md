class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums

O código percorre a lista `nums` a partir do segundo elemento (índice 1). Em cada posição `i`, ele soma o valor atual (`nums[i]`) com o valor anterior (`nums[i - 1]`) e atualiza `nums[i]` com esse resultado. Isso faz com que cada posição passe a conter a soma de todos os valores anteriores, formando a soma acumulada (running sum). No final, retorna a própria lista modificada.
