
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapa = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapa.values():
                stack.append(char)
            elif char in mapa:
                if not stack or stack[-1] != mapa[char]:
                    return False
                stack.pop()
            else:
                return False
        
        return not stack


A função percorre cada caractere da string com um loop for, e vai empilhando os símbolos de abertura ((, {, [) em uma lista chamada stack.
quando encontra um símbolo de fechamento (), }, ]), verifica se ele combina com o último símbolo empilhado. Se combinar, remove esse último da pilha (com pop()). Se não combinar ou a pilha estiver vazia, a string é inválida.
No final, se a pilha estiver vazia, é porque todos os símbolos foram fechados corretamente, então a string é válida.