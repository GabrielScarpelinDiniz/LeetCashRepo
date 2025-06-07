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

Simples - hashmap que guarda a contagem de itens em um dicionario. Se ja houver adiciona 1, se nao incia em 1. Após percorre os itens de novo e vê qual que é 1. Muito simplinho é nos - BORA PRA COPA INTELI.