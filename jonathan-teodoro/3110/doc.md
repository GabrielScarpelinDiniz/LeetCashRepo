class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(len(s)-1):
            sum += abs(ord(s[i]) - ord(s[i+1]))
        return sum

exercicio muito facil pq eu tinha esquecido completamente dessa brincadeia. Mas serviu pro aprendizado, nao sabia converter char para numero ascii em python. Descobri esse metodo ord(). Muito util. No mais, nada de mais. Percorro a string e vou somando o modulo do ascii atual - o proximo. facil dms. 