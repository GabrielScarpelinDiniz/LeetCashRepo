class Solution:
    def minOperations(self, boxes):
        n = len(boxes)
        answer = [0] * n

        count = 0  
        ops = 0    
        for i in range(n):
            answer[i] += ops
            if boxes[i] == '1':
                count += 1
            ops += count

        count = 0
        ops = 0
        for i in range(n - 1, -1, -1):
            answer[i] += ops
            if boxes[i] == '1':
                count += 1
            ops += count

        return answer

Esse código calcula quantas operações são necessárias para mover todas as bolas até cada caixa. Ele faz isso em duas passadas: na primeira, da esquerda pra direita, ele soma o custo de trazer as bolas que já viu até cada posição; na segunda, da direita pra esquerda, faz a mesma coisa com as bolas que vêm do outro lado. No final, cada posição tem a soma dos dois lados — ou seja, o total de passos que todas as bolas fariam pra chegar ali.