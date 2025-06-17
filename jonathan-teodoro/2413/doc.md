class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        else:
            return n * 2

Muito simples, mmc facinho - se o numero for divissel por 2 é ele mesmo, se nao é ele vezes 2.