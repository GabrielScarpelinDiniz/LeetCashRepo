class Solution(object):
    def calPoints(self, operations):
        resposta = []

        for op in operations:
            if op == "C":
                if resposta:
                    resposta.pop()
            elif op == "D":
                if resposta:
                    resposta.append(2 * resposta[-1])
            elif op == "+":
                if len(resposta) >= 2:
                    resposta.append(resposta[-1] + resposta[-2])
            else:
                resposta.append(int(op))

        return sum(resposta)



