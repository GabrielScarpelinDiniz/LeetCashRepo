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