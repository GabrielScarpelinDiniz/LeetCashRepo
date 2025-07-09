class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])     
            result.append(nums[i + n]) 
        return result

Cria uma lista vazia e percorre os índices de 0 até n-1. Em cada passo, ele adiciona primeiro o elemento da primeira metade (x_i) e depois o correspondente da segunda metade (y_i) do array original. Assim, ele intercala os elementos na ordem desejada, formando o array embaralhado que é retornado no final.