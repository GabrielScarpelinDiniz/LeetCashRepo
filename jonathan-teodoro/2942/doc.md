class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i, word in enumerate(words):
            if x in word:
                result.append(i)
        return result

codigo simples - a gente passa por cada palavra da lista e, se a letra que a gente tá procurando estiver dentro dela, a gente anota o índice (a posição) dessa palavra. No final, a gente devolve uma lista com esses índices. 