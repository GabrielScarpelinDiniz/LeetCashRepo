class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            answer = "-"
        else:
            answer = ""

        for i in str(x)[::-1]:
            if i != "-":
                answer += i
        print(answer)
        
        if int(answer).bit_length() >= 32:
            return 0
        return int(answer)

Inverte os dígitos de um número inteiro x. Primeiro, ele checa se o número é negativo e, se for, começa a construir a resposta com "-". Depois, ele percorre os dígitos do número convertido em string, de trás pra frente ([::-1]), e vai montando o número invertido (ignorando o sinal - se aparecer). No final, ele verifica se o número invertido ainda cabe dentro do limite de 32 bits (usando bit_length()), e se passar desse limite, retorna 0 (como o problema pede). Caso contrário, retorna o número invertido como inteiro.