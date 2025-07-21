class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        map_s = {}
        for i in range(len(s)):
            map_s[s[i]] = i
        
        total = 0
        for i in range(len(t)):
            char = t[i]
            pos_in_s = map_s[char]
            total += abs(i - pos_in_s)
        
        return total



Primeiro, eu crio um dicionário pra guardar a posição de cada letra da string s. Assim, eu consigo saber rapidinho onde cada letra aparece. Por exemplo, se s = "abc", o dicionário fica {'a': 0, 'b': 1, 'c': 2}.

Depois, eu percorro a string t e, pra cada letra, eu vejo em que posição ela tá ali (pelo índice do loop) e comparo com a posição dela na string s, usando o dicionário que eu fiz. Aí eu calculo a diferença entre essas duas posições (com abs) e vou somando tudo. No final, eu retorno essa soma, que é o quanto as letras mudaram de lugar de s pra t.