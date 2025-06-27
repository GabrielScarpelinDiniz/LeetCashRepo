class Solution:
    def countConsistentStrings(self, allowed, words):
        allowed_set = set(allowed)
        count = 0

        for word in words:
            is_consistent = True
            for char in word:
                if char not in allowed_set:
                    is_consistent = False
                    break
            if is_consistent:
                count += 1

        return count

O código transforma a string allowed em um conjunto (pra procurar letras mais rápido) e depois verifica cada palavra da lista: se todas as letras da palavra estão em allowed, ela é considerada consistente e incrementa o contador. No final, ele retorna quantas palavras passaram nesse teste.