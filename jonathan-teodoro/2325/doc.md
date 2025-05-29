class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        seen = set()
        substitution = {}
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        index = 0
        for char in key:
            if char.isalpha() and char not in seen:
                substitution[char] = alphabet[index]
                seen.add(char)
                index += 1
                if index == 26:
                    break

        decoded = []
        for char in message:
            if char == ' ':
                decoded.append(' ')
            else:
                decoded.append(substitution[char])
        
        return ''.join(decoded)

Esse não foi tão trivial quanto parecia!
Gerei função que decodifica uma mensagem cifrada com base em uma chave personalizada. Primeiro, ele constrói uma tabela de substituição ao percorrer a string key, registrando a primeira ocorrência de cada letra minúscula única (ignorando espaços e repetições), e associa cada uma delas a uma letra do alfabeto . Em seguida, percorre a string message, substituindo cada letra com base nessa tabela (mantendo os espaços inalterados) e monta a mensagem decodificada. O resultado é uma nova string com o texto original reconstruído a partir do código secreto.