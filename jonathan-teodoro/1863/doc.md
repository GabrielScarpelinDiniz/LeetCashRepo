class Solution:
    def subsetXORSum(self, nums):
        self.total = 0
        
        def dfs(index, current_xor):
            if index == len(nums):
                self.total += current_xor
                return
            dfs(index + 1, current_xor ^ nums[index])
            dfs(index + 1, current_xor)
        
        dfs(0, 0)
        return self.total

Uso DFS para explorar todos os subconjuntos possíveis do array nums. A cada chamada da função dfs, tem duas opções: incluir o número atual no XOR acumulado (current_xor ^ nums[index]) ou ignorá-lo e manter o valor atual (current_xor). Quando chega no final da lista (index == len(nums)), ele soma o XOR acumulado (current_xor) ao total. Como isso é feito para todas as combinações possíveis, o resultado final é a soma dos XORs de todos os subconjuntos.