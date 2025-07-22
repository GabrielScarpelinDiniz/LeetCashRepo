class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        cifras = {}
        alfabeto = 'abcdefghijklmnopqrstuvwxyz'
        i = 0
        
        for c in key:
            if c != ' ' and c not in cifras:
                cifras[c] = alfabeto[i]
                i += 1
        
        resultado = ''
        for c in message:
            if c == ' ':
                resultado += ' '
            else:
                resultado += cifras[c]
        
        return resultado
