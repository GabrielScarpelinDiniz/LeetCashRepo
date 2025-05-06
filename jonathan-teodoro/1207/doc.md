class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dicionario = {}
        for i in arr:
            if i in dicionario:
                dicionario[i] += 1
            else:
                dicionario[i] = 1
        
        visto = set()
        for i in dicionario.values():
            if i in visto:
                return False
            visto.add(i)

        return True

Trivial

Usando hashmap para esse exercicio gostosinho. Primeiro adiciono a contagem de itens em um set. Depois eu percorro os valores do set marcando os vistos e procurando se já passamos por esse valor. Se sim retornamos false, se não adicionamos ao contador e retornamos false. 

Complexidade O(N) bem suavinho