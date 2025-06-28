class Solution:
    def countPairs(self, nums, target):
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    count += 1
        return count


Prcorre todos os pares possíveis (i, j) com i < j e conta quantos têm a soma menor que o target. Ele evita repetições e garante que a ordem dos índices seja respeitada, exatamente como o enunciado pede. Simples e direto.
