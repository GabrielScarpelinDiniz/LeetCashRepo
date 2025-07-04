class Solution:
    def myAtoi(self, s: str) -> int:
        # Armazena o resulta
        result = 0
        # Variável para identificar se é negativo
        isNegative = False

        # Remove o primeiro white space
        s = s.lstrip()

        # Verifica se restou algo
        if not s:
            return 0

        # Verifica se o número é negativo ou positivo
        if s[0] == "-": 
            # Define como negativo
            isNegative = True
            # Remove símbolo de negativo
            s = s[1:len(s)]
        elif s[0] == "+":
            # Remove símbolo de positivo
            s = s[1:len(s)]

        # Itera sobre a string
        for i in s:
            # Caso o item seja um digito é adicionado ao resultado
            if i.isdigit():
                result *= 10
                result += int(i)
            # Caso o item não seja um digito o loop é quebrado
            else:
                break
        
        # Transforma o número em negativo
        if isNegative:
            result *= -1

        # Garante o limite superior
        if result > 2**31 -1:
            result = 2**31 - 1

        # Garante o limite inferior
        elif result < -2**31:
            result = -2**31
        
        # Retorna o resultado
        return result    