``` python
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = [0] * 101  
        for num in nums:
            freq[num] += 1

        good_pairs = 0
        for f in freq:
            if f >= 2:
                good_pairs += f * (f - 1) // 2

        return good_pairs

```
O código conta quantos pares de índices (i, j) existem no array nums onde nums[i] == nums[j] e i < j. Para isso, ele calcula a frequência de cada número e, para cada valor que aparece mais de uma vez, usa a fórmula da combinação (f * (f - 1) // 2) para contar quantos pares iguais podem ser formados com aquela frequência, somando todos os pares no final.