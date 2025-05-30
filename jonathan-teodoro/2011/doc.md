A variável X começa com o valor 0. Para cada operação na lista operations, verificamos se a string contém "++" (seja ++X ou X++), o que indica um incremento de 1 em X. Caso contrário, a operação será um decremento (--X ou X--), então subtraímos 1. Como o problema especifica que todas as operações são apenas incrementos ou decrementos, não é necessário tratar cada variação separadamente — basta verificar a presença de "++" para decidir se somamos ou subtraímos. Ao final, retornamos o valor acumulado de X.

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for i in operations:
            if '++' in i:
                X += 1
            else:
                X -= 1
        return X