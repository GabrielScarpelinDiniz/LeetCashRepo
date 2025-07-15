class Solution:
    def reverseDegree(self, s: str) -> int:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        total = 0
        for i in range(len(s)):
            reverse_value = 26 - alphabet.index(s[i])
            total += reverse_value * (i + 1)
        return total

primeiro monto uma string com o alfabeto e, para cada letra da palavra, descubro qual a posição dela usando .index(). Faço 26 - posição, que representa a ordem invertida. Multiplica isso pela posição da letra na string (começando de 1), soma tudo, e no fim retorna o total.